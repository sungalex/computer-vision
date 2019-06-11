# one neuron without activation (Feed-forward Neural Network)

# for one sample (x, y)
# s = wx + b
# e = (s-y)^2
# de/dw = ds/dw * de/ds = x * 2(s-y)
# de/db = ds/db * de/ds = 1 * 2(s-y)

# for batch samples
# (grad_w, grad_b) = average(de/dw, de/db) over samples in batch
# because loss function for the batch is the average of the loss of each sample

# update
# w -= grad_w * learning_rate
# b -= grad_b * learning_rate

import numpy as np
import matplotlib.pyplot as plt

x_train = np.random.rand(32,1)
y_train = x_train * 2 + 1

x_val = np.random.rand(32,1)
y_val = x_val * 2 + 1

x_test = np.array([[0.2], [0.4], [0.6], [0.8]])
y_test = x_test * 2 + 1


class FNN:

    def __init__(self, lr=0.01):
        self.lr = lr
        # initial weights
        self.w = 0.5
        self.b = 0.

    def calc_sum(self, w, b, x):
        return w * x + b

    def predict(self, x):
        # forward propagation
        return self.calc_sum(self.w, self.b, x)

    # train for one batch
    def train_on_batch(self, x, y):
        # batch forward propagation
        s = self.calc_sum(self.w, self.b, x)

        # this will be summed over the batch
        grad_sum_w = 0
        grad_sum_b = 0
        batch_size = x.shape[0]

        # batch 안의 모든 샘플에 대해서 기울기 계산
        # 기울기 평균
        for i in range(batch_size):
            grad_sum_w += 2 * x[i] * (s[i]-y[i])
            grad_sum_b += 2 * (s[i]-y[i])

        grad_w = grad_sum_w / batch_size
        grad_b = grad_sum_b / batch_size

        # 기울기 업데이트
        self.w -= grad_w * self.lr
        self.b -= grad_b * self.lr

    def fit(self, x, y, batch_size, epochs, validation_data):
        errors = []  # validation loss after each epoch
        for epoch in range(epochs):
            for i in range(0, x.shape[0], batch_size):
                self.train_on_batch(x[i:i+batch_size], y[i:i+batch_size])

            y_pred = self.predict(validation_data[0])
            error = np.mean(np.square(y_pred - validation_data[1]))
            errors.append(error)
            print("w, b, e =", self.w, self.b, error)
        return errors


fnn = FNN()
errors = fnn.fit(x_train, y_train, 32, 300, (x_val, y_val))
pred = fnn.predict(x_test)
print('pred:\n', pred)
print('y_test:\n', y_test)

plt.plot(errors)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
