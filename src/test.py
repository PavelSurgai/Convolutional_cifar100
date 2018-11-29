import numpy
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Dropout
from keras.layers.convolutional import Conv2D
from keras.utils import np_utils
from keras.optimizers import SGD
import sys
from keras.models import load_model

# Оцениваем качество обучения модели на тестовых данных


# Загружаем данные
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# Количество классов изображений
nb_classes = 100
batch_size = 32

model = load_model(sys.argv[1],custom_objects=None,compile=True)


# Задаем параметры оптимизации
sgd = SGD(lr=0.01)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(X_test, y_test,
              batch_size=batch_size,
              epochs=1,
              validation_split=0.1)

scores = model.evaluate(X_test, y_test)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))
