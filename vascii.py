from cv2 import COLOR_RGB2GRAY
from cv2 import VideoCapture
from cv2 import cvtColor
from cv2 import flip
from numpy import sum as npsum
from os import system, name

def clear():
    if name in ('nt','dos'):
        system("cls")
    elif name in ('linux','osx','posix'):
        system("clear")
    else:
        print("\n") * 150


def makeAscii(img, img_size, pixel_size):
    ASCII_CHARS = ['@', '#', '%', '$', 'S', '?', '*', ';', ':', ',', '.']
    ascii_img_size = img_size // pixel_size
    ascii_img = [['.' for j in range(ascii_img_size)]
                for i in range(ascii_img_size)]

    for y in range(0, img_size, pixel_size):
        for x in range(0, img_size, pixel_size):
            piece = img[y: y + pixel_size, x: x + pixel_size]
            symbol_index = int(npsum(piece) / (pixel_size **
                               2) / (255 / len(ASCII_CHARS)))
            try:
                symbol = ASCII_CHARS[symbol_index]
                ascii_img[y // pixel_size][x // pixel_size] = symbol
            except IndexError:
                pass

    return ascii_img

pixel_size = int(input('Enter the size of pixel: '))

is_update_display = False
if (input('Enable console clear [y/n] ? ') == 'y'):
    is_update_display = True
else:
    is_update_display = False

print('Please wait...')
cap = VideoCapture(0)

while True:
    _, img = cap.read()
    h, _, _ = img.shape
    gray_img = cvtColor(img, COLOR_RGB2GRAY)
    gray_img = flip(gray_img,1)
    output = makeAscii(gray_img, h, pixel_size)
    output = [''.join(output[i]) for i in range(h // pixel_size)]
    output = '\n'.join(output)
    if (is_update_display):
        clear()
    else:
        print('\n' * 150)
    print(output)

cap.release()