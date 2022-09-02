import pyautogui
import time
time.sleep(0.3)
pyautogui.hotkey('win','r')
time.sleep(0.3)
pyautogui.typewrite("Powershell echo hello world;Read-Host", interval=0.01)
time.sleep(0.3)
pyautogui.hotkey('enter')
