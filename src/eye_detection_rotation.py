import cv2
import numpy as np
import os

def detect_eye(paths, output_dir):
    # Carregar o classificador em cascata para detecção de olhos
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    os.makedirs(output_dir, exist_ok=True)

    for path in paths:
        image = cv2.imread(path)
        image_name = os.path.basename(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Verificar se foram detectados pelo menos dois olhos
        if len(eyes) >= 2:
            new_image = rotate_image(image, eyes)
            output_path = os.path.join(output_dir, image_name)
            cv2.imwrite(output_path, new_image)
        else:
            print("Não foram detectados olhos suficientes para realizar a rotação.")
        
        

def rotate_image(image, eyes):
    # Calcular os centros dos olhos
    eye_centers = [(x + w//2, y + h//2) for (x, y, w, h) in eyes]
    
    # Calcular o ângulo de rotação (em graus) com base na linha dos olhos
    angle = np.arctan2(eye_centers[1][1] - eye_centers[0][1], eye_centers[1][0] - eye_centers[0][0]) * 180 / np.pi
    
    # Calcular o centro da imagem
    center = (image.shape[1] // 2, image.shape[0] // 2)
    
    # Rotacionar a imagem com base no ângulo calculado
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), flags=cv2.INTER_LINEAR)
    
    return rotated_image

detect_eye(["cropped_images/scooby-02.jpg"], "aligns_images")