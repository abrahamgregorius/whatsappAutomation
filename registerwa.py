import os
import helper
from time import sleep

device_id = "R9CT4007GBM"
phone_num = "87815494888"

def chooseLanguage():
    os.system(f'adb -s ' + device_id + ' shell input tap 525 1023')
    os.system(f'adb -s ' + device_id + ' shell input tap 955 2155')

def frontPageLanguage():
    chooseLanguage()
    os.system(f'adb -s ' + device_id + ' shell input tap 650 1660')
    os.system(f'adb -s ' + device_id + ' shell input tap 515 600')
    for i in phone_num:
        helper.pressKey(i)
    os.system(f'adb -s ' + device_id + ' shell input tap 530 1250')

def frontPage():
    os.system(f'adb -s ' + device_id + ' shell input tap 515 2060')
    os.system(f'adb -s ' + device_id + ' shell input tap 515 600')
    for i in phone_num:
        helper.pressKey(i)
    os.system(f'adb -s ' + device_id + ' shell input tap 530 1250')
    os.system(f'adb -s ' + device_id + ' shell input tap 885 1385')

def contactMediaPerm():
    os.system(f'adb -s ' + device_id + ' shell input tap 755 1585')

def filePerm():
    os.system(f'adb -s ' + device_id + ' shell input tap 535 1980')
    os.system(f'adb -s ' + device_id + ' shell input tap 535 1980')

def drivePerm():
    os.system(f'adb -s ' + device_id + ' shell input tap 830 1360')
    os.system(f'adb -s ' + device_id + ' shell input tap 515 1110')
    sleep(3)
    os.system(f'adb -s ' + device_id + ' shell input tap 700 2110')
    sleep(3)
    os.system(f'adb -s ' + device_id + ' shell input tap 840 1350')
    
    
def profileSetup(name):
    os.system(f'adb -s ' + device_id + ' shell input tap 530 900')
    nama = [*name.upper()]
    for i in nama:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s ' + device_id + ' shell input tap 525 1300')


frontPage()
sleep(5)
contactMediaPerm()
sleep(5)
drivePerm()
sleep(5)
filePerm()
sleep(5)
drivePerm()
sleep(5)
profileSetup('Justin Timberlake')