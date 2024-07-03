import numpy as np
import os
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras import layers
from keras.models import Sequential


### Dataset Website:
# https://www.kaggle.com/datasets/grassknoted/asl-alphabet/data


base_dir = '/asl_alphabet_train/'  # Update this path
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size=(200, 200),
    batch_size=20,
    subset='training',
    class_mode='categorical')

validation_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size=(200, 200),
    batch_size=20,
    subset='validation',
    class_mode='categorical')


model = Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(train_generator.num_classes, activation='softmax')
])
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=15,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size)

val_loss, val_acc = model.evaluate(validation_generator)
print(f"Validation accuracy: {val_acc*100:.2f}%")


