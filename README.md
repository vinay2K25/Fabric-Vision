# Fabric-Vision

An AI powered web-application that detects and highlights textile defects using classical computer vision and YOLOv8 deep learning. 

## Features

* **Interactive Web-UI:** Built with Streamlit, allowing users to seamlessly upload fabric images and instantly visualize inspection results.
* **Real-time Parameter Tuning:** Features interactive sidebars to adjust confidence thresholds and anomaly sensitivities on the fly.
* **Dual-Engine Back-end:**
	* **Version One (Classical CV):** Utilizes OpenCV and NumPy to perform Statistical Frequency Anomaly Detection. It flattens images to find rare RGB-triplets (like stains or discolored threads) and masks them.
	* **Version Two (Deep Learning):** Utilizes a custom-trained YOLOv8 object detection model (via PyTorch/Ultralytics) to identify complex structural anomalies like physical tears, holes and thread pulls.

## Tech-Stack

* **Language:** Python
* **Front-end:** Streamlit
* **Computer Vision:** OpenCV, NumPy
* **Deep Learning:** PyTorch, Ultralytics

## How to Run Locally

1. **Clone the repository:**
```bash
git clone https://github.com/vinay2K25/Fabric-Vision.git
cd Fabric-Vision
```

2. **Install the required dependencies:**
```bash
pip install streamlit opencv-python numpy ultralytics 
```

3. **Launch the application:**
```bash
streamlit run app.py
```

*The application will automatically open in your default web-browser at* http://localhost:8501

## Model Training Details

The YOLOv8 model was fine-tuned on a custom dataset of fabric defects (sourced from Roboflow).
* **Epochs:** 25
* **Image Size:** 640 x 640
* **Classes Detected:** General Fabric Defects (Tears, Stains, Thread Pulls)
*(Note: The dataset and the heavy* .pt *model weights are excluded from this repository via* .gitignore *to keep the code-base lightweight)*
