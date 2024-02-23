from ultralytics import YOLO

def predict(paths):
    # Load a model
    model = YOLO('model/yolov8n.pt')  # pretrained YOLOv8n model
    # Run batched inference on a list of images
    results = model(paths, classes=16)  # return a list of Results objects
    # results = model.predict('guida.jpeg', classes=16)

    return results
