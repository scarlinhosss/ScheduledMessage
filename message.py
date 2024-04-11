import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write("messagetext.txt")
pyautogui.press('enter')
pyautogui.moveTo(979, 481)
pyautogui.click(button='right')
pyautogui.moveTo(1027, 610)
pyautogui.click()
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'f4')
pyautogui.press('win')
pyautogui.write("Firefox")
pyautogui.press('enter')
time.sleep(5)
pyautogui.write("web.whatsapp.com")
pyautogui.press('enter')
time.sleep(8)
pyautogui.click(381, 292)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter') 