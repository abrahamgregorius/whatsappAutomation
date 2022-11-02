import os
import random
from time import sleep
import uiautomator2 as u2
import helper

device_id = "R9CT4007GBM"

# Phone number and package name data
numdata = ["85811403649", "895410808876", "895410810679", "895410810680", "81527650313"]
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b", "com.aero"]

# Connecting device to UIAutomator
d = u2.connect(device_id)

def generateNumber():
    number = random.choice(numdata)
    return number
def generatePackage():
    package = random.choice(packdata)
    return package

def sendMessage(message, phone, packageName):
    # Buka chatroom whatsapp
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ phone + '"' + packageName + '')
    # Tulis pesan
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    # CLick send
    os.system(f'adb -s '+ device_id +' shell input tap 1000 2205')
        
def sendMessageWhatsapp(message, number):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.whatsapp')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageBusiness(message, number):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.whatsapp.w4b')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageAero(message, number):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.aero')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageFMWA(message, number):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.fmwhatsapp')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageYoWA(message, number):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.yowhatsapp')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

message = "Halo"
functions = [helper.sendMessageWhatsapp,helper.sendMessageAero,helper.sendMessageFMWA,helper.sendMessageBusiness,helper.sendMessageYoWA]

while True:
    #sendMessage("halo nama saya", generateNumber(), generatePackage())
    #try:
    #    d(text="OK").click()
    #except:
    #    print("nothing")
    
    a = random.choice(functions)
    a("Hello world", generateNumber())
