from ultralytics import YOLO

model = YOLO('model/yolov8n.pt')  # pretrained YOLOv8n model
# Training.
results = model.train(
   data='D:/Bah/Documentos/ESTUDO/UFRR/TCC/TCC-Codes/YOLO_Dog_Detection_and_Crop/potdog_v8.yaml',
   imgsz=224,
   epochs=50,
   batch=107,
   name='yolov8n_dogface_oxford_100epochs'
)