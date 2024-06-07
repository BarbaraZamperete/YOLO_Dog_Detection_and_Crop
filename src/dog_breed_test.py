from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
import numpy as np

def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))  # Tamanho padrão para Xception
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def predict_breed(model, img_path):
    print("Pré processando imagem")
    processed_image = load_and_preprocess_image(img_path)
    print("Pré processamento concluido")
    print("Iniciando predição")
    predictions = model.predict(processed_image)
    print("Predições concluidas")
    return predictions

class_names = [
    'chihuahua', 'spaniel_japonês', 'cão_maltês', 'pequinês', 'shih_tzu', 'spaniel_blenheim', 'papillon',
    'terrier_de_bolso', 'ridgeback_do_rhodesia', 'cão_afegão', 'basset', 'beagle', 'bloodhound', 'bluetick', 'coonhound_preto_e_castanho', 'foxhound_americano',
    'foxhound_inglês', 'redbone', 'borzoi', 'wolfhound_irlandês', 'greyhound_italiano', 'whippet', 'podengo_ibicenco', 'elkhound_norueguês',
    'cão_de_lontra', 'saluki', 'deerhound_escocês', 'weimaraner', 'bullterrier_staffordshire', 'terrier_staffordshire_americano',
    'terrier_bedlington', 'terrier_border', 'terrier_azul_de_kerry', 'terrier_irlandês', 'terrier_norfolk', 'terrier_norwich',
    'terrier_yorkshire', 'fox_terrier_de_pelo_duro', 'terrier_lakeland', 'terrier_sealyham', 'airedale', 'cairn', 'terrier_australiano',
    'dinmont_dandie', 'bull_boston', 'schnauzer_miniatura', 'schnauzer_gigante', 'schnauzer_padrão', 'terrier_escocês',
    'terrier_tibetano', 'terrier_silky', 'terrier_de_revestimento_macio', 'terrier_branco_da_montanha_ocidental', 'lhasa_apso', 'retriever_de_revestimento_plano',
    'retriever_de_revestimento_encaracolado', 'retriever_dourado', 'retriever_labrador', 'retriever_da_baía_de_chesapeake', 'pointer_alemão_de_pelo_curto',
    'vizsla', 'setter_inglês', 'setter_irlandês', 'setter_gordon', 'spaniel_bretão', 'clumber_spaniel', 'springer_spaniel_inglês',
    'springer_spaniel_galês', 'spaniel_cocker', 'spaniel_sussex', 'spaniel_irlandês_d’água', 'kuvasz', 'schipperke', 'groenendael', 'malinois', 'briard', 'kelpie', 'komondor',
    'cão_de_pastoreio_antigo_inglês', 'cão_de_pastoreio_da_ilha_shetland', 'collie', 'collie_border', 'bouvier_dos_flandres', 'rottweiler',
    'pastor_alemão', 'doberman', 'pinscher_miniatura', 'cão_de_montanha_suíço', 'cão_de_montanha_bernês', 'appenzeller',
    'entlebucher', 'boxer', 'bullmastiff', 'mastim_tibetano', 'bulldog_francês', 'grande_dinamarquês', 'são_bernardo', 'cão_eskimo',
    'malamute', 'husky_siberiano', 'affenpinscher', 'basenji', 'pug', 'leonberg', 'terranova', 'grande_pirineus',
    'samoyed', 'pomerânia', 'chow_chow', 'keeshond', 'griffon_de_bruxelas', 'pembroke', 'cardigan', 'poodle_toy', 'poodle_miniatura',
    'poodle_padrão', 'cão_sem_pelo_mexicano', 'dingo', 'dhole', 'cão_caçador_africano'
]


# Carregue o modelo treinado
print("Carregando modelo")
model = load_model('D:/Bah/Documentos/ESTUDO/UFRR/TCC/TCC-Codes/YOLO_Dog_Detection_and_Crop/src/dog_breed_xception_part1.h5')
print("Modelo carregado")
# Caminho da imagem a ser testada
print("Carregando imagem")
img_path = 'D:/Bah/Documentos/ESTUDO/UFRR/TCC/TCC-Codes/Datasets/Images_meus_dogs - Copia/Train/bolinha/bolinha-03.jpeg'
print("Imagem carregada")
predictions = predict_breed(model, img_path)

# Converter as previsões para uma lista de tuplas (pontuação, raça) e ordenar
predictions_list = [(score, class_names[i]) for i, score in enumerate(predictions[0])]
predictions_list.sort(reverse=True, key=lambda x: x[0])
top = predictions_list[:10]
# Exibir as previsões ordenadas
for i, (score, breed) in enumerate(top, 1):
    print(f"{i}º {breed}: {score*100}%")