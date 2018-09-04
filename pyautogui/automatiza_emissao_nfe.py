import pyautogui
import time


#pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
PRINT_BUTTON = pyautogui.locateOnScreen('print.png')


def center_click(location):
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)
    print('Click ({}, {})'.format(x, y))
    return True


def to_authorize():
    is_to_authorize = pyautogui.locateOnScreen('nao_autorizada.png',
                                               grayscale=False)
    if not is_to_authorize:
        is_to_authorize = pyautogui.locateOnScreen('rejeitada.png',
                                                   grayscale=False)

    print('Não Autorizado: ', is_to_authorize)
    return is_to_authorize


def next_click():
    button_next = pyautogui.locateOnScreen('next.png')
    print('Next: ', button_next)
    if button_next:
        return center_click(button_next)


start = time.time()
while True:
    pyautogui.moveRel(None, 100)  # move mouse 100 pixels down

    if to_authorize():
        print('print_button:', PRINT_BUTTON)
        center_click(PRINT_BUTTON)

    if not next_click():
        break

print('Concluído em: ', time.time() - start)
