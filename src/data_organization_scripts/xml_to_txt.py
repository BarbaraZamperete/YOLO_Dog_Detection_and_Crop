import os
import xml.etree.ElementTree as ET

def converter_xml_para_txt(arquivo_xml, arquivo_txt):
    # Parse do arquivo XML
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()

    # Inicializar uma lista para armazenar os dados a serem escritos no arquivo TXT
    dados_txt = []

    # Iterar sobre todos os objetos anotados no XML
    for obj in root.findall('object'):
        # Extrair rótulo e coordenadas da caixa delimitadora
        label = obj.find('name').text
        if label == 'dog':
            xmax = int(obj.find('bndbox').find('xmax').text)
            ymax = int(obj.find('bndbox').find('ymax').text)
            xmin = int(obj.find('bndbox').find('xmin').text)
            ymin = int(obj.find('bndbox').find('ymin').text)
            # Adicionar os dados formatados à lista
            dados_txt.append(f"0 {xmax} {ymax} {xmin} {ymin}")

    # Abrir arquivo TXT para escrita e escrever os dados
    with open(arquivo_txt, 'w') as f:
        f.write('\n'.join(dados_txt))

# Diretório onde estão os arquivos XML de anotação
diretorio_xml = 'datasets/oxford-iiit-pet/teste/anotations'
# Diretório onde serão salvos os arquivos TXT de anotação
diretorio_txt = 'datasets/oxford-iiit-pet/teste/txt'

# Listar os arquivos XML de anotação
arquivos_xml = os.listdir(diretorio_xml)

# Converter cada arquivo XML para TXT
for arquivo_xml in arquivos_xml:
    nome_base = os.path.splitext(arquivo_xml)[0]
    arquivo_txt = os.path.join(diretorio_txt, nome_base + '.txt')
    converter_xml_para_txt(os.path.join(diretorio_xml, arquivo_xml), arquivo_txt)