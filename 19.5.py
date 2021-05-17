print("19.5. Простые числа")
def prime(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 else 'Составное число'

if __name__ == '__main__':
    number = int(input("Введите число: "))

print(prime(number))
input("Press any key to exit")
exit(0)
