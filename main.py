from time import sleep
from PIL import ImageGrab
import pyautogui


X = 270


def capture_screen():
    image = ImageGrab.grab()
    return image


def detect_enemy(screen):
    first_color = screen.getpixel((160, 400))
    for x in range(155, int(X)):
        for y in range(400, 480):
            color = screen.getpixel((x, y))
            if color != first_color:
                return True
            else:
                first_color = color


def jump():
    global X
    pyautogui.press('up')
    if X < 400:
        X += 2
    elif 400 <= X < 500:
        X += 2.75
    elif 500 < X:
        X += 3


print('Starting in 3 seconds...')
sleep(3)

while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()
