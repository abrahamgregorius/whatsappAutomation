import os
import random
from time import sleep
import requests
import uiautomator2 as u2
import subprocess
import sqlite3

device_id = "R9CT4007GBM"
packagename = "com.whatsapp"


response = requests.get("https://names.drycodes.com/1?combine=2&nameOptions=boy_names")
names = response.json()
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b", "com.aero"]

class AutoHelper:
    numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
    device_id = "R9CT4007GBM"
    d = u2.connect(device_id)

    def __init__(self):
        pass

    def adbs(self, command):
        a = subprocess.run(command, capture_output=True)
        return a.stdout.decode()

    def startApp(self):     
        self.d.app_start("" + self.generatePackage() + "")

    def generateFirstName(self):
        for i in names:
            res = i.split('_')[0]
            return res

    def generateLastName(self):
        for i in names:
            res = i.split('_')[1]
            return res

    def generatePassword(self):
        for i in names:
            res = i
            return res

    def pressKey(self, keycode):
        os.system(f'adb -s '+ self.device_id +' shell input keyevent KEYCODE_' + keycode)

    def pressSend(self):
        os.system(f'adb -s ' + self.device_id + ' shell input tap 985 2230') 

    def randomMonth(self):
        monthCoordinates = {
            "jan":"350 225",
            "feb":"350 360",
            "mar":"350 450",
            "apr":"350 550",
            "may":"350 650",
            "jun":"350 750",
            "jul":"350 850",
            "aug":"350 950",
            "sep":"350 1050",
            "oct":"350 1150",
            "nov":"350 1250",
            "dec":"350 1350",
        }
        res = random.choice(list(monthCoordinates.values()))
        return res

    def randomDay(self):
        day = random.randrange(1, 28, 1)
        return day

    def randomYear(self):
        year = random.randrange(1975, 1999, 1)
        return year

    def randomGender(self):
        genderCoordinates = {
            "m":"255 750",
            "f":"255 650"
        }
        res = random.choice(list(genderCoordinates.values()))
        return res

    def generateNumber(self):
        number = random.choice(self.numdata)
        return number

    def generatePackage(self):
        package = random.choice(packdata)
        return package

    def grantPermissionWhatsapp(self):
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.READ_CALL_LOG')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.ACCESS_FINE_LOCATION')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.ANSWER_PHONE_CALLS')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.RECEIVE_SMS')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.READ_EXTERNAL_STORAGE')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.ACCESS_COARSE_LOCATION')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.READ_PHONE_STATE')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.SEND_SMS')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.CALL_PHONE')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.WRITE_CONTACTS')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.CAMERA')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.GET_ACCOUNTS')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.WRITE_EXTERNAL_STORAGE')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.RECORD_AUDIO')
        os.system(f'adb -s '+ device_id +' shell pm grant com.whatsapp android.permission.READ_CONTACTS')

    def registerWhatsapp(self, phone_num, name):
        os.system(f'adb -s '+ self.device_id +' shell pm clear com.whatsapp')
        self.grantPermissionWhatsapp()
        self.d.app_start("com.whatsapp")
        try:
            self.d(text="English").click()
        except:
            print("No need to choose language")
        finally:
            self.d(text="AGREE AND CONTINUE").click()

        self.d(resourceId="com.whatsapp:id/registration_country").click()
        self.d(resourceId="com.whatsapp:id/menuitem_search").click()
        country = "INDONESIA"
        sleep(1)
        for i in country:
            self.pressKey(i)

        self.d(text="Indonesia").click()

        for i in phone_num:
            self.pressKey(i)
            
        self.d(text="NEXT").click()
        
        self.d(text="OK").click()
        self.d(text="SKIP").click()
        self.d.click(280, 900)
        nama = name.upper()
        for i in nama:
            if i == " ":
                self.pressKey("SPACE")
            self.pressKey(i)
        self.d(text="NEXT").click()

    def registerBusiness(self, phone_num, name):
        self.d.app_start('com.whatsapp.w4b')
        # For Original Whatsapp and Whatsapp Business
        try:
            self.d(text="English").click()
        except Exception:
            print("No need to choose language")
        finally:
            self.d(text="AGREE AND CONTINUE").click()
            self.d(text="USE A DIFFERENT NUMBER").click()
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click()
            self.d(text="CONTINUE").click()

            self.d(text="CONTINUE").click()
            self.d(text="Allow").click()
            self.d(text="Allow").click()
            self.d(text="SKIP").click()
            self.d.click(300, 840)

            nama = name.upper()
            for i in nama:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)
            self.d.click(990, 988)

            category = "other business"
            kategori = category.upper()
            for i in kategori:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)

            self.d(text="Other Business").click()
            self.d(text="NEXT").click()
            self.d(text="NOT NOW").click()

    def registerFm(self, phone_num, name):
        self.d.app_start('com.fmwhatsapp')
        try:
            # Allow access media
            self.d(text="Allow").click()
        except:
            print("There is no permission request")
        finally:
            # Front page
            self.d(text="AGREE AND CONTINUE").click()
            # Input number
            self.d(text="phone number").click()
            for i in phone_num:
                 self.pressKey(i)
            self.d(text="NEXT").click()

         # Switching from business
        try:
            self.d(text="SWITCH").click()
        except:
            print("No switch requested")
        finally:
            self.d(text="CONTINUE").click()
            self.d(text="Allow").click()   
            # Contacts and media permission
            self.d(text="CONTINUE").click()
            self.d(text="Allow").click()

              # Google permission
            self.d(text="SKIP").click()

            nama = name.upper()
            for i in nama:
                 if i == " ":
                      self.pressKey("SPACE")
                 self.pressKey(i)
            self.d(text="NEXT").click()
            self.d(text="CLOSE").click()

    def registerYo(self, phone_num, name):
        self.d.app_start('com.yowhatsapp')
        try:
              # Allow access media
              self.d(text="Allow").click()
        except:
            print("There is no permission request")
        finally:
            # Front page
            self.d(text="AGREE AND CONTINUE").click()
            # Input number
            self.d(text="phone number").click()
            for i in phone_num:
                 self.pressKey(i)
            self.d(text="NEXT").click()
        try:
            self.d(text="SWITCH").click()
        except:
            print("There is no switch request")
        finally:
            # Confirmation
            self.d(text="OK").click()
            # Verify hanya 7 jam sekali
            self.d(text="CONTINUE").click()
            self.d(text="Allow").click()

              # Contacts and media permission
            self.d(text="CONTINUE").click()
            self.d(text="Allow").click()

            # Google permission request
            self.d(text="SKIP").click()
            nama = name.upper()
            for i in nama:
                 if i == " ":
                      self.pressKey("SPACE")
                 self.pressKey(i)
            self.d(text="NEXT").click()
            self.d(text="CLOSE").click()

    def mediaSettings(self):
         self.d(text="SETTINGS").click()
         self.d(text="Permissions").click()
         os.system(f'adb -s' + self.device_id + ' shell input swipe 550 1690 550 970')
         self.d(text="Files and media").click()
         self.d(resourceId="com.android.permissioncontroller:id/allow_radio_button").click()

    def registerAero(self, phone_num, name):
        self.d.app_start('com.aero')
        try:
            self.d(text="Allow").click()
        except:
            print("Gaada prompt")
        finally:
            pass
        try:
            self.mediaSettings()
            self.d.app_stop("com.aero")
            self.d.app_start("com.aero")
            pass
        except:
            print("There is no permission request")
        finally:
            # Front page
            self.d(text="AGREE AND CONTINUE").click()
            # Input number
            self.d(text="phone number").click()
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click()
        try:
            self.d(text="SWITCH").click()
        except:
            print("No switch requested")
        finally:
            # Confirmation
            self.d(text="OK").click()
            # Verify hanya 7 jam sekali
            self.d(text="CONTINUE").click()
            self.d(text="Allow").click()

            nama = name.upper()
            for i in nama:
                 if i == " ":
                      self.pressKey("SPACE")
                 self.pressKey(i)
            self.d(text="NEXT").click()
            self.d(text="THANKS!").click()

    def sendMessage(self, phone_num, packageName, message):
        # Buka chatroom whatsapp
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ phone_num + '" ' + packageName)
        # Tulis pesan
        sleep(1)
        pesan = message.upper()
        for i in pesan:
            if i == " ":
                self.pressKey("SPACE")
            self.pressKey(i)
        # CLick send
        os.system(f'adb -s '+ self.device_id +' shell input tap 1000 2205')

    def pushPhoto(self, phone_num, packageName):
        os.system(f'adb -s '+ self.device_id +' push MEDIA/peekingsponge.jpg /storage/emulated/0/DCIM/')
        sleep(2)
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ phone_num +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/peekingsponge.jpg -p ' + packageName)
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 975 2183')
        
    def pushVideo(self, phone_num, packageName):
        # Push
        os.system(f'adb -s '+ self.device_id +' push MEDIA/video.mp4 /storage/emulated/0/DCIM/')
        sleep(2)
        # Send menu
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ phone_num +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/video.mp4 -p ' + packageName + '')
        sleep(2)
        os.system(f'adb -s '+ self.device_id +' shell input tap 888 1270')
        sleep(1)
        # Pop up 
        os.system(f'adb -s '+ self.device_id +' shell input tap 995 2125')

    def listAllWhatsapp(self):
        a = self.adbs(f'adb -s '+ self.device_id +' shell cmd package list packages | grep -E "whatsapp\|aero"')
        b = a.split()
        for i in b:
            print(i.split(':')[1])

    def checkActivity(self):
        a = self.adbs(f'adb -s '+ self.device_id +' shell dumpsys activity activities | grep -E "mCurrentFocus"')
        b = a.split()[2][:-1]
        c = b.split("/")[1]
        return c

    def checkStatus(self):
        status = self.checkActivity()
        try:
            if status == "com.whatsapp.registration.EULA":
                self.registerWhatsapp('85811403649', "Profile")
            elif status == "com.whatsapp.w4b.registration.EULA":
                self.registerBusiness('85811403649', "Profile")
            elif status == "com.fmwhatsapp.registration.EULA":
                self.registerFm('85811403649', "Profile")
            elif status == "com.yowhatsapp.registration.EULA":
                self.registerYo('85811403649', "Profile")
            elif status == "com.aero.registration.EULA":
                self.registerAero('85811403649', "Profile")
            elif status == ".userban.ui.BanAppealActivity":
                print("Device is banned")
        finally:
            self.sendMessage("Halo", self.generatePackage(), self.generateNumber())
    
    def makeCall(self, phone_num, packageName):
        # Buka chatroom whatsapp
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ phone_num + '" ' + packageName)
        sleep(3)
        os.system(f'adb -s '+ self.device_id +' shell input tap 900 190')
        self.d(text="CALL").click()
        # try:
        #     d(text="CONTINUE").click()
        #     d(text="While using the app").click()
        #     d(text="CONTINUE").click()
        #     d(text="Allow").click()
        # finally:
        os.system(f'adb -s '+ self.device_id +' shell input tap 900 190')
        
        

# UNUSED FUNCTIONS
# ALPHABET FUNCTION
# def pressA():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_A')
# def pressB():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_B')
# def pressC():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_C')
# def pressD():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_D')
# def pressE():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_E')
# def pressF():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_F')
# def pressG():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_G')
# def pressH():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_H')
# def pressI():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_I')
# def pressJ():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_J')
# def pressK():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_K')
# def pressL():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_L')
# def pressM():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_M')
# def pressN():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_N')
# def pressO():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_O')
# def pressP():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_P')
# def pressQ():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_Q')
# def pressR():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_R')
# def pressS():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_S')
# def pressT():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_T')
# def pressU():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_U')
# def pressV():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_V')
# def pressX():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_X')
# def pressY():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_Y')
# def pressZ():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_Z')
# 
# # NUMBER FUNCTIONS
# def press0():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_0')
# def press1():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_1')
# def press2():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_2')
# def press3():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_3')
# def press4():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_4')
# def press5():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_5')
# def press6():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_6')
# def press7():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_7')
# def press8():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_8')
# def press9():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_9')
# 
# # BUTTONS FUNCTIONS
# def pressPOWER():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_POWER')
# def pressMENU():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_MENU')
# def pressHOME():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_HOME')
# def pressCALL():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_CALL')
# def pressBACK():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_BACK')
# def pressENDCALL():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_ENDCALL')
# def pressSOFT_RIGHT():
#     os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_SOFT_RIGHT')
# def sendMessageWhatsapp(self, message, number):
#     os.system(f'adb -s ' + device_id + ' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.whatsapp')
#     sleep(3)
#     pesan = message.upper()
#     for i in pesan:
#         if i == " ":
#             self.pressKey("SPACE")
#         self.pressKey(i)
#     os.system(f'adb -s '+ device_id +' shell input tap 1000 2205')
# def sendMessageBusiness(self, message, number):
#     os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.whatsapp.w4b')
#     sleep(3)
#     pesan = message.upper()
#     for i in pesan:
#         if i == " ":
#             self.pressKey("SPACE")
#         self.pressKey(i)
#     os.system(f'adb -s '+ device_id +' shell input tap 1000 2205')
# def sendMessageAero(self, message, number):
#     os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.aero')
#     sleep(3)
#     pesan = message.upper()
#     for i in pesan:
#         if i == " ":
#             self.pressKey("SPACE")
#         self.pressKey(i)
#     os.system(f'adb -s '+ device_id +' shell input tap 1000 2205')
# def sendMessageFMWA(self, message, number):
#     os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.fmwhatsapp')
#     sleep(3)
#     pesan = message.upper()
#     for i in pesan:
#         if i == " ":
#             self.pressKey("SPACE")
#         self.pressKey(i)
#     os.system(f'adb -s '+ device_id +' shell input tap 1000 2205')
# def sendMessageYoWA(self, message, number):
#     os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ number +'" com.yowhatsapp')
#     sleep(3)
#     pesan = message.upper()
#     for i in pesan:
#         if i == " ":
#             self.pressKey("SPACE")
#         self.pressKey(i)
#     os.system(f'adb -s '+ device_id +' shell input tap 1000 2205')
# def newNumber(name, phone_number):
#     # Masuk ke menu adding contact
#     os.system('adb -s '+ device_id +' shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name '+ name +' -e phone 0'+ phone_number +' ')
#     # Choose save contact to
#     sleep(1)
#     os.system(f'adb -s ' + device_id + ' shell input tap 300 200')
#     sleep(1)
#     os.system(f'adb -s ' + device_id + ' shell input tap 270 340')
#     # Click save
#     sleep(1)
#     os.system(f'adb -s ' + device_id + ' shell input tap 780 2206')