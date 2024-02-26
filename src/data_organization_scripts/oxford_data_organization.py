import os
import shutil
import random

def mudar_dir():
    # Diretório onde estão as imagens
    diretorio_origem = 'datasets/oxford-iiit-pet/annotations/xmls'
    diretorio_destino = 'datasets/oxford-iiit-pet/annotations/xmls/dogs'

    # Criar o diretório de destino se não existir
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Iterar sobre os arquivos no diretório de origem
    for filename in os.listdir(diretorio_origem):
        # Verificar se o arquivo começa com letra minúscula (cachorro)
        print(filename)
        if filename[0].islower() and filename!="dogs":
            # Construir o caminho completo do arquivo de origem
            caminho_origem = os.path.join(diretorio_origem, filename)
            print(caminho_origem)
            # Construir o caminho completo do arquivo de destino
            caminho_destino = os.path.join(diretorio_destino, filename)
            print(caminho_destino)
            # Copiar o arquivo para o diretório de destino
            shutil.move(caminho_origem, caminho_destino)

def separar_img_anotacao():
    # Diretório onde estão as imagens
    diretorio_imagens = 'datasets/oxford-iiit-pet/i'
    # Diretório onde estão as anotações
    diretorio_anotacoes = 'datasets/oxford-iiit-pet/annotations/xmls/dogs'
    # Diretório onde deseja mover as imagens com anotações
    diretorio_destino = 'datasets/oxford-iiit-pet/images/dogs_anotated'

    # Criar o diretório de destino se não existir
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Listar todos os arquivos de anotação
    arquivos_anotacoes = os.listdir(diretorio_anotacoes)

    # Iterar sobre os arquivos de anotação
    for arquivo_anotacao in arquivos_anotacoes:
        # Verificar se o arquivo de anotação corresponde a uma imagem
        if arquivo_anotacao.endswith('.xml'):
            # Construir o nome da imagem correspondente
            nome_imagem = os.path.splitext(arquivo_anotacao)[0] + '.jpg'
            # Verificar se a imagem correspondente existe
            if nome_imagem in os.listdir(diretorio_imagens):
                # Construir os caminhos completos dos arquivos
                caminho_imagem = os.path.join(diretorio_imagens, nome_imagem)
                caminho_anotacao = os.path.join(diretorio_anotacoes, arquivo_anotacao)
                # Mover a imagem com anotação para o diretório de destino
                shutil.move(caminho_imagem, diretorio_destino)
                # Opcional: também mover a anotação para o diretório de destino
                shutil.move(caminho_anotacao, diretorio_destino)

def separ_treino_test_val():
    # Diretório principal
    diretorio_principal = 'datasets/oxford-iiit-pet'

    # Diretórios de cães e anotações
    diretorio_caes = os.path.join(diretorio_principal, 'images')
    # diretorio_anotacoes = os.path.join(diretorio_principal, 'dogs_anotation')

    # Diretórios para os conjuntos de treinamento, teste e validação
    diretorio_treinamento = os.path.join(diretorio_principal, 'treinamento')
    diretorio_teste = os.path.join(diretorio_principal, 'teste')
    diretorio_validacao = os.path.join(diretorio_principal, 'validacao')

    # Proporção de dados para cada conjunto (treinamento, teste, validação)
    proporcao_treinamento = 0.6
    proporcao_teste = 0.1
    proporcao_validacao = 0.3

    # Criar diretórios de treinamento, teste e validação
    for diretorio in [diretorio_treinamento, diretorio_teste, diretorio_validacao]:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

    # Listar os arquivos de cães e anotações
    arquivos_caes = os.listdir(diretorio_caes)
    # arquivos_anotacoes = os.listdir(diretorio_anotacoes)

    # Embaralhar os arquivos
    random.shuffle(arquivos_caes)
    # random.shuffle(arquivos_anotacoes)

    # Calcular os índices de corte para cada conjunto
    indice_treinamento = int(len(arquivos_caes) * proporcao_treinamento)
    indice_teste = int(len(arquivos_caes) * (proporcao_treinamento + proporcao_teste))

    # Mover os arquivos para os diretórios correspondentes
    for arquivo in arquivos_caes[:indice_treinamento]:
        shutil.move(os.path.join(diretorio_caes, arquivo), diretorio_treinamento)
    for arquivo in arquivos_caes[indice_treinamento:indice_teste]:
        shutil.move(os.path.join(diretorio_caes, arquivo), diretorio_teste)
    for arquivo in arquivos_caes[indice_teste:]:
        shutil.move(os.path.join(diretorio_caes, arquivo), diretorio_validacao)

    # Repetir para os arquivos de anotações
    # for arquivo in arquivos_anotacoes[:indice_treinamento]:
    #     shutil.move(os.path.join(diretorio_anotacoes, arquivo), diretorio_treinamento)
    # for arquivo in arquivos_anotacoes[indice_treinamento:indice_teste]:
    #     shutil.move(os.path.join(diretorio_anotacoes, arquivo), diretorio_teste)
    # for arquivo in arquivos_anotacoes[indice_teste:]:
    #     shutil.move(os.path.join(diretorio_anotacoes, arquivo), diretorio_validacao)



def sep_imagens():
    
    # Diretório onde estão as imagens
    diretorio_imagens = 'datasets/oxford-iiit-pet/images'
    # Diretório onde estão as anotações de treinamento, teste e validação
    diretorio_treinamento = 'datasets/oxford-iiit-pet/treinamento'
    diretorio_teste = 'datasets/oxford-iiit-pet/teste'
    diretorio_validacao = 'datasets/oxford-iiit-pet/validacao'

    # Iterar sobre os diretórios de anotações
    for diretorio_anotacoes in [diretorio_treinamento, diretorio_teste, diretorio_validacao]:
        # Listar os arquivos de anotação
        arquivos_anotacoes = os.listdir(diretorio_anotacoes)
        # Iterar sobre os arquivos de anotação
        for arquivo_anotacao in arquivos_anotacoes:
            # Verificar se o arquivo de anotação corresponde a uma imagem
            if arquivo_anotacao.endswith('.xml'):
                # Construir o nome da imagem correspondente
                nome_imagem = os.path.splitext(arquivo_anotacao)[0] + '.jpg'
                # Verificar se a imagem correspondente existe
                if nome_imagem in os.listdir(diretorio_imagens):
                    # Construir os caminhos completos dos arquivos
                    caminho_imagem = os.path.join(diretorio_imagens, nome_imagem)
                    caminho_anotacao = os.path.join(diretorio_anotacoes, arquivo_anotacao)
                    # Mover a imagem para o diretório de anotações
                    shutil.move(caminho_imagem, diretorio_anotacoes)

sep_imagens()