from ultralytics import YOLO

model = YOLO('model/yolov8n.pt')  # pretrained YOLOv8n model
# Training.
results = model.train(
   data='potdog_v8.yaml',
   imgsz=224,
   epochs=10,
   batch=32,
   name='yolov8n_dogface_oxford'
)