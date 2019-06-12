import numpy as np
import matplotlib.pyplot as plt


class FNN:

    def __init__(self, lr=0.01):
        self.lr = lr     # learning rate
        self.w = []
        self.b = []
        self.f = []    # layer별 activation functions
        self.f_deriv = []    # derivatives (도함수)
        self.n_layers = 0
    
    def add(self, activation=None, activation_deriv=None):
        self.w.append(np.random.rand(1) * 2 - 1)     # -1 ~ 1 random
        self.b.append(0.)    # 0으로 초기화
        self.f.append(activation)    # activation function
        self.f_deriv.append(activation_deriv)    # derivatives
        self.n_layers += 1
    
    def calc_sum(self, w, b, input):
        return input * w + b
    
    def propagate_forward(self, x):
        s = [x]
        o = [x]
        for n in range(1, self.n_layers):
            s.append(self.calc_sum(self.w[n], self.b[n], o[n-1]))
            o.append(self.f[n](s[n]))
        return s, o
    
    def predict(self, x):
        s, o = self.propagate_forward(x)
        return o[-1]
        
    def train_on_batch(self, x_batch, y_batch):
        l_last = self.n_layers - 1

        # batch forward propagation
        s_batch, o_batch = self.propagate_forward(x_batch)

        grad_sum_w = [0.] * self.n_layers
        grad_sum_b = [0.] * self.n_layers

        # this will be summed over the batch
        batch_size = x_batch.shape[0]

        # batch 안의 모든 샘플에 대해서 기울기 계산
        for n in range(batch_size):
            # get n-th sample
            s = []; o = []; y = y_batch[n]
            for l in range(self.n_layers):
                s.append(s_batch[l][n])
                o.append(o_batch[l][n])

            # de/do[l_last] = 2 * (o[l_last]-y)
            # delta[l_lsat] = f'[l_last](s[l_last]) * de/do[l_last]
            # delta[l] = f'[l](s[l]) * w[l+1] * delta[l+1]
            delta = [0.] * self.n_layers
            delta[l_last] = self.f_deriv[l_last](s[l_last]) * 2 * (o[l_last]-y)

            for l in range(l_last - 1, 0, -1):   # 역순으로 미분값 계산
                delta[l] = self.f_deriv[l](s[l]) * self.w[l+1] * delta[l+1]

            for l in range(1, self.n_layers):
                grad_sum_w[l] += o[l-1] * delta[l]
                grad_sum_b[l] += delta[l]

        # 기울기 업데이트
        for l in range(1, self.n_layers):
            self.w[l] -= grad_sum_w[l]/batch_size * self.lr
            self.b[l] -= grad_sum_b[l]/batch_size * self.lr
    
    def fit(self, x, y, batch_size, epochs, validation_data):
        errors = []    # validation loss after each epoch
        for epoch in range(epochs):
            for i in range(0, x.shape[0], batch_size):
                self.train_on_batch(x[i:i+batch_size], y[i:i+batch_size])

            y_pred = self.predict(validation_data[0])
            error = np.mean(np.square(y_pred - validation_data[1]))
            errors.append(error)
            print('{0} epoch, error: {1}'.format(epoch, error))
            print('w: {}, b: {}'.format(self.w[1:], self.b[1:]))
        return errors


def linear(x):  # linear y = x
    return x

def linear_deriv(x):
    return 1

def sigmoid(x):
    return 1. / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1 - np.tanh(x) ** 2


# x_train = np.random.rand(1024, 1)
x_train = np.random.rand(1024)
# linear function 에 activation function 을 추가하기 위해 y 값의 변위로 -1 ~ 1 이내로 제한
y_train = x_train * 0.1 - 0.05

x_val = np.random.rand(32)
y_val = x_val * 0.1 - 0.05

x_test = np.array([[0.0], [0.2], [0.4], [0.6], [0.8], [1.0]])
y_test = x_test * 0.1 - 0.05

fnn = FNN(0.1)
fnn.add()   # input layer
fnn.add(linear, linear_deriv)    # hidden layer
fnn.add(sigmoid, sigmoid_deriv)   # hidden layer
fnn.add(tanh, tanh_deriv)    # output layer

errors = fnn.fit(x_train, y_train, 32, 1000, (x_val, y_val))

s, o = fnn.propagate_forward(x_test)
print("s:")
for i in range(len(s)): print(s[i])
print("o:")
for i in range(len(o)): print(o[i])

y_pred = fnn.predict(x_test)
print('y_pred:\n', y_pred)
print('y_test:\n', y_test)

plt.plot(errors)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
