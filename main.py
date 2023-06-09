import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

pyautogui.press('win')
pyautogui.write('calculadora')
pyautogui.press('enter')
pyautogui.click(x=568, y=764)
pyautogui.click(x=1270, y=766)
pyautogui.click(x=650, y=888)
pyautogui.click(x=1300, y=968)

# time.sleep(5)
# print(pyautogui.position())




