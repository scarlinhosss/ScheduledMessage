import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write("messagetext.txt")
pyautogui.press('enter')
pyautogui.moveTo(943, 333)
pyautogui.click()
pyautogui.click(button='right')
pyautogui.moveTo(1006, 478)
pyautogui.click()
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'f4')
pyautogui.press('win')
pyautogui.write("Firefox")
pyautogui.press('enter')
time.sleep(10)
pyautogui.write("web.whatsapp.com")
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(348, 272)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter') 
