import numpy as np

def num_derivative(f, x):
    delta_x = 1e-4
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index

        tmp_val = x[idx]

        x[idx] = tmp_val + delta_x
        fx1 = f(x)  # f(x+delta_x)

        x[idx] = tmp_val - delta_x
        fx2 = f(x)  # f(x-delta_x)

        grad[idx] = (fx1 - fx2) / (2 * delta_x)
        x[idx] = tmp_val

        it.iternext()

    return grad


def loss_func(x, t):
    y = np.dot(x, W) + b

    return (np.sum((t - y) ** 2)) / (len(x))

def predict(x):
    y = np.dot(x, W) + b

    return y

x_data = np.array([9, 14, 21, 27, 32, 37]).reshape(6,1)
t_data = np.array([74, 81, 86, 90, 88, 92]).reshape(6,1)

W = np.random.rand(1,1)
b = np.random.rand(1)
print("W = ", W, ", W.shape = ", W.shape, ", b = ", b, ", b.shape = ", b.shape)

learning_rate = 1e-3

f = lambda x: loss_func(x_data, t_data)

print("Initial error value = ", loss_func(x_data, t_data), "Initial W = ", W, ", Initial b = ", b)

for step in range(10001):

    W = W - learning_rate * num_derivative(f, W)

    b = b - learning_rate * num_derivative(f, b)

    if (step % 500 == 0):
        print("step =", step, ", error value =", loss_func(x_data, t_data), ", W =", W, ", b =", b)

test_data = 30
result = predict(test_data)
print('공부를', test_data, '시간했을때 예상점수는', result, '점 입니다.')

