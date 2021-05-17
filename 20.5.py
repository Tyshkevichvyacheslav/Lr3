print("Счастливый пассажир")

def happy(s):
    if sum([int(char) for char in s[:3]]) == sum([int(char) for char in s[-3:]]):
        print("Счастливый")
    else:
        print("Несчастливый")

if __name__ == '__main__':
    s = input("Введите номмер билета: ")
    happy(s)

input("Press any key to exit")
exit(0)
