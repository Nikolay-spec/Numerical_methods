from sympy import *
import numpy as np
import matplotlib.pyplot as plt

xy = np.array([(3, 5)])
ep = 0.000001

step = [0.01]  # for SDM3c
rad = []  # Temporary args


def Func(x, y):
    return x ** 2 - x * y + y ** 2 - 2 * x + y


def grad():
    x, y = xy[-1]
    a, b = symbols('x y')
    func = 'x ** 2 - x * y + y ** 2 - 2 * x + y'
    return [eval(i, {"x": x, "y": y}) for i in [str(diff(func, a)), str(diff(func, b))]]


def SDM(step):
    global xy
    new_xy = [xy[-1] - step[0] * np.array(grad())]
    xy = np.append(xy, new_xy, axis=0)
    if Func(xy[-1][0], xy[-1][1]) - Func(xy[-2][0], xy[-2][1]) < 0:
        step[0] *= 1.618
    else:
        step[0] /= 1.618
    # print(xy)
    print("Function:",Func(xy[-1][0], xy[-1][1]))
    # print(xy[-2][0], xy[-2][1], xy[-1][0], xy[-1][1])


iter = 0
while abs(Func(xy[-1][0], xy[-1][1]) + 1) > ep:
    iter += 1
    print(f"Iteration of SDM #{iter};")
    SDM(step)


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = Func(X, Y)
# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3)
f = np.array([Func(xy[i][0], xy[i][1]) for i in range(len(xy))])
x = np.array([xy[i][0] for i in range(len(xy))])
y = np.array([xy[i][1] for i in range(len(xy))])
ax.plot(x, y, f, color='red', alpha=0.5)
ax.scatter(x, y, f, c='blue')

plt.show()
