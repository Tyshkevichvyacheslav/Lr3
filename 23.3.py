print("Пам-парам парам-пам парам")

line = input("Введите строку ->  ").lower()
print("Было ->     "+line)
lines = line.split()

lst = [sum(x in 'уеыаоэяию' for x in lin)
       for lin in lines]

if len(set(lst)) == 1:
    res = "Парам пам-пам"
else:
    res = "Пам парам"

print("Стало ->     "+res)



input("Press any key to exit")
exit(0)