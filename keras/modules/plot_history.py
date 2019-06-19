import matplotlib.pyplot as plt


def plot_loss(history, title=None):
    if not isinstance(history, dict):
        history = history.history

    if title is not None:
        plt.title(title)
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc=0)
    plt.show()


def plot_acc(history, title):
    if not isinstance(history, dict):
        history = history.history

    if title is not None:
        plt.title(title)
    plt.plot(history['acc'])
    plt.plot(history['val_acc'])
    plt.ylabel('Accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc=0)
    plt.show()