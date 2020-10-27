"""
All Coordinates 

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


Link for game: https://pataya.itch.io/heist
"""

import pyautogui as p
import time as t

while True:
    # if the coordinate matches the pixel it double clicks it
    if p.pixelMatchesColor(1144, 419, (208, 52, 78)):
        p.doubleClick(1144, 444)
    # clicks the bank 200 times in 0.01 interval fast
    p.click(827, 478, clicks=200, interval=0.01)
    p.click(408, 389)  # after the bank has been clicked 200 times it buys the cheapest one first and goes up to the highest price ones, this one here is the pickpocketer
    p.click(405, 461)  # Money earned per bag
    p.click(468, 388)  # mugger
    p.click(463, 462)  # decrease time spent in bank
    p.click(527, 390)  # mercenary
    p.click(524, 462)  # Increase speed on all henchmens
    p.click(589, 388)  # swindler
    p.click(584, 459)  # increase deployment rate
    p.click(645, 390)  # virtuoso
    p.click(646, 464)  # increase maximum capacity of bags
