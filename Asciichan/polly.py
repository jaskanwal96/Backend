import pyautogui

from time import sleep



while True:

        pyautogui.moveTo(100, 100, duration=0.5)

        sleep(2)

        pyautogui.moveTo(200, 100, duration=0.5)

        sleep(2)

        pyautogui.press('left')

        sleep(2)

        pyautogui.moveTo(100, 300, duration=0.5)

        sleep(2)

        pyautogui.moveTo(500, 400, duration=0.5)

        sleep(2)

        pyautogui.moveTo(800, 200, duration=0.5)

        sleep(2)

        pyautogui.press('right')

        sleep(2)

        pyautogui.moveTo(700, 100, duration=0.5)

        sleep(2)

        pyautogui.moveTo(700, 700, duration=0.5)

        sleep(20)
