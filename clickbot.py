"""
Coordinates 

characters
pickpocket (408, 389)
mugger (468, 388)
mercenary (527, 390)
swindler (589, 388)
virtuoso (645, 390)

upgrades 
Money earned(405, 461)
decrease time spent on the bank for all chracters (463, 462)
Increase speed for all characters(524, 462)
Increase deployment rate (584, 459)
Increase max capacity of all characters bag for money(646, 464)
"""

import pyautogui as p
import time as t

# p.mouseInfo()
# exit()


p.locateCenterOnScreen('bank.png')
p.locateCenterOnScreen('Money.png')


while True:
    p.click(827, 478, clicks=100, interval=0.1)  # bank
    p.click(408, 389)  # pickpocket
    p.click(405, 461)  # Money earned
    p.click(468, 388)  # mugger
    p.click(463, 462)  # decrease time spent in bank
    p.click(527, 390)  # mercenary
    p.click(524, 462)  # Increase speed on all henchmens
    p.click(589, 388)  # swindler
    p.click(584, 459)  # increase deployment rate
    p.click(645, 390)  # virtuoso
    p.click(646, 464)  # maximum capacity of bags

    elif p.pixelMatchesColor(1144, 444, (209, 164, 170)):
        p.click(1144, 444)
