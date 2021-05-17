print("Все равны, как на подбор ")
def same_by(characteristic, objects):
  return len(set(map(characteristic, objects))) < 2

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

input("Press any key to exit")
exit(0)