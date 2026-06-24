---
title: MNIST Digit Recognizer
emoji: 🔢
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 3.50.2
app_file: app.py
pinned: false
---

# MNIST Digit Recognizer 🔢

A deep learning model that recognizes handwritten digits (0-9) built from scratch using PyTorch and deployed with Gradio on HuggingFace Spaces.

## 🚀 Live Demo
[Try it here](https://jayeshmurthi49-byte-mnist-digit-recognizer.hf.space)

## 📌 Project Overview
This project is part of my 6-month AI Engineer roadmap (Phase 4 — Deep Learning).
The model is a Multi Layer Perceptron (MLP) trained on the MNIST dataset of 70,000 handwritten digit images.

## 🧠 What I Built
- Built a neural network from scratch using PyTorch
- Trained on 60,000 images, tested on 10,000 images
- Achieved ~97% test accuracy
- Deployed live using Gradio on HuggingFace Spaces

## 🏗️ Model Architecture
Input → 784 neurons (28×28 flattened)
Hidden Layer 1 → 128 neurons + ReLU
Hidden Layer 2 → 64 neurons + ReLU
Output Layer → 10 neurons (digits 0-9)
Loss Function → CrossEntropyLoss
Optimizer → Adam (lr=0.001)
Epochs → 5

## 📊 Dataset
- Name: MNIST
- Training images: 60,000
- Test images: 10,000
- Image size: 28×28 grayscale
- Classes: 10 (digits 0 to 9)

## 🛠️ Tech Stack
- Python
- PyTorch
- Gradio
- HuggingFace Spaces
- Pillow

## 📁 Project Structure
app.py           → Gradio UI and prediction logic
train.py         → Model training and saving
model.pkl        → Trained model weights
requirements.txt → Dependencies

## 💡 Concepts Used
- Multi Layer Perceptron (MLP)
- Forward Propagation
- Backpropagation
- ReLU Activation Function
- CrossEntropy Loss
- Adam Optimizer
- Gradient Descent

## 🔗 Connect
- GitHub: https://github.com/jayeshmurthi49-byte
- LinkedIn: https://linkedin.com/in/jayesh-murthi-8b1653400