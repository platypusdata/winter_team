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

def ex1_func(inputs):
    x = inputs[0]
    return x**2

def ex2_func(inputs):
    x = inputs[0]
    return 3*x*(np.exp(x))


def ex3_func(inputs):
    x = inputs[0]
    y = inputs[1]
    return (2 * x + 3 * x * y + np.power(y, 3))


def q_func(inputs):
    w = inputs[0, 0]
    x = inputs[0, 1]
    y = inputs[1, 0]
    z = inputs[1, 1]

    return (w * x + x * y * z + 4 * w + 2 * z * np.power(y, 3))

inputs = np.array([[1.0, 2.0], [4.0, 8.0]])

result = num_derivative(q_func,inputs)

#inputs = np.array([1.0, 2.0])


print(result)

