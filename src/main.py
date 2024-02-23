from crop_image import crop_image
from yolo_detect_dog import predict
from eye_detection_rotation import detect_eye
import glob



if __name__ == "__main__":
    

    paths = glob.glob("images/*.jpeg")
    paths = [path.replace("\\", "/") for path in paths]
    output_dir_crop = "cropped_images"
    output_dir_aling = "aligns_images"

    results = predict(paths)
    crop_paths = crop_image(results, paths, output_dir_crop)
    print(crop_paths)
    detect_eye(crop_paths, output_dir_aling)
