print("Фрактальный список – 2")
def defractalize(fractal):
    return [x for x in fractal if x is not fractal]

fractal = [2, 5]
fractal.append(3)
fractal.append(9)
print(fractal)

print("____________")

fractal = [2, 5]
fractal.append(3)
print(fractal)


input("Press any key to exit")
exit(0)
