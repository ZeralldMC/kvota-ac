import ctypes
from msvcrt import getch
from operator import length_hint
from random import randint
import datetime
import time
import json
import requests
import eel
import psutil

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

processlist=list()

for process in psutil.process_iter():
    processlist.append(process.name())

processlist = list(dict.fromkeys(processlist))

print(processlist)



print("127GAMES KVOTA ANTI-CHEAT v1.001B")
print("Loading resources...")

def createLog(status):
    if status == 1:
        status_print = "Access denied"
    if status == 2:
        status_print = "Access allowed"
    with open("logs/" + str(randint(9999999, 99999999999)) + '_kvotaLog.txt', 'w') as f:
        f.write(
            '[LOG_' + str(datetime.datetime.now()) + "] " + str(status_print) +
            '\n[LOG_' + str(datetime.datetime.now()) + "] Scan: " + str(len(processlist)) + " programms scanned" + 
            '\n[LOG_' + str(datetime.datetime.now()) + "] Final result: " + str(len(cheatList)) + " out of " + str(len(processlist)) + " available programs seemed suspicious"
        )

    print(str(len(cheatList)) + " cheats detected")
    
    @eel.expose
    def getCheck():
        return status
    getCheck()

def deniedAccess():
    print("Access to run denied. Detecting other files...")

def allowAccess():
    print("All files successfuly verified. Enjoy")

url = 'https://127games.ml/kvota/api/allCheats.php'

response = requests.get(url)
jsonList = json.loads(response.text)

cheatProgramms = jsonList["cheatsDetect"]

cheatList = [processlist for processlist in processlist if processlist in cheatProgramms]

if [processlist for processlist in processlist if processlist in cheatProgramms]:
    createLog(1)
    deniedAccess()
else:
    allowAccess()
    createLog(2)



eel.init("web")

eel.start('/interface.html', size=(680, 310), port=8002)
