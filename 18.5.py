print("Уравнение прямой")
def equation(a, b):
    xa = float(a[:a.find(';')])
    ya = float(a[a.find(';') + 1:])
    xb = float(b[:b.find(';')])
    yb = float(b[b.find(';') + 1:])
    if xa == xb:
        print(a[:a.find(';')])
    elif ya == yb:
        print(a[a.find(';') + 1:])
    else:
        k = (ya - yb) / (xa - xb)
        b = yb - k * xb
        print(k, b)

equation("0;0", "1;1")
equation("0;0", "0;4")
equation("4;6.9", "-5.2;6.9")
