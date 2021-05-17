print("Печать фрактала ")
def fractal_print(obj):
  print('[' + ', '.join(map(str, obj)) + ']')
fractal = [3]
fractal.append(fractal)
fractal_print(fractal)
print("_____________")
fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)

input("Press any key to exit")
exit(0)
