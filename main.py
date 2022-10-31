import os
import registerbusiness
import registerfm
import registeraero
import registeruiauto
import registeryo
import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")

data = [["895410810664", "com.whatsapp"], ["895410810679", "com.fmwhatsapp"], ["895410810680", "com.yowhatsapp"], ["895410808876", "com.whatsapp.w4b"]]
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
        os.system('adb -s '+ self.device_id +' shell "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name '+ self.name +' -e phone 0'+ self.phone_number +' ')
        # Choose save contact to
        os.system(f'adb -s ' + device_id + ' shell input tap 300 200')
        os.system(f'adb -s ' + device_id + ' shell input tap 270 340')
        # Click save
        d(packageName="com.samsung.android.app.contacts", resourceId="com.samsung.android.app.contacts:id/menu_done").click()

    def sendMessageWhatsapp(self, message, packageName):
        # Buka chatroom whatsapp
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ self.phone_number + packageName + '')
        # Pencet message box
        os.system(f'adb -s ' + device_id + ' shell input tap 285 2210')
        # Tulis pesan
        pesan = message.upper()
        for i in pesan:
            if i == " ":
                helper.pressKey("SPACE")
            helper.pressKey(i)
        os.system(f'adb -s ' + device_id + ' shell input tap 996 2205')
        


        
first = Main("Bambang", helper.generateNumber(data), "R9CT4007GBM")
first.newNumber()
first.sendMessageWhatsapp("Halo cuy mantap jiwa", helper.generatePackageName(data))

