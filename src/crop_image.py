from ultralytics import YOLO
import cv2
import os
import math

def crop_image(results, paths, output_dir):

    os.makedirs(output_dir, exist_ok=True)
    # Process results list
    crop_paths = []
    for (result, path) in zip(results, paths):
        image = cv2.imread(path)
        image_name = os.path.basename(path)
        # print(result.boxes)
        for j, box in enumerate(result.boxes):
            xmin, ymin, xmax, ymax = box.xyxy[-1]

            # Determinar a orientação da imagem (deitada ou não)
            altura, largura, _ = image.shape
            if altura > largura:  # Se a altura for maior que a largura, a imagem está deitada
                xmin, ymin, xmax, ymax = ymin, xmin, ymax, xmax  # Trocar as coordenadas

            # Print para verificar as coordenadas após a troca (opcional)
            print("Coordenadas após ajuste:")
            print(xmin, ymin, xmax, ymax)

            # Convertendo as coordenadas para inteiros, arredondando conforme necessário
            xmin, ymin, xmax, ymax = map(lambda x: math.ceil(x) if x % 1 > 0.5 else math.floor(x), (xmin, ymin, xmax, ymax))
            print("Coordenadas após arredondar:")
            print(xmin, ymin, xmax, ymax)
            # Recorte da imagem com as coordenadas ajustadas
            cropped_image = image[ymin:ymax, xmin:xmax]

            # Construir o nome do arquivo com sufixo único para cada cachorro
            base_name, extension = os.path.splitext(image_name)
            output_name = f"{base_name}_{j+1}{extension}"
            output_path = os.path.join(output_dir, output_name)

            # Verificar se o nome do arquivo já existe e, se sim, incrementar o índice
            while os.path.exists(output_path):
                j += 1
                output_name = f"{base_name}_{j+1}{extension}"
                output_path = os.path.join(output_dir, output_name)

            # Salvar o arquivo recortado
            cv2.imwrite(output_path, cropped_image)
            crop_paths.append(output_path)

        result.show()  # display to screen
        # result.save(filename='result.jpg')  # save to disk

    return crop_paths


