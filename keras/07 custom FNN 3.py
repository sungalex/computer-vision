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
    
    def add(self, units, activation=None, activation_deriv=None):
        input_dim = self.w[-1].shape[1] if self.n_layers > 0 else 1
        self.w.append(np.random.rand(input_dim, units) * 2 - 1)     # -1 ~ 1 random
        self.b.append(np.zeros(units))    # 0으로 초기화
        self.f.append(activation)    # activation function
        self.f_deriv.append(activation_deriv)    # derivatives
        self.n_layers += 1
    
    def calc_sum(self, w, b, input):
        return input * w + b
    
    def propagate_forward(self, x):
        s = [x]
        o = [x]
        for l in range(1, self.n_layers):
            s.append(np.matmul(o[l-1], self.w[l]) + self.b[l])
            o.append(self.f[l](s[l]))
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

            delta = [np.zeros(1)] * self.n_layers
            delta[l_last] = self.f_deriv[l_last](s[l_last]) * 2 * (o[l_last]-y) / y.shape[-1]

            for l in range(l_last - 1, 0, -1):   # 역순으로 미분값 계산
                delta[l] = self.f_deriv[l](s[l]) * np.matmul(self.w[l+1], delta[l+1])

            for l in range(1, self.n_layers):
                dedw = np.zeros(self.w[l].shape, np.float32)
                for i in range(dedw.shape[0]):
                    for j in range(dedw.shape[1]):
                        dedw[i,j] = o[l-1][i] * delta[l][j]
                dedb = delta[l]
                grad_sum_w[l] += dedw
                grad_sum_b[l] += dedb

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
            # print('w: {}, b: {}'.format(self.w[1:], self.b[1:]))
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


x_train = np.random.rand(1024, 2)
y_train = np.array([[x[0]+x[1],x[0]-x[1]] for x in x_train]) * 0.1

x_val = np.random.rand(32, 2)
y_val = np.array([[x[0]+x[1],x[0]-x[1]] for x in x_val]) * 0.1

x_test = np.array([[0.2, 0.1], [0.3, 0.1], [0.4, 0.1], [0.5, 0.1]])
y_test = np.array([[x[0]+x[1],x[0]-x[1]] for x in x_test]) * 0.1

fnn = FNN(0.1)
fnn.add(2)   # input layer
fnn.add(3, linear, linear_deriv)    # hidden layer
fnn.add(3, sigmoid, sigmoid_deriv)   # hidden layer
fnn.add(2, tanh, tanh_deriv)    # output layer

errors = fnn.fit(x_train, y_train, 32, 1000, (x_val, y_val))

# s, o = fnn.propagate_forward(x_test)
# print("s:")
# for i in range(len(s)): print(s[i])
# print("o:")
# for i in range(len(o)): print(o[i])

y_pred = fnn.predict(x_test)
print('y_pred:\n', y_pred)
print('y_test:\n', y_test)

plt.plot(errors[25:])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
