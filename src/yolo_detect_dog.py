from ultralytics import YOLO

def predict(paths):
    # Load a model
    # model = YOLO('model/yolov8n.pt')  # pretrained YOLOv8n model
    model = YOLO('runs/detect/yolov8n_dogface2/weights/best.pt') #my model
    # Run batched inference on a list of images
    results = model(paths)  # return a list of Results objects
    # results = model.predict('guida.jpeg', classes=16)
    return results

# results = predict(["datasets/dataset-kagle/valid/images/n02085620_712.jpg"])
# print(results)