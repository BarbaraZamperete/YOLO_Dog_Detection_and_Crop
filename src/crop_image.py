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
            cropped_image = image[int(xmin):int(xmax), int(ymin):int(ymax)]
            
            output_path = os.path.join(output_dir, image_name)
            crop_paths.append(output_path)
            cv2.imshow("cro",cropped_image)
            cv2.waitKey(0)  # Aguarda até que uma tecla seja pressionada
            cv2.destroyAllWindows()  # Fecha todas as janelas abertas
            # cv2.imwrite(output_path, cropped_image)
        # result.show()  # display to screen
        # result.save(filename='result.jpg')  # save to disk
            
    return crop_paths

