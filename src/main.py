from crop_image import crop_image
from yolo_detect_dog import predict
import glob



if __name__ == "__main__":
    

    paths = glob.glob("images/*.jpeg")
    paths = [path.replace("\\", "/") for path in paths]
    output_dir = "cropped_images"

    results = predict(paths)
    crop_image(results, paths, output_dir)