from ultralytics import YOLO

# Loading a pre-trained YOLOv8 model! We're now using the small-model instead of the nano-model!
model = YOLO('yolov8s.pt')

# Train the model on the custom data-set!
# fdvtwo = Fabric detector version two!
results = model.train(data = 'data.yaml', epochs = 25, imgsz = 640, batch = 16, plots = True, name = "fdvtwo")