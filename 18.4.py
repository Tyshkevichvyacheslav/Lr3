print("Правильная скобочная последовательность")
def Bracket_check(n):
    sp = []
    flag = False
    for i in range(len(n)):
        if n[i] == '(':
            sp.append(n[i])
        elif n[i] == ')' and len(sp) == 0:
            flag = True
            break
        elif n[i] == ')' and sp[-1] == '(':
            del sp[-1]
    if len(sp) == 0 and not flag:
        print('YES')
    else:
        print('NO')

Bracket_check(input("Введите последовательность : "))