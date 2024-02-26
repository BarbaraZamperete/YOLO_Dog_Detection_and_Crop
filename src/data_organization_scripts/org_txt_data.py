import os
import cv2

def obter_dimensoes_imagem(caminho_imagem):
    # Carregar a imagem usando OpenCV
    imagem = cv2.imread(caminho_imagem)
    # Obter as dimensões da imagem
    altura, largura, _ = imagem.shape
    return largura, altura

def converter_coordenadas(arquivo_entrada, diretorio_imagens, diretorio_saida):
    # Garantir que o diretório de saída exista
    os.makedirs(diretorio_saida, exist_ok=True)

    # Listar os arquivos de entrada
    arquivos_txt = os.listdir(arquivo_entrada)

    for arquivo_txt in arquivos_txt:
        # Construir caminho completo para o arquivo de imagem correspondente
        nome_arquivo = os.path.splitext(arquivo_txt)[0]
        caminho_imagem = os.path.join(diretorio_imagens, nome_arquivo + '.jpg')

        # Obter dimensões da imagem
        largura_imagem, altura_imagem = obter_dimensoes_imagem(caminho_imagem)

        # Abrir arquivo de entrada e criar arquivo de saída
        with open(os.path.join(arquivo_entrada, arquivo_txt), 'r') as f_in, \
             open(os.path.join(diretorio_saida, arquivo_txt), 'w') as f_out:
            for linha in f_in:
                dados = linha.strip().split()  # Ler dados do arquivo de entrada
                classe = dados[0]
                xmax, ymax, xmin, ymin = map(float, dados[1:])  # Coordenadas da caixa delimitadora

                # Calcular coordenadas x_center, y_center, width, height normalizadas
                x_center = (xmin + xmax) / (2 * largura_imagem)
                y_center = (ymin + ymax) / (2 * altura_imagem)
                width = (xmax - xmin) / largura_imagem
                height = (ymax - ymin) / altura_imagem

                # Escrever dados no formato especificado no arquivo de saída
                f_out.write(f"{classe} {x_center} {y_center} {width} {height}\n")

# Exemplo de uso:
diretorio_arquivos_txt = 'datasets/oxford-iiit-pet/validacao/labels'
diretorio_imagens = 'datasets/oxford-iiit-pet/validacao/images'
diretorio_saida = 'datasets/oxford-iiit-pet/validacao/annotations'

converter_coordenadas(diretorio_arquivos_txt, diretorio_imagens, diretorio_saida)
