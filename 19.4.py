print("Палиндромы")
def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'
print("_____________________________")
print(palindrome('12321'))
print(palindrome('Палиндром'))
input("Press any key to exit")
exit(0)
