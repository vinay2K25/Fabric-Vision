from ultralytics import YOLO

# Loading a pre-trained YOLOv8 model!
model = YOLO('yolov8n.pt')

# Train the model on the custom data-set!
results = model.train(data = 'data.yaml', epochs = 25, imgsz = 640, plots = True)