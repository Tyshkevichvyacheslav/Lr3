print("Месяц/Month")

def month_name(number, language):
    if language == "ru":
        if number == 1:
            print("Январь")
        elif number == 2:
            print("февраль")
        elif number == 3:
            print("Март")
        elif number == 4:
            print("Апрель")
        elif number == 5:
            print("май")
        elif number == 6:
            print("Июнь")
        elif number == 7:
            print("Июль")
        elif number == 8:
            print("август")
        elif number == 9:
            print("сентября")
        elif number == 10:
            print("Октябрь")
        elif number == 11:
            print("ноябрь")
        elif number == 12:
            print("Декабрь")
    elif language == "en":
        if number == 1:
            print("January")
        elif number == 2:
            print("february")
        elif number == 3:
            print("march")
        elif number == 4:
            print("April")
        elif number == 5:
            print("may")
        elif number == 6:
            print("june")
        elif number == 7:
            print("July")
        elif number == 8:
            print("August")
        elif number == 9:
            print("September")
        elif number == 10:
            print("Octobrt")
        elif number == 11:
            print("November")
        elif number ==  12:
            print("December")

if __name__ == '__main__':
    language=str(input("Choose language: ru/en"))
    while language != 'en' and language != 'ru':
        language = input("Choose language: ru/en")
    number = int(input("Укажите месяц/Choose mounth:"))
    while number>12:
        number = int(input("Укажите месяц/Choose mounth:"))
    month_name(number,language)
input("Press any key to exit")
exit(0)


