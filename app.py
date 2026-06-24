import torch
import torch.nn as nn
from torchvision import transforms
import gradio as gr
from PIL import Image 

# Define same MLP 
class MLP(nn.Module):
    def __init__(self):
        super(MLP,self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
        self.relu = nn.ReLU() 


    def forward(self,x):
        x = x.view(-1,28*28)
        x = self.relu(self.fc1(x)) 
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x 
    
# Load model
model = MLP() 
model.load_state_dict(torch.load('model.pkl',map_location=torch.device('cpu')))
model.eval() 

# Predict function 
def predict(image):
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((28,28)),
        transforms.ToTensor()
    ])
    image = Image.fromarray(image.astype('uint8'))
    tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(tensor)
        predicted  = torch.argmax(output,dim=1).item()
    return f"Predicted Digit: {predicted}"   

# Gradio UI 
app = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Textbox(),
    title="MNIST Digit Recognizer",
    description="Draw or upload a digit (0-9) and the model will predict it"

)
app.launch()