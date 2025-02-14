
from ultralytics import YOLO

# Load YOLO Model
model = YOLO('yolov8n.yaml')  # Use a pre-trained model

results = model.train(data = 'config.yaml', epochs = 100)

# Show Results
print(results)



