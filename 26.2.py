print("Шахматная доска")
from PIL import Image, ImageDraw


def board(num, size, cell_colour='#000000'):
    image = Image.new('RGB', (num * size, num * size), '#FFFFFF')
    drawer = ImageDraw.Draw(image)

    for x in range(0, num, 2):
        for y in range(0, num):
            if y % 2 == 0:
                drawer.rectangle(((x * size, y * size),
                                  (x * size + size - 1, y * size + size - 1)), cell_colour)
            else:
                drawer.rectangle(((x * size + size, y * size),
                                  (x * size + size + size - 1, y * size + size - 1)), cell_colour)
    image.save('res_1.png', 'PNG')
    image.show()

board(8, 10)
input(" ")
input("Press any key to exit")
exit(0)