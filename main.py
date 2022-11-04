import os
from time import sleep
import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")

data = [["85811403649", "com.whatsapp"], ["895410810679", "com.fmwhatsapp"], ["895410810680", "com.yowhatsapp"], ["895410808876", "com.whatsapp.w4b"]]
numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b"]
device_id = "R9CT4007GBM"

autoHelper = helper.AutoHelper("R9CT4007GBM")

def startApp():     
    d.app_start("" + autoHelper.generatePackage() + "")

def pushPhoto(packageName):
    os.system(f'adb -s '+ device_id +' push MEDIA/peekingsponge.jpg /storage/emulated/0/DCIM/')
    sleep(2)
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ autoHelper.phone_number +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/peekingsponge.jpg -p ' + packageName)
    sleep(1)
    os.system(f'adb -s '+device_id+' shell input tap 975 2183')

while True:
#     first = Main("Nenek", helper.generateNumber(), "R9CT4007GBM")
#     first.pushVideo(helper.generatePackage())
    autoHelper.registerWhatsapp('81239283553', 'Bambang')