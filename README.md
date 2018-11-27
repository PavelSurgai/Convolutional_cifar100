# Convolutional_cifar100
Предмет: системы отображения информации. Задание №2
Тема: Классификация изображений по ста категориям с помощью свёрточной нейронной сети.

Датасет cifar100.

Необходимое ПО:

-Python 3.

-Библиотека глубокого обучения Keras.

-Библиотеки TensorFlow или Theano (используются в качестве вычислительного бекенда для Keras).

-Подключение к интернету.

Обучение:

$ python3 train.py <batch_size> <num_epochs>

<batch_size> - размер батча;

<num_epochs> - количество эпох обучения;

Тестирование:

$ python3 test.py <path_to_model/model.h5>

<path_to_model> - путь к модели;

Логи обучения:

Необходимое ПО tensorboard;

tensorboard --logdir=</path/to/logs>

</path/to/logs> - путь к логам;

Просмотр: http://localhost:6006/
