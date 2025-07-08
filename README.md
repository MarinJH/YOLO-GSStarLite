# YOLO-GSStarLite

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Dataset](#dataset)
- [Model Usage Instructions](#model-usage-instructions)  
- [Code of Conduct](#code-of-conduct)

## Introduction

YOLO-GSStarLite is an innovative and lightweight weed detection algorithm derived from YOLOv8n, designed to enhance detection accuracy and processing speed while minimizing false positives and negatives in complex agricultural settings. This repository contains the source code and resources related to the development and evaluation of YOLO-GSStarLite.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- Git installed to clone the repository
- Necessary dependencies listed in `requirements.txt`

### Installation

To get started with YOLO-GSStarLite, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MarinJH/YOLO-GSStarLite.git
   cd YOLO-GSStarLite

## Dataset

Due to the large size of the complete agricultural image dataset used for training YOLO-GSStarLite, we are unable to host the full dataset directly on GitHub. 

This repository contains:
- A curated subset of sample images
- Annotation examples

For research access to the **complete dataset** (over 8000+ high-resolution field images with comprehensive annotations), please contact us via email: [x15014082116@163.com](mailto:x15014082116@163.com). Include your research affiliation and intended use case.

## Model Usage Instructions

Follow these steps to properly use YOLO-GSStarLite for your weed detection tasks:

### 1. Install Dependencies
First install all required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### 2. Train your Model
```bash
   python train.py --data data.yaml --weights model.pt --epochs 200
   ```
###3. Evaluate the Model
```bash
   python evaluate.py --weights runs/train/exp/weights/best.pt --data data.yaml
   ```
## Code of Conduct

### Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of:

- Age
- Body size
- Visible or invisible disability
- Ethnicity
- Sex characteristics  
- Gender identity and expression
- Level of experience
- Education
- Socio-economic status
- Nationality
- Personal appearance
- Race
- Religion
- Sexual identity and orientation

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.
