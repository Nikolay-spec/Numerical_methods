import sys, os

xy = [3, 5]
oxy = xy[:]
s = [1, 0]
a = float(input("Print parameter for Svenn step:"))
rad = []



def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def Function(x, y):
    func = x**2 - x*y + y**2 - 2*x + y
    return func

def svenn_alpha(xy,s):
    delta = a * abs(((xy[0] ** 2 + xy[1] ** 2) ** 0.5) / (s[0] ** 2 + s[1] ** 2) ** 0.5)
    return delta

def svenn(xy,s):
    print("----------SVENN---START----------")
    delta = svenn_alpha(xy,s)
    k = 0
    tn = 0
    print(f"tn = {tn}")
    print(f"f({k}) = {Function(xy[0],xy[1])}")
    if Function(xy[0] - delta*s[0],xy[1] - delta*s[1]) >= Function(xy[0] + delta*s[0],xy[1] + delta*s[1]):
        while True:
            tn = tn + delta * (2 ** k)
            print("---------------------------------------------------------------------------------------------")
            print(f"tn = {tn}")
            print(f"f({k + 1}) = {Function(xy[0] + tn*s[0],xy[1] + tn*s[1])}")
            if Function(xy[0] + tn*s[0], xy[1] + tn*s[1]) < Function(xy[0] + (tn + delta * (2 ** (k + 1)))*s[0], xy[1] + (tn + delta * (2 ** (k + 1)))*s[1]):
                tt1 = tn
                k += 1
                tn = tn + delta * (2 ** k)
                print("---------------------------------------------------------------------------------------------")
                print(f"tn = {tn}")
                print(f"f({k + 1}) = {Function(xy[0] + tn*s[0],xy[1] + tn*s[1])}")
                print("---------------------------------------------------------------------------------------------")
                print(f"tn = {(tn + tt1) / 2}")
                print(f"f({k + 2}) = {Function(xy[0] + ( (tn + tt1) / 2)*s[0],xy[1] + ( (tn + tt1) / 2)*s[1])}")
                if Function(xy[0] + ((tn + tt1) / 2)*s[0], xy[1] + ((tn + tt1) / 2)*s[1]) < Function(xy[0] + tt1*s[0], xy[1] + tt1*s[1]):
                    rad.append(tt1)
                    rad.append((tn + tt1) / 2)
                    rad.append(tn)
                else:
                    rad.append(tt1 - delta * (2 ** (k - 1)))
                    rad.append(tt1)
                    rad.append((tn + tt1) / 2)
                break
            k += 1
    else:
        while True:
            tn = tn - delta * (2 ** k)
            print("---------------------------------------------------------------------------------------------")
            print(f"tn = {tn}")
            print(f"f({k + 1}) = {Function(xy[0] + tn*s[0],xy[1] + tn*s[1])}")
            if Function(xy[0] + tn*s[0],xy[1] + tn*s[1]) < Function(xy[0] + (tn - delta * (2 ** (k + 1)))*s[0],xy[1] + (tn - delta * (2 ** (k + 1)))*s[1]):
                tt1 = tn
                k += 1
                tn = tn - delta * (2 ** k)
                print("---------------------------------------------------------------------------------------------")
                print(f"tn = {tn}")
                print(f"f({k + 1}) = {Function(xy[0] + tn*s[0],xy[1] + tn*s[1])}")
                print("---------------------------------------------------------------------------------------------")
                print(f"tn = {(tn + tt1) / 2}")
                print(f"f({k + 2}) = {Function(xy[0] + ( (tn + tt1) / 2)*s[0],xy[1] + ( (tn + tt1) / 2)*s[1])}")
                if Function(xy[0] + ((tn + tt1) / 2)*s[0], xy[1] + ((tn + tt1) / 2)*s[1]) < Function(xy[0] + tt1*s[0], xy[1] + tt1*s[1]):
                    rad.append(tt1)
                    rad.append((tn + tt1) / 2)
                    rad.append(tn)
                else:
                    rad.append(tt1 + delta * (2 ** (k - 1)))
                    rad.append(tt1)
                    rad.append((tn + tt1) / 2)
                break
            k += 1
    print("----------SVENN---END----------")

def golden_ratio(xy,s):
    print("----------GOLDEN---RATIO---START----------")
    print(f"xy[1]={xy[1]}")
    i = 0
    ep = 0.00001
    t1 = rad[0] + 0.382 * (rad[2] - rad[0])
    t2 = rad[0] + 0.618 * (rad[2] - rad[0])
    while abs(rad[2] - rad[0]) > ep:
        if Function(xy[0] + t1*s[0],xy[1] + t1*s[1]) > Function(xy[0] + t2*s[0],xy[1] + t2*s[1]):
            rad[0] = t1
            t1 = t2
            radtemp = rad[0]
            L = (rad[2] - radtemp)
            t2 = radtemp + 0.618 * L
            print("_____________________________________________________________________")
            print(f"a={rad[0]};b={rad[2]};")
            print(f"l1={t1}")
            print(f"l2={t2}")
            print(f"f({i + 1})={Function(xy[0] + t1*s[0],xy[1] + t1*s[1])}")
            print(f"f({i + 1})={Function(xy[0] + t2*s[0],xy[1] + t2*s[1])}")
            print(0)
        else:  # Function(xy[0] + t1*s[0],xy[1] + t1*s[1]) < Function(xy[0] + t2*s[0],xy[1] + t2*s[1])
            rad[2] = t2
            L = (rad[2] - rad[0])
            t2 = t1
            t1 = rad[0] + 0.382 * L
            print("_____________________________________________________________________")
            print(f"a={rad[0]};b={rad[2]};")
            print(f"l1={t1}")
            print(f"l2={t2}")
            print(f"f({i + 1})={Function(xy[0] + t1*s[0],xy[1] + t1*s[1])}")
            print(f"f({i + 1})={Function(xy[0] + t2*s[0],xy[1] + t2*s[1])}")
            print(1)
        i += 1
    rad.append(rad[0])
    rad.append((rad[0]+rad[2])/2)
    rad.append(rad[2])
    print("----------GOLDEN---RATIO---END----------")
    return (rad[0]+rad[2])/2

def DSK_Powell(xy,s):
    ep = 0.2
    delta = svenn_alpha(xy,s)
    l = rad[1] + ((delta * (Function(xy[0] + rad[0]*s[0],xy[1] + rad[0]*s[1]) - Function(xy[0] + rad[2]*s[0],xy[1] + rad[2]*s[1]))) / (
            2 * (Function(xy[0] + rad[0]*s[0],xy[1] + rad[0]*s[1]) - 2 * Function(xy[0] + rad[1]*s[0],xy[1] + rad[1]*s[1]) + Function(xy[0] + rad[2]*s[0],xy[1] + rad[2]*s[1]))))
    print(f"t={l}")
    print(f"f={Function(xy[0] + l*s[0],xy[1] + l*s[1])}")
    if Function(xy[0] + rad[1]*s[0],xy[1] + rad[1]*s[1]) - Function(xy[0] + l*s[0],xy[1] + l*s[1]) <= ep:
        if (rad[1] - l) <= ep:
            print("done")
            print(rad[1] - l)
            print(Function(xy[0] + rad[1]*s[0],xy[1] + rad[1]*s[1]) - Function(xy[0] + l*s[0],xy[1] + l*s[1]))
            print(f"Lambda = {(rad[1] + l) / 2}")
            print(f"f(l) = {Function(xy[0] + ((rad[1] + l) / 2)*s[0],xy[1] + ((rad[1] + l) / 2)*s[1])}")
            return (rad[1] + l) / 2
    if l < rad[1]:
        if Function(xy[0] + l*s[0],xy[1] + l*s[1]) < Function(xy[0] + rad[1]*s[0],xy[1] + rad[1]*s[1]):
            t1 = rad[0]
            t2 = l
            t3 = rad[1]
        else:
            t1 = l
            t2 = rad[1]
            t3 = rad[2]
    else:
        if Function(xy[0] + l*s[0],xy[1] + l*s[1]) < Function(xy[0] + rad[1]*s[0],xy[1] + rad[1]*s[1]):
            t1 = rad[1]
            t2 = l
            t3 = rad[2]
        else:
            t1 = rad[0]
            t2 = rad[1]
            t3 = l

    a1 = (Function(xy[0] + t2*s[0],xy[1] + t2*s[1]) - Function(xy[0] + t1*s[0],xy[1] + t1*s[1])) / (t2 - t1)
    a2 = (1 / (t3 - t2)) * (((Function(xy[0] + t3*s[0],xy[1] + t3*s[1]) - Function(xy[0] + t1*s[0],xy[1] + t1*s[1])) / (t3 - t1)) - a1)
    nl = (t1 + t2) / 2 - (a1 / 2 * a2)
    print(nl)

def Rozen_Step(xy):
    iter=0
    while abs(Function(xy[0],xy[1] + 1)) > 0.000001:
        blockPrint()
        for i in range(0,2):
            svenn(xy, s)
            # nxy = [coord + DSK_Powell(xy,s)*s[xy.index(coord)] for coord in xy]
            nxy = [coord + golden_ratio(xy, s) * s[xy.index(coord)] for coord in xy]
            xy[:] = nxy
            s[:] = [-s[1],s[0]]
            rad.clear()
        vector = [x - y for x, y in zip(oxy, xy)]
        s[:] = [v / ((vector[0] ** 2 + vector[1] ** 2) ** 0.5) for v in vector]
        enablePrint()
        print(f"Iteration:{iter+1}_______________________________________________________________________________")
        print(xy)
        print(Function(xy[0],xy[1]))
        iter+=1


# svenn(xy,s)
# DSK_Powell(xy,s)
Rozen_Step(xy)



