import numpy as np

class UGANDataset(object):
    def __init__(self, batch_size, noise_size):
        self._generator_y = np.ones((batch_size, 1), dtype=np.float32)
        self._discriminator_y = np.concatenate([np.ones((batch_size, 1), dtype=np.float32),
                                          np.zeros((batch_size, 1), dtype=np.float32)])
        self._batch_size = batch_size
        self._noise_size = noise_size
        self._batches_before_shuffle = 1000
        self._current_batch = 0
        
    def next_generator_sample(self):
        return np.random.rand(self._batch_size, self._noise_size), self._generator_y
    
    def _load_discriminator_data(self, index):
        None
    
    def _shuffle_discriminator_data(self):
        None

    def next_discriminator_sample(self, generated_data):
        self._current_batch %= self._batches_before_shuffle
        if self._current_batch == 0:
            self._shuffle_discriminator_data()
        index = np.arange(self._current_batch * self._batch_size, (self._current_batch + 1) * self._batch_size)
        self._current_batch += 1
        image_batch = np.concatenate([self._load_discriminator_data(index), generated_data], axis = 0)
        return image_batch, self._discriminator_y
        

    def display(self, batch, row=8, col=8):
        width, height = batch.shape[1], batch.shape[2]
        total_width, total_height = width * col, height * row
        result_image = np.empty((total_height, total_width, batch.shape[3]))
        batch_index = 0
        for i in range(row):
            for j in range(col):
                result_image[(i * height):((i+1)*height), (j * width):((j+1)*width)] = batch[batch_index]
                batch_index += 1
        return result_image

    
class ArrayDataset(UGANDataset):
    def __init__(self, X, batch_size, noise_size):
        super(ArrayDataset, self).__init__(batch_size, noise_size)
        self._X = X
        self._batches_before_shuffle = int(X.shape[0] // self._batch_size)
    
    def _load_discriminator_data(self, index):
        return self._X[index]
    
    def _shuffle_discriminator_data(self):
        np.random.shuffle(self._X)
    
class MNISTDataset(ArrayDataset):
    def __init__(self, batch_size, noise_size = 100):
        from keras.datasets import mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X = np.concatenate((X_train, X_test), axis=0)
        X = X.reshape((X.shape[0], X.shape[1], X.shape[2], 1))
        X = (X.astype(np.float32) - 127.5) / 127.5
        super(MNISTDataset, self).__init__(X, batch_size, noise_size)
        
    def display(self, batch, row=8, col=8):
        image = super(MNISTDataset, self).display(batch, row, col)
        image = (image * 127.5) + 127.5
        image = np.squeeze(np.round(image).astype(np.uint8))
        return image