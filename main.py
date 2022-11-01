import os
from time import sleep
import registerbusiness
import registerfm
import registeraero
import registeruiauto
import registeryo
import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")

data = [["895410810664", "com.whatsapp"], ["895410810679", "com.fmwhatsapp"], ["895410810680", "com.yowhatsapp"], ["895410808876", "com.whatsapp.w4b"], ["81311951704", "com.aero"]]
device_id = "R9CT4007GBM"

class Main:
    def __init__(self, name="Bambang", phone_number="", device_id="R9CT4007GBM"):
        self.name = name
        self.phone_number = phone_number
        self.device_id = device_id

    def startApp(self):     
        d.app_start("" + helper.generatePackageName(data) + "")
    
    def newNumber(self):
        # Masuk ke menu adding contact
        os.system('adb -s '+ self.device_id +' shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name '+ self.name +' -e phone 0'+ self.phone_number +' ')
        # Choose save contact to
        sleep(1)
        os.system(f'adb -s ' + device_id + ' shell input tap 300 200')
        sleep(1)
        os.system(f'adb -s ' + device_id + ' shell input tap 270 340')
        # Click save
        sleep(1)
        os.system(f'adb -s ' + device_id + ' shell input tap 780 2206')

    def sendMessage(self, message, packageName):
        # Buka chatroom whatsapp
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ self.phone_number + '"' + packageName + '')
        # Pencet message box
        os.system(f'adb -s ' + device_id + ' shell input tap 285 2210')
        # Tulis pesan
        sleep(3)
        pesan = message.upper()
        for i in pesan:
            if i == " ":
                helper.pressKey("SPACE")
            helper.pressKey(i)
        os.system(f'adb -s ' + device_id + ' shell input tap 996 2205')

    def pushVideo(self, packageName):
        # Push
        os.system(f'adb -s '+ self.device_id +' push MEDIA/video.mp4 /storage/emulated/0/DCIM/')
        sleep(2)
        # Send menu
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ self.phone_number +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/video.mp4 -p ' + packageName + '')
        sleep(1)
        # Pop up 
        if d(resourceId="android:id/message").get_text().split()[0] == "Share":
            d(text="OK").click()
        # Click send
        d(resourceId="com.whatsapp:id/send").click()

    def pushPhoto(self, packageName):
        # Push
        os.system(f'adb -s '+ self.device_id +' push MEDIA/peekingsponge.jpg /storage/emulated/0/DCIM/')
        sleep(2)
        # Send menu
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ self.phone_number +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/peekingsponge.jpg -p ' + packageName + '')
        sleep(1)
        # If packageName is com.fmwhatsapp
        if packageName == "com.fmwhatsapp":
            try:
                registerfm.mediaPermission()
                os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ self.phone_number +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/peekingsponge.jpg -p ' + packageName + '')
            except:
                print("There is no request for media permission in FMWhatsapp")
            finally:
                # Press send
                d(resourceId="com.whatsapp:id/send").click()
        else:
            # Click send
            d(resourceId="com.whatsapp:id/send").click()
        
    
# first = Main("Kakak", "81311951704", "R9CT4007GBM")
# first.pushPhoto(helper.generatePackageName(data))

testa = helper.generatePackageName(data)
print(testa)