import os
import random
from time import sleep
import requests
import uiautomator2 as u2
import subprocess
import sqlite3
import time

packagename = "com.whatsapp"


packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b", "com.aero"]

class AutoHelper:
    numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
    device_id = "R9CT4000AAM"
    d = u2.connect(device_id)

    def __init__(self):
        pass

    def adbs(self, command):
        a = subprocess.run(command, capture_output=True)
        return a.stdout.decode()

    def startApp(self):     
        self.d.app_start("" + self.generatePackage() + "")
        
    def resetAdb(self):
        os.system(f'adb kill-server')
        sleep(15)
        os.system(f'adb start-server')

    def pressKey(self, keycode):
        os.system(f'adb -s '+ self.device_id +' shell input keyevent KEYCODE_' + keycode)

    def pressSend(self):
        os.system(f'adb -s ' + self.device_id + ' shell input tap 985 2230') 

    def dumpUi(self, device_id):
        # os.system(f'adb kill-server')
        currentTime = time.ctime().split(" ")[3].replace(":", "_")
        os.system(f'adb -s '+ device_id +' shell uiautomator dump /sdcard/' + device_id + "_" + currentTime + '.xml ')
        print(
        sleep(1)
        os.system(f'adb -s '+ device_id +' pull /sdcard/' + device_id + "_" + currentTime + '.xml ~/Desktop/koko/flow/whatsappRegister' + device_id + currentTime + '.xml')
        print(currentTime)
        # os.system(f'adb -s '+ device_id +' shell rm /sdcard/' + device_id + "_" + currentTime + '.xml')

    def installPackages(self):
        os.system(f'adb -s ' + self.device_id + ' install apk/com.whatsapp.apk')
        os.system(f'adb -s ' + self.device_id + ' install apk/com.whatsapp.w4b.apk')
        os.system(f'adb -s ' + self.device_id + ' install apk/com.aero.apk')
        os.system(f'adb -s ' + self.device_id + ' install apk/com.yowhatsapp.apk')
        os.system(f'adb -s ' + self.device_id + ' install apk/com.fmwhatsapp.apk')

    def uninstallPackages(self):
        os.system(f'adb -s ' + self.device_id + ' uninstall com.whatsapp')
        os.system(f'adb -s ' + self.device_id + ' uninstall com.whatsapp.w4b')
        os.system(f'adb -s ' + self.device_id + ' uninstall com.aero')
        os.system(f'adb -s ' + self.device_id + ' uninstall com.yowhatsapp')
        os.system(f'adb -s ' + self.device_id + ' uninstall com.fmwhatsapp')

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

    def enableWifi(self):
        os.system(f'adb -s '+ self.device_id +' shell svc wifi enable')

    def disableWifi(self):
        os.system(f'adb -s '+ self.device_id +' shell svc wifi disable')

    def makeConnection(self, wifiName, security, password):
        os.system(f'adb -s '+ self.device_id +' shell cmd -w wifi connect-network '+ wifiName + ' '+ security + ' '+ password)

    def resetConnection(self):
        os.system(f'adb -s '+ self.device_id +' shell am start -n "com.android.settings/.Settings"')
        os.system(f'adb -s '+ self.device_id +' shell input swipe 500 2000 500 100')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 500 900')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 500 2150')
        sleep(1)
        self.d(text="Reset network settings").click()
        sleep(2)
        self.d(text="Reset settings").click()
        sleep(2)
        self.d(text="Reset").click()
        sleep(3)
        self.pressKey("HOME")
        

    def grantPermission(self, packageName):
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.READ_CALL_LOG')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.ACCESS_FINE_LOCATION')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.ANSWER_PHONE_CALLS')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.RECEIVE_SMS')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.READ_EXTERNAL_STORAGE')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.ACCESS_COARSE_LOCATION')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.READ_PHONE_STATE')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.SEND_SMS')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.CALL_PHONE')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.WRITE_CONTACTS')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.CAMERA')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.GET_ACCOUNTS')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.WRITE_EXTERNAL_STORAGE')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.RECORD_AUDIO')
        os.system(f'adb -s '+ self.device_id +' shell pm grant '+ packageName +' android.permission.READ_CONTACTS')

    def setLanguage(self):
        os.system("adb -s " + self.device_id + " shell am start -a android.settings.LOCALE_SETTINGS")
        print("In the menu")
        try:
            self.d(text="English (United States)").click()
            self.d(text="Terapkan").click()
        except Exception:
            print("No English option")
            try:
                print("Adding language")
                self.d(text="Tambah bahasa").click()
                self.d(text="English").click()
                self.d(text="United States").click()
                self.d(text="Atr sbg default").click()
            except Exception:
                print("Already in English")
                return 
            
    def checkPopup(self):
        while True:
            try:
                text = self.d(resourceId="android:id/message").get_text()
                result = text.split(".")[0]
                return result
            except Exception:
                print("No message")
                
                break

    def registerWhatsapp(self, phone_num, name):
        
        # Granting permission and starting app
        try:
            self.grantPermission("com.whatsapp")
            self.d.app_start("com.whatsapp")
            print("Permission granted and started app")
        except:
            print("Permission not granted and app not started")

        
        # English option
        try:
            self.d(text="English").click()
        except Exception:
            print("No need to choose language")


        # Agree and continue
        try:    
            self.d(text="AGREE AND CONTINUE").click()
            print("Success AGREE AND CONTINUE")
        except:
            print("Failed clicking AGREE AND CONTINUES")
        
            
        # Clicking country picker and search bar
        try:
            self.d(resourceId="com.whatsapp:id/registration_country").click()
            print("Clicked country picker")
            self.d(resourceId="com.whatsapp:id/menuitem_search").click()
            print("Clicked search bar")
        except:
            print("Clicked country picker and search bar")

        # Choosing INDONESIA
        try:
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            self.d(text="Indonesia").click()
            print("Success choosing Indonesia")
        except:
            print("Failed choosing Indonesia")

        
        # Typing phone number
        try:
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click()
            print("Success clicking phone number")
        except:
            print("Failed clicking phone number")
        

        # Switching request
        try:
            self.d(text="SWITCH").click()
            print("Clicked SWITCH")
        except Exception:
            print("No switch requested")


        # Clicking OK
        try:
            self.d(text="OK").click()
            print("Clicked OK")
        except Exception:
            print("No OK button")
        sleep(10)


        # Clicking SKIP
        try:
            self.d(text="SKIP").click()
            print("Success skip")
        except:
            print("Failed skip")


        # Google backup
        try:
            self.d(text="SKIP").click()
        except Exception:
            print("No skip button")


        # Registering name
        try:
            self.d.click(280, 900)
            nama = name.upper()
            for i in nama:
                if i == " ":
                    self.pressKey("SPACE")
            self.pressKey(i)
            print("Success typing name")
        except:
            print("Failed input name")
            
            
        # Clicking NEXT
        try:
            self.d(text="NEXT").click()
            print("Clicked NEXT")
        except:
            print("Failed clicking NEXT")



    def registerBusiness(self, phone_num, name):
        
        # Granting permission and starting app
        self.grantPermission("com.whatsapp.w4b")
        self.d.app_start('com.whatsapp.w4b')
        print("Granted permissions and started app")


        # English option
        try:
            self.d(text="English").click()
            print("Clicked English")
        except Exception:
            print("No ENGLISH button")
            

        # Agree and continue
        try:
            self.d(text="AGREE AND CONTINUE").click()
            print("Clicked Agree and continue")
        except:
            print("Failed clicking Agree and continue")
    
    
        # Use a different number 
        try:
            self.d(text="USE A DIFFERENT NUMBER").click()
            print("Clicked USE A DIFFERENT NUMBER")
        except Exception:
            print("No USE A DIFFERENT NUMBER button")
        
        
        # Clicking country picker and search bar
        try:  
            self.d(resourceId="com.whatsapp.w4b:id/registration_country").click()
            print("Clicked country picker")
        except:
            print("Failed clicking country picker")
        try:
            self.d(resourceId="com.whatsapp.w4b:id/menuitem_search").click()
            print("Clicked search bar")
        except:
            print("Failed clicking search bar")
            
        
        # Typing and choosing Indonesia
        try:
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            self.d(text="Indonesia").click()
            print("Clicked INDONESIA")
        except:
            print("Failed choosing Indonesia")


        # Typing number and clicking next
        try:
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click()
        except:
            print("Failed typing number and clicking NEXT")


        # Clicking USE THIS NUMBER button
        try: 
            self.d(resourceId="com.whatsapp.w4b:id/use_consumer_app_info_button").click()
        except:
            print("Failed clicking USE THIS NUMBER button")


        # Clicking CONTINUE and OK
        try:
            self.d(text="CONTINUE").click()
        except Exception:
            print("Failed clicking CONTINUE button")
        try:
            self.d(text="OK").click()
        except:
            print("Failed clicking OK button")


        # Google Backup
        try:
            self.d(text="SKIP").click()
        except Exception:
            print("No skip button")

        
        # Registering name
        try:
            self.d(resourceId="com.whatsapp.w4b:id/registration_name").click()
            self.d(resourceId="com.whatsapp.w4b:id/registration_name").clear_text()
            nama = name.upper()
            for i in nama:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)
            print("Success registering name")
        except:
            print("Failed registering name")


        # Clicking BUSINESS TYPE menu
        try:
            self.d(resourceId="com.whatsapp.w4b:id/register_name_business_categories").click()
            print("Clicked BUSINESS TYPE menu")
        except:
            print("Failed clicking BUSINESS TYPE menu")


        # Clicking and clearing search bar
        try:
            self.d(resourceId="com.whatsapp.w4b:id/search_src_text").click()
            self.d(resourceId="com.whatsapp.w4b:id/search_src_text").clear_text()
            print("Clicked and cleared search bar")
        except:
            print("Failed clicking and clearing search bar")
            
            
        # Choosing other business
        try:
            category = "other"
            kategori = category.upper()
            for i in kategori:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)
            sleep(1.5)
            self.d(text="Other Business").click()
            print("Chosen OTHER BUSINESS")
        except:
            print("Failed choosing OTHER BUSINESS")

        
        # Clicking NEXT
        try:
            self.d(text="NEXT").click()
            print("Clicked NEXT")
        except: 
            print("Failed clicking NEXT")
            
        sleep(6)

        # Clicking NOT NOW
        try:
            self.d(text="NOT NOW").click()
            print("Clicked NOT NOW")
        except:
            print("Failed clicking NOT NOW")



    def registerFm(self, phone_num, name):        
        # Granting permission and starting app
        self.grantPermission("com.fmwhatsapp")
        self.d.app_start('com.fmwhatsapp')
        print("Granted permissions and started app")


        # Agree and continue
        try:
            self.d(text="AGREE AND CONTINUE").click(timeout=25)
            print("Clicked Agree and Continue")
        except:
            print("Failed clicking Agree and Continue")
        
        
        # Clicking country picker and search bar
        try:
            self.d(resourceId="com.fmwhatsapp:id/registration_country").click(timeout=25)
            print("Clicked country picker")
            self.d(resourceId="com.fmwhatsapp:id/menuitem_search").click(timeout=25)
            print("Clicked country picker search bar")
        except:
            print("Failed clicking country picker and search bar")
        
        
        # Typing and clicking INDONESIA        
        try:
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            print("Typed country")
            self.d(text="Indonesia").click(timeout=25)
            print("Typed and clicked Indonesia")
        except:
            print("Failed typing and clicking Indonesia")
        
        
        # Typing phone number
        try:
            for i in phone_num:
                self.pressKey(i)
            print("Typed phone number")
        except:
            print("Failed typing phone number")
            
        # Clicking NEXT
        try:
            self.d(text="NEXT").click(timeout=25)
            print("Clicked NEXT")
        except:
            print("No NEXT button")

        # Switching from business
        try:
            self.d(text="SWITCH").click(timeout=10)
        except Exception:
            print("No switch requested")
        
        # Clicking OK
        try:
            self.d(text="OK").click(timeout=25)
        except Exception:
            print("No OK button")
        
        # Google permission
        try:
            self.d(text="SKIP").click(timeout=25)
        except Exception:
            print("No skip button")


        # Inputting name
        try:
            sleep(5)
            self.d(resourceId="com.fmwhatsapp:id/registration_name").click(timeout=25)
            nama = name.upper()
            for i in nama:
                    if i == " ":
                        self.pressKey("SPACE")
                    self.pressKey(i)
        except:
            print("Unable to input name")
        
        # Clicking NEXT
        try:
            self.d(text="NEXT").click(timeout=25)
        except:
            print("No NEXT button")
        
        # Clicking CANCEL
        try: 
            self.d(text="CANCEL").click(timeout=25)
        except:
            print("No CANCEL button")
            
        # Clicking CLOSE
        try:
            self.d(text="CLOSE").click(timeout=25)
        except:
            print("No CLOSE button")
        
        # Clicking OK for changelog
        try:
            self.d(text="OK").click(timeout=25)
        except:
            print("No OK button")


        
    def registerYo(self, phone_num, name):        
        # Granting permission and starting app
        try:
            self.grantPermission("com.yowhatsapp")
            self.d.app_start('com.yowhatsapp')
            print("Permission granted and started app")
        except:
            print("Permission not granted and app is not started")


        # Agree and continue
        try:
            self.d(text="AGREE AND CONTINUE").click(timeout=15)
            print("Clicked AGREE AND CONTINUE")
        except:
            print("Failed clicking AGREE AND CONTINUE")


        # Country picking and choosing Indonesia
        try:
            self.d(resourceId="com.yowhatsapp:id/registration_country").click(timeout=15)
            self.d(resourceId="com.yowhatsapp:id/menuitem_search").click(timeout=15)
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            self.d(text="Indonesia").click(timeout=15)
        except: 
            print("Failed picking country and choosing INDONESIA")


        # Input number
        try:
            self.d(text="phone number").click(timeout=15)
            for i in phone_num:
                    self.pressKey(i)
            self.d(text="NEXT").click(timeout=15)
        except: 
            print("Failed inputting number and clicking NEXT")


        # Switching from Business
        try:
            self.d(text="SWITCH").click(timeout=15)
        except Exception:
            print("There is no switch request")


        # Confirmation
        try:
            self.d(text="OK").click(timeout=15)
        except Exception:
            print("No OK button")


        # Backing up from Google Drive
        try:
            self.d(text="SKIP").click(timeout=15)
        except Exception:
            print("No skip button")


        # Inputting name
        try:
            sleep(5)
            nama = name.upper()
            for i in nama:
                    if i == " ":
                        self.pressKey("SPACE")
                    self.pressKey(i)
        except:
            print("Failed inputting name")


        # Clicking NEXT
        try:
            self.d(text="NEXT").click(timeout=15)
        except Exception:
            print("No NEXT button")

        # Clickng CANCEL for updates
        try:
            self.d(text="CANCEL").click(timeout=15)
        except:
            print("No CANCEL button")
        
        # Clicking CLOSE
        try:
            self.d(text="CLOSE").click(timeout=15)
        except Exception:
            print("No CLOSE button")
            
        # Clicking OK for changelog
        try:
            self.d(text="OK").click(timeout=25)
        except:
            print("No OK button")



    def registerAero(self, phone_num, name):
        # Granting permission and starting app
        try:
            self.grantPermission("com.aero")
            self.d.app_start("com.aero")
            print("Permission granted and app started")
        except: 
            print("Permission not granted and app not started")
        
        
        # Front page
        try:
            self.d(text="AGREE AND CONTINUE").click(timeout=15)
            print("Clicked AGREE AND CONTINUE")
        except:
            print("Failed clicking AGREE AND CONTINUE")


        # Clicking country picker and search bar
        try:
            self.d(resourceId="com.aero:id/registration_country").click(timeout=15)
            self.d(resourceId="com.aero:id/menuitem_search").click(timeout=15)
            print("Clicked country picker and search bar")
        except:
            print("Failed clicking country picker and search bar")
        
        
        # Typing and choosing INDONESIA
        try:
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            self.d(text="Indonesia").click(timeout=15)
            print("Success choosing INDONESIA")
        except: 
            print("Failed typing and choosing INDONESIA")


        # Inputting number
        try:
            self.d(text="phone number").click(timeout=15)
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click(timeout=15)
            print("Inputted phone number and clicked NEXT")
        except: 
            print("Failed inputting phone number and clicked NEXT")
            
        
        
        
        # Switching from Business
        try:
            self.d(text="SWITCH").click(timeout=15)
        except Exception:
            print("No switch requested")

        
        # Confirmation
        try:
            self.d(text="OK").click(timeout=15)
        except Exception:
            print("No OK button")
            
        # Google backup
        try:
            self.d(text="SKIP").click(timeout=15)
            print("Clicked SKIP")
        except:
            print("Failed clicking SKIP")


        # Inputting name
        try:
            nama = name.upper()
            for i in nama:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)
            print("Success inputting name")
        except:
            print("Failed inputting name")
        
        
        # Clicking NEXT
        try:
            self.d(text="NEXT").click(timeout=15)
        except Exception:
            print("No NEXT button")
        
        
        # Clicking LATER
        try:
            self.d(text="LATER").click(timeout=15)
        except Exception:
            print("No LATER button")
        
        
        # Clicking THANKS
        try:
            self.d(text="THANKS!").click(timeout=15)
        except Exception:
            print("No THANKS button")
            
        # Clicking OK
        try:
            self.d(text="OK").click(timeout=15)
        except Exception:
            print("No OK button")



    def sendMessage(self, phone_num, packageName, message):
        # Buka chatroom whatsapp - use country code when inputting number 
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone='+ phone_num + '" ' + packageName)
        # Tulis pesan
        self.d(resourceId="com.whatsapp:id/entry").clear_text()
        sleep(1)
        pesan = message.upper()
        for i in pesan:
            if i == " ":
                self.pressKey("SPACE")
            self.pressKey(i)
        # CLick send
        os.system(f'adb -s '+ self.device_id +' shell input tap 1000 2205')

    def pushPhoto(self, phone_num, packageName, message=None):
        os.system(f'adb -s '+ self.device_id +' push MEDIA/peekingsponge.jpg /storage/emulated/0/DCIM/Camera')
        sleep(2)
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ phone_num +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/Camera/peekingsponge.jpg -p ' + packageName)
        sleep(1)
        self.d(resourceId="com.whatsapp:id/caption").set_text(message)
        sleep(1)
        self.d(resourceId="com.whatsapp:id/send").click()

    def pushVideo(self, phone_num, packageName, message=None):
        # Push
        os.system(f'adb -s '+ self.device_id +' push MEDIA/video.mp4 /storage/emulated/0/DCIM/Camera')
        sleep(2)
        # Send menu
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t text/plain -e jid "62'+ phone_num +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/Camera/video.mp4 -p ' + packageName + '')
        sleep(2)
        os.system(f'adb -s '+ self.device_id +' shell input tap 888 1270')
        sleep(1)
        self.d(resourceId="com.whatsapp:id/caption").set_text(message)
        sleep(1)
        self.d(resourceId="com.whatsapp:id/send").click()
        
    def listAllWhatsapp(self):
        a = self.adbs(f'adb -s '+ self.device_id +' shell cmd package list packages | grep -E "whatsapp\|aero"')
        b = a.split()
        for i in b:
            print(i.split(':')[1])

    def checkActivity(self):
        try:
            a = self.adbs(f'adb -s '+ self.device_id +' shell dumpsys activity activities | grep -E "mCurrentFocus"')
            b = a.split()[2][:-1]
            c = b.split("/")[1]
            return c
        except Exception:
            return None

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
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ phone_num + '" ' + packageName)
        sleep(3)
        os.system(f'adb -s '+ self.device_id +' shell input tap 900 190')
        self.d(text="CALL").click() 

    

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