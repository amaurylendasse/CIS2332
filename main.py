# Amaury Lendasse
import numpy as np
import matplotlib.pyplot as plt


# generating x and y
sizex = [int(1e3), 1]
x = np.random.uniform(-5, 5, sizex)
y = np.sin(np.random.uniform(0, 2, 1) *x) + np.sin(np.random.uniform(1, 3, 1) * x) + np.sin(np.random.uniform(1, 5, 1) * x)
noise = np.random.normal(0, 0.005, sizex)
y = y + noise

# normalization
m = np.mean(x)
s = np.std(x)
x = (x - m) / s

unitvector = np.ones((sizex[0], 1))
x = np.concatenate((x, unitvector), axis=1)
sizex[1] += 1



# generating w
sizew = 100
w = np.random.normal(0, 2, [sizex[1], sizew])

for i in range(0, sizew + 1, 5):
    # calculating H
    H = np.matmul(x, w[:, :i])
    H = np.tanh(H)
    H = np.concatenate((H, unitvector), axis=1)

    # solving system
    HH = np.matmul(np.transpose(H), H)
    HH = HH + np.identity(np.size(HH, 1)) * 0.0000001
    HY = np.matmul(np.transpose(H), y)
    A = np.linalg.solve(HH, HY)
    yh = np.matmul(H, A)

    # calculating MSE
    mse = ((y - yh) ** 2).mean(axis=0)
    print('MSE is', mse)

    # plotting
    # plt.plot(x[:,0], y, 'b.', x[:,0], yh, 'r.')
    plt.plot(x[:,0], y, 'b.')
    plt.plot(x[:,0], yh, 'r.')
    plt.ion()
    plt.show()
    plt.pause(.1)


