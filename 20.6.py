print("Делайте ваши ставки")
print("В соревнованиях учавствуют 10 лошадей ")


def do_bet(horse, bet):
    if bet == 0 or horse in horses or horse > 10 or horse <= 0:
        print('Что-то пошло не так, попробуйте еще раз')
        return
    else:
        print('Ваша ставка в размере', bet, 'на лошадь', horse, 'принята')
        horses.append(horse)
        return

horses = []

do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)


input("Press any key to exit")
exit(0)


comm = '''
def do_bet():
    horse = int(input("Введите  номер лошади: "))
    bet = int(input("Введите вашу ставку: "))
    c = 10
    while c != 0:
        if horse < 11 or bet!=0 or horse!=0 or horse!='' or  bet!='':
            print("Ваша ставка в размере " + str(bet) + " на лошадь " + str(horse) + " принята")
            horses.append(horse)
            c -= 1
            horse = int(input("Введите  номер лошади: "))
            if horse in horses:
                print("Что-то пошло не так, попробуйте еще раз")
                horse = int(input("Введите правильный номер лошади, на которую еще не делали ставки : "))
            bet = int(input("Введите вашу ставку: "))
            horses.append(horse)
            c -= 1
        if c == 0:
            print("Ставки закончились ")
        elif bet==0 or horse in horses or horse>11 or horse==' ' or bet==' '  :
            print("Что-то пошло не так, попробуйте еще раз")
            horse = int(input("Ваедите правильный номер лошади: "))
            bet = int(input("Повторите  вашу ставку: "))


horses = []
do_bet()
'''
