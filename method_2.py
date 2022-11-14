import numpy as np
from matplotlib import pyplot as plt
from sympy import *

xy = np.array([(3, 5)])
ep = 0.000001

step = [0.01]  # for SDM
rad = []  # Temporary args
all_s = np.array([0])  # for fr
all_grads = np.array([(1, 1)])  # for fr


def Func(x, y):
    return x ** 2 - x * y + y ** 2 - 2 * x + y


def grad():
    x, y = xy[-1]
    a, b = symbols('x y')
    func = Func(a, b)
    return [eval(i, {"x": x, "y": y}) for i in [str(diff(func, a)), str(diff(func, b))]]


def gessian():
    x, y = xy[-1]
    a, b = symbols('x y')
    func = Func(a, b)
    return [[eval(str(diff(i, a)), {"x": x, "y": y}), eval(str(diff(i, b)), {"x": x, "y": y})] for i in
            [str(diff(func, a)), str(diff(func, b))]]


def fr():
    global xy, all_s, all_grads
    gr = np.array(grad())
    w = (gr[0] ** 2 + gr[1] ** 2) / (all_grads[-1][0] ** 2 + all_grads[-1][1] ** 2)
    s = -gr + w * all_s[-1]
    gs = np.array(gessian()).T
    lm = -(-s @ s.T / (s @ gs @ s.T))
    new_xy = xy[-1].T + lm * s.T
    all_grads = np.append(all_grads, [grad()], axis=0)
    all_s = np.append(all_s, s, axis=0)
    xy = np.append(xy, [new_xy], axis=0)

    # print(xy)
    print("Function:",Func(xy[-1][0], xy[-1][1]))


iter = 0
while abs(Func(xy[-1][0], xy[-1][1]) + 1) > ep:
    iter += 1
    print(f"Iteration of SDM #{iter};")
    fr()

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
