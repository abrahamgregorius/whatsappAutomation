import os
import random
from time import sleep
import uiautomator2 as u2
import helper

device_id = "R9CT4007GBM"

# Phone number and package name data
numdata = ["85811403649", "895410810679", "81239283626", "895410808876"]
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b"]

# Connecting device to UIAutomator
d = u2.connect(device_id)

class Main:
    # Initialize properties
    def __init__ (self, phone): 
        self.phone = phone
    def sendMessage(self, message, packageName):
        # Buka chatroom whatsapp
        os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ self.phone + '"' + packageName + '')
        # Tulis pesan
        sleep(3)
        pesan = message.upper()
        for i in pesan:
            if i == " ":
                helper.pressKey("SPACE")
            helper.pressKey(i)
        # CLick send
        d(resourceId="" + packageName + ":id/send").click()

def generateNumber():
    number = random.choice(numdata)
    return number
def generatePackage():
    package = random.choice(packdata)
    return package
def sendMessage(phone, message, packageName):
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

        
def sendMessageWhatsapp(message):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=6281311951704" com.whatsapp')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageBusiness(message):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=6281311951704" com.whatsapp.w4b')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageAero(message):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=6281311951704" com.aero')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageFMWA(message):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=6281311951704" com.fmwhatsapp')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')

def sendMessageYoWA(message):
    os.system(f'adb -s R9CT4007GBM shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=6281311951704" com.yowhatsapp')
    sleep(3)
    pesan = message.upper()
    for i in pesan:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    os.system(f'adb -s R9CT4007GBM shell input tap 1000 2205')


# Inisiasi variabel terlebih dahulu
a = generatePackage()
b = generateNumber()

#first = Main(b)
#first.sendMessage("Hello World", a)

message = "Halo"

functions = [sendMessageWhatsapp,sendMessageAero,sendMessageFMWA,sendMessageBusiness,sendMessageYoWA]

while True:
    a = random.choice(functions)
    a("Hello world")