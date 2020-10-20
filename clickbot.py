import pyautogui as p
import time as t

#p.mouseInfo()
#exit()

x, y = p.locateCenterOnScreen('bank.png')
#p.locateCenterOnScreen('glowingBank.png')

while True:
    p.click(x, y)


    
    
