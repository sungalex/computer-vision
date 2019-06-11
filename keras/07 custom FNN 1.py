import numpy as np
import matplotlib.pyplot as plt

# x_train = np.random.rand(1024, 1)
x_train = np.random.rand(1024)
# linear function 에 activation function 을 추가하기 위해 y 값의 변위로 -1 ~ 1 이내로 제한
y_train = x_train * 0.1 - 0.05

x_val = np.random.rand(32)
y_val = x_val * 0.1 - 0.05

x_test = np.array([[0.0], [0.2], [0.4], [0.6], [0.8], [1.0]])
y_test = x_test * 0.1 - 0.05


class FNN:

    def __init__(self, lr=0.01):
        self.lr = lr
        # initial weights
        self.w = 0.5
        self.b = 0.

    def f(self, x):
        return np.tanh(x)

    def f_deriv(self, x):
        return 1 - np.tanh(x) ** 2

    def calc_sum(self, w, b, input):
        return w * input + b

    def propagate_forward(self, x):
        s = self.calc_sum(self.w, self.b, x)
        o = self.f(s)
        return s, o

    def predict(self, x):
        # forward propagation
        s, o = self.propagate_forward(x)
        return o

    # train for one batch
    def train_on_batch(self, x, y):
        # batch forward propagation
        s, o = self.propagate_forward(x)

        # this will be summed over the batch
        grad_sum_w = 0
        grad_sum_b = 0
        batch_size = x.shape[0]

        # batch 안의 모든 샘플에 대해서 기울기 계산
        # 기울기 평균
        for i in range(batch_size):
            grad_b = self.f_deriv(s[i]) * 2 * (o[i]-y[i])
            grad_w = x[i] * grad_b
            grad_sum_b += grad_b
            grad_sum_w += grad_w

        grad_w = grad_sum_w / batch_size
        grad_b = grad_sum_b / batch_size

        # 기울기 업데이트
        self.w -= grad_w * self.lr
        self.b -= grad_b * self.lr

    def fit(self, x, y, batch_size, epochs, validation_data):
        errors = []    # validation loss after each epoch
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
