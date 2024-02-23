from ultralytics import YOLO
import cv2
import os

def crop_image(results, paths, output_dir):

    os.makedirs(output_dir, exist_ok=True)
    # Process results list
    crop_paths = []
    for result, path in zip(results, paths) :
        image = cv2.imread(path)
        image_name = os.path.basename(path)
        print(result.boxes)
        for box in result.boxes:
            print("box:")
            print(box)
            xmin, ymin, xmax, ymax = box.xyxy[-1]
            print("Coordenadas:")
            print(xmin, ymin, xmax, ymax)
            cropped_image = image[int(ymin):int(ymax), int(xmin):int(xmax)]
            
            output_path = os.path.join(output_dir, image_name)
            crop_paths.append(output_path)
            cv2.imwrite(output_path, cropped_image)
        # result.show()  # display to screen
        # result.save(filename='result.jpg')  # save to disk
            
    return crop_paths

