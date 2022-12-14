import os
import random
from time import sleep
import requests
import uiautomator2 as u2
import subprocess
import sqlite3

packagename = "com.whatsapp"


response = requests.get("https://names.drycodes.com/1?combine=2&nameOptions=boy_names")
names = response.json()
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

    def generatePassword(self):
        for i in names:
            res = i
            return res

    def pressKey(self, keycode):
        os.system(f'adb -s '+ self.device_id +' shell input keyevent KEYCODE_' + keycode)

    def pressSend(self):
        os.system(f'adb -s ' + self.device_id + ' shell input tap 985 2230') 

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

    def registerWhatsapp(self, phone_num, name):
        os.system(f'adb -s '+ self.device_id +' shell pm clear com.whatsapp')
        self.grantPermission("com.whatsapp")
        self.d.app_start("com.whatsapp")

        status = self.checkActivity()

        if status == "com.whatsapp/com.whatsapp.registration.EULA":
            try:
                self.d(text="English").click()
            except Exception:
                print("No need to choose language")
            try:
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
            except Exception:
                return False
        
            try:
                self.d(text="SKIP").click()
                print("Success skip")
            except:
                print("Failed skip")
        
            i = 0

            while True:
                data_acc = self.heperny.getAccounts()

                checkbydb_columotp = self.heperny.checkSmsOtpColumn(self.pull_id)
                if checkbydb_columotp[4] != None:
                    numberotp = checkbydb_columotp[4]
                    print(numberotp)
                    break
                else:
                    print("Waiting SMS Recive OTP")
                i+=1
                if i > 60:
                    return False
                    break
                sleep(1)
            try:
                print("OTP FOUND "+str(numberotp))
                os.system(f'adb -s '+self.device_id+' shell input text "'+str(numberotp)+'"')
                sleep(1)


                updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                print("Set pullid otp to null")
                print("Success input otp")
            except Exception:
                updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                print("Set pullid otp to null")
                print("Failed input otp")

            try:
                self.d(text="OK").click()
                sleep(1)
                self.d(text="SKIP").click()


                print("Success klik ok and skip")
            except Exception:
                print("Failed Skip backup")
        
            try:
                self.d.click(280, 900)
                nama = name.upper()
                for i in nama:
                    if i == " ":
                        self.pressKey("SPACE")
                    self.pressKey(i)
                self.d(text="NEXT").click()
            except Exception:
                return False
            
        else:
            self.heperny.updateAccApps(1, "com.whatsapp", self.data_account[0])
            return True

    def registerBusiness(self, phone_num, name):
        os.system(f'adb -s '+ self.device_id +' shell pm clear com.whatsapp.w4b')
        self.grantPermission("com.whatsapp.w4b")
        self.d.app_start('com.whatsapp.w4b')

        status = self.checkActivity()
        
        # Indefinite page (Halaman tidak selalu muncul)
        try:
            self.d(text="English").click(timeout=15)
        except Exception:
            print("No need to choose language")

        # Halaman awal
        try:
            self.d(text="AGREE AND CONTINUE").click(timeout=15)
        except:
            print("Next step, 'AGREE AND CONTINUE' already pressed")

        # First "USE A DIFFERENT NUMBER" page
        try:
            self.d(text="USE A DIFFERENT NUMBER").click(timeout=15)
        except Exception:
            print("No need to use a different number")

        # Clicking "registration_country" in "RegisterPhone"
        try:
            self.d(resourceId="com.whatsapp.w4b:id/registration_country").click(timeout=15)
        except:
            print("Already clicked 'registration_country'")

        # Typing and choosing "Indonesia" as "registration_country"
        try:
            self.d(resourceId="com.whatsapp.w4b:id/menuitem_search").click(timeout=15)
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            self.d(text="Indonesia").click(timeout=15)
            print("Country 'Indonesia' is picked")
        except:
            print("Failed")

        # Second "USE A DIFFERENT NUMBER" page
        try:
            self.d(resourceId="com.whatsapp.w4b:id/use_consumer_app_info_button").click(timeout=15)
        except:
            print("Failed use the same number")
        
        # Type "phone_number"
        try:
            self.d(resourceId="com.whatsapp.w4b:id/registration_phone").click(timeout=15)
            print(phone_num)
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click(timeout=15)
        except Exception:
            return False

        try:
            self.d(text="OK").click(timeout=10)
        except:
            print("Failed clicked OK")
            
        try:
            self.d(text="OK").click(timeout=10)
        except:
            print("Failed clicked OK")

        try:
            self.d(text="CONTINUE").click(timeout=15)
        except Exception:
            print("Failed clicked CONTINUE")


        # Receive and type OTP
        i = 0
        while True:
            data_acc = self.heperny.getAccounts()

            checkbydb_columotp = self.heperny.checkSmsOtpColumn(self.pull_id)
            if checkbydb_columotp[4] != None:
                numberotp = checkbydb_columotp[4]
                print(numberotp)
                break
            else:
                print("Waiting SMS Recive OTP")
            i+=1
            if i > 100:            
                os.system(f'adb -s '+ self.device_id + ' shell pm clear com.whatsapp.w4b')
                break
            sleep(1)
        try:
            print("OTP FOUND "+str(numberotp))
            os.system(f'adb -s '+self.device_id+' shell input text "'+str(numberotp)+'"')
            sleep(1)

            updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)


            print("Set pullid otp to null")
            print("Success input otp")
        except Exception:
            updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
            print("Set pullid otp to null")
            print("Failed input otp")

        try:
            self.d(text="SKIP").click(timeout=15)
            self.d.click(300, 840)
            print("success skip")
        except:
            print("No Skipp")
        
        # Type name
        print("MAU INPUT NAME "+str(status))
            
        try:
            print("MASUK INPUT NAME")
            self.d(resourceId="com.whatsapp.w4b:id/registration_name").click(timeout=15)
            self.d(resourceId="com.whatsapp.w4b:id/registration_name").clear_text()
            # nama = name.upper()
            genertname = namegenerator.gen().split("-")[0]
            nama = genertname.upper()
            for i in nama:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)
        except:
            print("Failed input name")

        # Clicking business category menu
        try:
            self.d(resourceId="com.whatsapp.w4b:id/register_name_business_categories").click(timeout=15)
        except:
            print("Failed clicked 'Business Category'")
        print("MAU INPUT CHOICE CATEGORY "+str(status))
        

        # Choosing business type
        try:
            self.d(resourceId="com.whatsapp.w4b:id/search_src_text").click(timeout=30.0)
            self.d(resourceId="com.whatsapp.w4b:id/search_src_text").clear_text()
            self.d(resourceId="com.whatsapp.w4b:id/search_src_text").click(timeout=30.0)
            category = "other business".upper()
            for i in category:
                if i == " ":
                    self.pressKey("SPACE")
                
                self.pressKey(i)
                sleep(0.5)
            print("Done search other business")
        except:
            print("Failed to search other business")
        sleep(2)


        try:
            self.d(text="Other Business").click(timeout=30.0)
            
        except:
            print("Failed click 'Other Business'")
        sleep(1)
        
        try:
            self.d(text="NEXT").click(timeout=30.0)
        except:
            print("Failed clicked 'NEXT'")

        try:
            self.d(text="NOT NOW").click(timeout=30.0) 
        except:
            print("Not now error")
            return False
                    
    def registerFm(self, phone_num, name):
        os.system(f'adb -s '+ self.device_id +' shell pm clear com.fmwhatsapp')
        self.grantPermission("com.fmwhatsapp")
        self.d.app_start('com.fmwhatsapp')

        status = self.checkActivity()

        if status == "com.fmwhatsapp/com.fmwhatsapp.registration.EULA":

            try:
                self.d(text="AGREE AND CONTINUE").click()
                self.d(resourceId="com.fmwhatsapp:id/registration_country").click()
                self.d(resourceId="com.fmwhatsapp:id/menuitem_search").click()
                country = "INDONESIA"
                sleep(1)
                for i in country:
                    self.pressKey(i)
                self.d(text="Indonesia").click()

                for i in phone_num:
                     self.pressKey(i)
                self.d(text="NEXT").click()
            except Exception:
                return False

            # Switching from business
            try:
                self.d(text="SWITCH").click()
            except Exception:
                print("No switch requested")

            i = 0

            while True:
                data_acc = self.heperny.getAccounts()

                checkbydb_columotp = self.heperny.checkSmsOtpColumn(self.pull_id)
                if checkbydb_columotp[4] != None:
                    numberotp = checkbydb_columotp[4]
                    print(numberotp)
                    break
                else:
                    print("Waiting SMS Recive OTP")
                i+=1
                if i > 60:
                    return False
                    break
                sleep(1)
            try:
                print("OTP FOUND "+str(numberotp))
                os.system(f'adb -s '+self.device_id+' shell input text "'+str(numberotp)+'"')
                sleep(1)

                updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                print("Set pullid otp to null")
                print("Success input otp")
            except Exception:
                updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                print("Set pullid otp to null")
                print("Failed input otp")

                # Google permission
            self.d(text="SKIP").click()

            nama = name.upper()
            for i in nama:
                    if i == " ":
                        self.pressKey("SPACE")
                    self.pressKey(i)
            self.d(text="NEXT").click()
            self.d(text="CLOSE").click()
        else:
            self.heperny.updateAccApps(1, "com.fmwhatsapp", self.data_account[0])
            return True

    def registerYo(self, phone_num, name):
        os.system(f'adb -s '+ self.device_id +' shell pm clear com.yowhatsapp')
        self.grantPermission("com.yowhatsapp")
        self.d.app_start('com.yowhatsapp')
            
        status = self.checkActivity()

        if status == "com.yowhatsapp/com.yowhatsapp.registration.EULA":
                try:
            # Front page
                    self.d(text="AGREE AND CONTINUE").click()

                    self.d(resourceId="com.yowhatsapp:id/registration_country").click()
                    self.d(resourceId="com.yowhatsapp:id/menuitem_search").click()
                    country = "INDONESIA"
                    sleep(1)
                    for i in country:
                        self.pressKey(i)
                    self.d(text="Indonesia").click()

                    # Input number
                    self.d(text="phone number").click()
                    for i in phone_num:
                            self.pressKey(i)
                    self.d(text="NEXT").click()
                except Exception:
                    return False
                    
                try:
                    self.d(text="SWITCH").click()
                except Exception:
                    print("There is no switch request")

                # Confirmation
                self.d(text="OK").click()

                i = 0

                while True:
                    data_acc = self.heperny.getAccounts()

                    checkbydb_columotp = self.heperny.checkSmsOtpColumn(self.pull_id)
                    if checkbydb_columotp[4] != None:
                        numberotp = checkbydb_columotp[4]
                        print(numberotp)
                        break
                    else:
                        print("Waiting SMS Recive OTP")
                    i+=1
                    if i > 60:
                        return False
                        break
                    sleep(1)
                try:
                    print("OTP FOUND "+str(numberotp))
                    os.system(f'adb -s '+self.device_id+' shell input text "'+str(numberotp)+'"')
                    sleep(1)


                    updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                    print("Set pullid otp to null")
                    print("Success input otp")
                except Exception:
                    updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                    print("Set pullid otp to null")
                    print("Failed input otp")

                # Google permission request
                self.d(text="SKIP").click()
                nama = name.upper()
                for i in nama:
                     if i == " ":
                          self.pressKey("SPACE")
                     self.pressKey(i)
                self.d(text="NEXT").click()
                self.d(text="CLOSE").click()

        else:
            self.heperny.updateAccApps(1, "com.yowhatsapp", self.data_account[0])
            return True
            
    def registerAero(self, phone_num, name):
        os.system(f'adb -s '+ self.device_id +' shell pm clear com.aero')
        self.grantPermission("com.aero")
        self.d.app_start('com.aero')

        status = self.checkActivity()

        if status == "com.aero/com.aero.registration.EULA":
            try:
                # Front page
                self.d(text="AGREE AND CONTINUE").click()

                self.d(resourceId="com.aero:id/registration_country").click()
                self.d(resourceId="com.aero:id/menuitem_search").click()
                country = "INDONESIA"
                sleep(1)
                for i in country:
                    self.pressKey(i)
                self.d(text="Indonesia").click()

                # Input number
                self.d(text="phone number").click()
                for i in phone_num:
                    self.pressKey(i)
                self.d(text="NEXT").click()
            except Exception:
                return False

            i = 0

            while True:
                data_acc = self.heperny.getAccounts()

                checkbydb_columotp = self.heperny.checkSmsOtpColumn(self.pull_id)
                if checkbydb_columotp[4] != None:
                    numberotp = checkbydb_columotp[4]
                    print(numberotp)
                    break
                else:
                    print("Waiting SMS Recive OTP")
                i+=1
                if i > 60:
                    return False
                    break
                sleep(1)
            try:
                print("OTP FOUND "+str(numberotp))
                os.system(f'adb -s '+self.device_id+' shell input text "'+str(numberotp)+'"')
                sleep(1)


                updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                print("Set pullid otp to null")
                print("Success input otp")
            except Exception:
                updatemspull = self.heperny.updateSmspullOtp(None, self.pull_id)
                print("Set pullid otp to null")
                print("Failed input otp")

            try:
                self.d(text="SWITCH").click()
            except:
                print("No switch requested")
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

        else:
            self.heperny.updateAccApps(1, "com.aero", self.data_account[0])
            return True

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
        a = self.adbs(f'adb -s '+ self.device_id +' shell dumpsys activity activities | grep -E "mCurrentFocus"')
        b = a.split()[2][:-1]
        c = b.split("/")[1]
        return b

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