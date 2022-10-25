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
    # Selamat datang di whatsapp
    os.system(f'adb -s ' + device_id + ' shell input tap 515 2060')
    # Klik nomor telponnya
    os.system(f'adb -s ' + device_id + ' shell input tap 515 600')
    # Masukkan nomor telepon
    for i in phone_num:
        helper.pressKey(i)
    # Klik lanjutkan    
    os.system(f'adb -s ' + device_id + ' shell input tap 530 1250')

def contactMediaPerm():
    # Klik lanjut
    os.system(f'adb -s ' + device_id + ' shell input tap 755 1585')
    # Klik izinkan kontak
    os.system(f'adb -s ' + device_id + ' shell input tap 535 1980')
    # Klik izinkkan media
    os.system(f'adb -s ' + device_id + ' shell input tap 535 1980')

def drivePerm():
    # Klik lewati
    os.system(f'adb -s ' + device_id + ' shell input tap 645 1360')

def profileSetup(name):
    # Klik input nama
    os.system(f'adb -s ' + device_id + ' shell input tap 530 900')
    # Input nama
    nama = [*name.upper()]
    for i in nama:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    # Klik lanjut
    os.system(f'adb -s ' + device_id + ' shell input tap 525 1300')


frontPage()
sleep(5)
contactMediaPerm()
sleep(5)
drivePerm()
sleep(5)
profileSetup('Justin Timberlake')