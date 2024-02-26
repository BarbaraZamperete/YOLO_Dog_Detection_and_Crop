from crop_image import crop_image
from yolo_detect_dog import predict
from eye_detection_rotation import detect_eye
import glob



if __name__ == "__main__":


    paths = glob.glob("C:/Users/Bárbara Z/Desktop/TCC-Codes/Datasets/Images_meus_dogs/Train/**/*.jpg", recursive=True)
    paths = [path.replace("\\", "/") for path in paths]
    print(paths)
    # paths = ["images/guida2.jpg"]
    output_dir_crop = "cropped_images"
    output_dir_aling = "aligns_images"

    results = predict(paths)
    # print(results)
    crop_paths = crop_image(results, paths, output_dir_crop)
    # print(crop_paths)
    # detect_eye(crop_paths, output_dir_aling)
