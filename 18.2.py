print("Скажи «пароль» и проходи")
def ask_password():
    a = input("Введите пароль: ")
    count = 0
    while count < 2:
        if a =='password':
            print("Пароль принят")
            exit(0)
        else:
            count += 1
        input("Пароль не принят, повторите : ")
        if count == 2:
            print("В доступе отказано")
            input("Press any button to exit")
            exit(0)
print(ask_password())