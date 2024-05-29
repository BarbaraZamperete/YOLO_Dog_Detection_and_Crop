import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.applications import Xception
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

# Carregar o conjunto de dados Stanford Dogs
print("Carregando o conjunto de dados Stanford Dogs...")
(train_ds, val_ds), ds_info = tfds.load(
    'stanford_dogs',
    split=['train', 'test'],
    with_info=True,
    as_supervised=True,
)
print("Conjunto de dados carregado com sucesso.")

num_classes = ds_info.features['label'].num_classes

# Função de pré-processamento
def preprocess_image(image, label):
    image = tf.image.resize(image, (299, 299))
    image = image / 255.0
    return image, label

print("Pré-processando os conjuntos de dados...")
# Aplicar o pré-processamento aos conjuntos de dados
train_ds = train_ds.map(preprocess_image).batch(32).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
val_ds = val_ds.map(preprocess_image).batch(32).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
print("Pré-processamento concluído.")

# Construir o modelo Xception
print("Construindo o modelo Xception...")
base_model = Xception(weights='imagenet', include_top=False, input_shape=(299, 299, 3))

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
print("Modelo Xception construído com sucesso.")

# Congelar as camadas base
print("Congelando as camadas base...")
for layer in base_model.layers:
    layer.trainable = False
print("Camadas base congeladas.")

# Compilar o modelo
print("Compilando o modelo...")
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
print("Modelo compilado.")

# Treinar o modelo
print("Iniciando o treinamento do modelo (primeira fase)...")
model.fit(
    train_ds,
    epochs=10,
    validation_data=val_ds
)
print("Primeira fase do treinamento concluída.")

# Descongelar as camadas base para ajuste fino
print("Descongelando as camadas base para ajuste fino...")
for layer in base_model.layers:
    layer.trainable = True
print("Camadas base descongeladas.")

# Recompilar o modelo para ajuste fino
print("Recompilando o modelo para ajuste fino...")
model.compile(optimizer=Adam(learning_rate=0.00001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
print("Modelo recompilado.")

# Treinar o modelo novamente
print("Iniciando o ajuste fino do modelo (segunda fase)...")
model.fit(
    train_ds,
    epochs=10,
    validation_data=val_ds
)
print("Segunda fase do treinamento concluída.")

# Salvar o modelo treinado
print("Salvando o modelo treinado...")
model.save('dog_breed_xception.h5')
print("Modelo salvo com sucesso.")
