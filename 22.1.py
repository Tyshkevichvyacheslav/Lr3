print("Цезарь")
llst = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
blst = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encrypt_caesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x) % len(llst)
            ret += llst[(ind + shift) % len(llst)]
        elif x in blst:
            ind = blst.index(x) % len(llst)
            ret += blst[(ind + shift) % len(llst)]
        else:
            ret += x
    return ret


def decrypt_caesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind - shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind - shift]
        else:
            ret += x
    return ret


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
print("____________")
msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)


input("Press any key to exit")
exit(0)
