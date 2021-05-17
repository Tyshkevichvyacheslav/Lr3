print("Точка на прямой")
def line(s, t):
    x = float(t[:t.index(';')])
    y = float(t[t.index(';') + 1:])
    k = float(s[:s.index('x')])
    b = float(s[s.index('x') + 1:])
    print((k * x + b) == y)

line("1x+6", "1;7")
line("5x-10", "5;-9")
line("0x+7", "3;7")
line("3.5x+0", "2;7")
input("Press any key to exit")
exit(0)
