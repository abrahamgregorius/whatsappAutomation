import os
import random
from time import sleep
import time
import requests
import uiautomator2 as u2
import subprocess
import sqlite3
import helpers as helpers
import namegenerator
from lxml import html
import requests

class AutoHelper:

    def __init__(self, device_id, phone_number, phone_name, pull_id =0, acc_id =0):
        self.device_id = device_id
        self.phone_number = phone_number
        self.heperny = helpers.QueryHelp(device_id,1)
        self.d = u2.connect(device_id)
        self.phone_name = phone_name
        self.pull_id = pull_id
        self.data_account = self.heperny.checkAccountReady(device_id)


    def adbs(self, command):
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, _) = proc.communicate()
        print(out)
        return out.decode('utf-8')
    def adb(self, command):
    
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, _) = proc.communicate()
        return out.decode('utf-8')


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
    def setLanguage(self):
        os.system("adb -s " + self.device_id + " shell am start -a android.settings.LOCALE_SETTINGS")
        print("In the menu")
        try:
            self.d(text="English (United States)").click()
            self.d(text="Terapkan").click()
        except Exception:
            print("No English option")
        try:
            self.d(text="Tambah bahasa").click()
            self.d(text="English").click()
            self.d(text="United States").click()
            self.d(text="Atr sbg default").click()
        except:
            print("Already in English")
            return

    def pressKey(self, keycode):
        os.system(f'adb -s '+ self.device_id +' shell input keyevent KEYCODE_' + keycode)

    def pressSend(self):
        os.system(f'adb -s ' + self.device_id + ' shell input tap 985 2230') 

    def clearApp(self, packageName):
        os.system(f'adb -s {self.device_id} shell pm clear {packageName}')

    def resetWifiConnection(self):
        try:
            os.system(f'adb -s '+ self.device_id +' shell am start -n "com.android.settings/.Settings"')
        except:
            print("Failed")
        sleep(1)
        
        try:
            os.system(f'adb -s '+ self.device_id +' shell input swipe 500 2200 500 100') # Swipe kebawah
        except:
            print("Failed")
        sleep(1)
        
        try:
            self.d(text="General management").click() # General management 
        except:
            print("Failed")        
        sleep(0.7)
        
        try:
            self.d(text="Reset").click() # Reset 
        except:
            print("Failed")        
        sleep(0.7)
        
        try:
            self.d(text="Reset network settings").click() # Reset network settings 
        except:
            print("Failed")        
        sleep(0.1)
        
        try:
            self.d(resourceId="com.android.settings:id/initiate_reset_network").click() # Reset settings 
        except:
            print("Failed")        
        sleep(0.7)
        
        try:
            self.d(resourceId="com.android.settings:id/execute_reset_network").click() # Reset
        except:
            print("Failed")            

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

    def errorHandling(self, device_id, package_name, error_code, error_note):
            url = "172.16.0.98:5050/api/error_change"

            payload={'device_id': device_id,
            'package_name': package_name,
            'error_code': error_code,
            'error_note': error_note}
            files=[

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)

            print(response.text)

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

    def dumpUi(self, device_id):
        currentTime = time.ctime().split(" ")[3].replace(":", "_")
        os.system(f'adb -s '+ device_id +' shell uiautomator dump --compressed /sdcard/' + device_id + "_" + currentTime + '.xml ')
        print(currentTime)
        sleep(1)
        os.system(f'adb -s '+ device_id +' pull /sdcard/' + device_id + "_" + currentTime + '.xml  /home/pony/WORKON/appium-farming/uidump/' + device_id + currentTime + '.xml')
        print(currentTime)

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

    def makeConnection(self, name, security, password):
        os.system(f'adb -s '+ self.device_id +' shell cmd -w wifi connect-network '+ name + ' '+ security + ' '+ password) 

    def resetConnection(self):
        os.system(f'adb -s '+ self.device_id +' shell am start -n "com.android.settings/.Settings"')
        os.system(f'adb -s '+ self.device_id +' shell input swipe 500 2200 500 100')
        self.d.implicitly_wait(3)
        sleep(3)
        os.system(f'adb -s '+ self.device_id +' shell input tap 500 900')
        os.system(f'adb -s '+ self.device_id +' shell input tap 500 2150')
        os.system(f'adb -s '+ self.device_id +' shell input tap 500 580')
        os.system(f'adb -s '+ self.device_id +' shell input tap 500 600')
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

    def checkDialog(self):
        text = self.d(resourceId="android:id/message").get_text()
        return text

    def registerWhatsapp(self, phone_num, name):
        # Granting permission and starting app
        try:
            self.grantPermission("com.whatsapp")
            self.d.app_start("com.whatsapp")
            print("Permission granted and started app")
            self.errorHandling(self.device_id, "com.whatsapp", "1", "Permission granted and started app")
        except:
            print("Permission not granted and app not started")
            self.errorHandling(self.device_id, "com.whatsapp", "-1", "Permission not granted and app not started")


        
        # English option
        try:
            self.d(resourceId="com.whatsapp:id/next_button").click()
            print("Clicked next button")
            self.errorHandling(self.device_id, "com.whatsapp", "2", "Clicked next button")
        except Exception:
            print("No need to choose language or no next button")
            self.errorHandling(self.device_id, "com.whatsapp", "-2", "No need to choose language or no next button")



        # Agree and continue
        try:    
            self.d(text="AGREE AND CONTINUE").click()
            print("Clicked AGREE AND CONTINUE")
            self.errorHandling(self.device_id, "com.whatsapp", "3", "Clicked AGREE AND CONTINUE")
        except:
            print("Failed clicking AGREE AND CONTINUE")
            self.errorHandling(self.device_id, "com.whatsapp", "-3", "Failed clicking AGREE AND CONTINUE")
        
            
            
        # Clicking country picker and search bar
        try:
            self.d(resourceId="com.whatsapp:id/registration_country").click()
            self.d(resourceId="com.whatsapp:id/menuitem_search").click()
            print("Clicked country picker and search bar")
            self.errorHandling(self.device_id, "com.whatsapp", "4", "Clicked country picker and search bar")
        except:
            print("Failed clicking country picker and search bar")
            self.errorHandling(self.device_id, "com.whatsapp", "-4", "Failed clicking country picker and search bar")

        # Choosing INDONESIA
        try:
            country = "INDONESIA"
            sleep(1)
            for i in country:
                self.pressKey(i)
            self.d(text="Indonesia").click()
            print("Success choosing Indonesia")
            self.errorHandling(self.device_id, "com.whatsapp", "5", "Success choosing Indonesia")
        except:
            print("Failed choosing Indonesia")
            self.errorHandling(self.device_id, "com.whatsapp", "-5", "Failed choosing Indonesia")

        
        # Typing phone number
        sleep(5)
        try:
            for i in phone_num:
                self.pressKey(i)
            self.d(text="NEXT").click()
            print("Success clicking phone number")
            self.errorHandling(self.device_id, "com.whatsapp", "6", "Inputted phone number")
        except:
            print("Failed clicking phone number")
            self.errorHandling(self.device_id, "com.whatsapp", "-6", "Failed inputting phone number")
        

        # Switching request
        try:
            self.d(text="SWITCH").click()
            print("Clicked SWITCH")
            self.errorHandling(self.device_id, "com.whatsapp", "7", "Clicked SWITCH")
        except Exception:
            print("No switch requested or failed clicking switch")
            self.errorHandling(self.device_id, "com.whatsapp", "-7", "No switch requested or failed clicking SWITCH")


        # Clicking OK
        try:
            self.d(text="OK").click()
            print("Clicked OK")
            self.errorHandling(self.device_id, "com.whatsapp", "8", "Clicked OK")
        except Exception:
            print("No OK button")
            self.errorHandling(self.device_id, "com.whatsapp", "-8", "No OK button or failed clicking OK")
        sleep(10)
 
    
        # <===========================OTP===========================>
    
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

            updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
            print("Set pullid otp to null")
            print("Success input otp")
            self.errorHandling(self.device_id, "com.whatsapp", "9", "Inputted OTP")
        except Exception:
            updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
            print("Set pullid otp to null")
            print("Failed input otp")
            self.errorHandling(self.device_id, "com.whatsapp", "-9", "Failed inputting OTP")

        # <========================POST-OTP=========================>

        # Clicking OK
        try:
            self.d(text="OK").click()
            print("Clicked OK")
            self.errorHandling(self.device_id, "com.whatsapp", "10", "Clicked OK")
            sleep(1)
        except:
            print("Failed clicking OK")
            self.errorHandling(self.device_id, "com.whatsapp", "-10", "Failed clicking OK")
        
        
        # Clicking SKIP
        try: 
            self.d(text="SKIP").click()
            print("Success clicking skip")
            self.errorHandling(self.device_id, "com.whatsapp", "11", "Clicked skip")
        except Exception:
            print("Failed clicking skip")
            self.errorHandling(self.device_id, "com.whatsapp", "-11", "Failed clicking skip")

    
        # Registering name
        try:
            self.d.click(280, 900)
            nama = name.upper()
            for i in nama:
                if i == " ":
                    self.pressKey("SPACE")
                self.pressKey(i)
            print("Inputted name")
            self.errorHandling(self.device_id, "com.whatsapp", "12", "Inputted name")
        except:
            print("Failed typing name")
            self.errorHandling(self.device_id, "com.whatsapp", "-12", "Failed inputting name")


        # Clicking NEXT
        try:
            self.d(text="NEXT").click()
            self.heperny.updateAccAppsPullid(1, self.pull_id, self.pull_id, "com.whatsapp", self.data_account[0])
            print("Clicked NEXT")
            return True
            self.errorHandling(self.device_id, "com.whatsapp", "13", "Clicked NEXT")
        except:
            print("Failed input name")
            return False
            self.errorHandling(self.device_id, "com.whatsapp", "-13", "Failed clicking NEXT")

    def registerBusiness(self, phone_num, name):
        execute=0
        maxexecute = 2
        condition = 0
        register_position = 0
        while True:
            print("PERCOBAAN KE - "+str(execute))
            if execute == maxexecute and maxexecute > 0:
                return False
                break
            if phone_num != None:
                try:
                    self.grantPermission("com.whatsapp.w4b")
                    print("Success Grant Permission and Next Open Whatsapp")
                    register_position = 1
                except:
                    print("Next Step open Whatsapp")
                    register_position = -1
                    pass
                self.d.app_start('com.whatsapp.w4b')
                print("Success Open APP Wa")

                status = self.checkActivity()
                print("Get Check Activity")
                
                if status == "com.whatsapp.HomeActivity":
                    self.heperny.updateAccAppsPullid(1, self.pull_id, self.pull_id, "com.whatsapp.w4b", self.data_account[0])
                    return False
                    break
                if status == "com.whatsapp.registration.EULA" or status != "com.whatsapp.HomeActivity" or status == null:
                    self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)


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

                # <===========================OTP===========================>

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
                    
                # <========================POST-OTP=========================>

                # Google Backup
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
                    url = "http://ninjaname.horseridersupply.com/indonesian_name.php?number_generate=1&gender_type=male&submit=Generate"

                    payload={
                        'number_generate': '1',
                        'gender_type': 'male',
                        'submit': 'Generate'
                    }
                    headers = {
                        'number_generate': '1',
                        'gender_type': 'male',
                        'submit': 'Generate'
                    }

                    a = requests.request("POST", url,headers=headers, data=payload)
                    get = html.fromstring(a.text)
                    nama = get.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]//text()')
                    genertname = nama[0].replace("• ", "")
                    nama = genertname.upper()
                    for i in nama:
                        if i == " ":
                            self.pressKey("SPACE")
                        self.pressKey(i)
                except:
                    print("Failed input name")

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
                status_reg=1
                self.heperny.updateAccAppsPullid(status_reg, self.pull_id, self.pull_id, "com.whatsapp.w4b", self.data_account[0])
                return True
                break
            except:     
                print("Not now error")
                return False
                break
            execute+=1
            sleep(1)

    
    def registerFm(self, phone_num, name):
        # Granting permission and starting app
        self.grantPermission("com.fmwhatsapp")
        self.d.app_start('com.fmwhatsapp')
        print("Granted permissions and started app")
        
        # status = self.checkActivity()
        status = "com.fmwhatsapp/com.fmwhatsapp.registration.EULA"
        print("RegisterFMWhatsapp starting...")
        if status == "com.fmwhatsapp/com.fmwhatsapp.registration.EULA":

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
            

            # Switching from business
            try:
                self.d(text="SWITCH").click()
            except Exception:
                print("No switch requested")

            # <===========================OTP===========================>

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

                updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
                print("Set pullid otp to null")
                print("Success input otp")
            except Exception:
                updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
                print("Set pullid otp to null")
                print("Failed input otp")
                
                
            # <========================POST-OTP=========================>

            # Google permission
            try:
                self.d(text="SKIP").click()
            except:
                print("No SKIP button")


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
                print("Failed inputting name")
            
            # Clicking NEXT
            try:
                self.d(text="NEXT").click()
            except:
                print("No NEXT button")
            
            # Clicking CANCEL
            try:
                self.d(text="CANCEL").click()
            except:
                print("No CANCEL button")
            
            # Clicking CLOSE
            try:
                self.d(text="CLOSE").click()
            except:
                print("No NEXT button")
                
                
            self.heperny.updateAccAppsPullid(1, self.pull_id, self.pull_id, "com.fmwhatsapp", self.data_account[0])
        else:
            self.heperny.updateAccApps(1, "com.fmwhatsapp", self.data_account[0])
            return True

    def registerYo(self, phone_num, name):
        # Granting permission and starting app
        try:
            self.grantPermission("com.yowhatsapp")
            self.d.app_start('com.yowhatsapp')
            # self.adb("adb -s "+self.device_id+" shell am start -n com.yowhatsapp.Main")
            print("Permission granted and started app")
        except:
            print("Permission not granted and app is not started")

        status = "com.yowhatsapp/com.yowhatsapp.registration.EULA"
        print("RegisterYoWhatsapp starting...")
        if status == "com.yowhatsapp/com.yowhatsapp.registration.EULA":

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
            
            # <===========================OTP===========================>
            
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


                updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
                print("Set pullid otp to null")
                print("Success input otp")
            except Exception:
                updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
                print("Set pullid otp to null")
                print("Failed input otp")

            # <========================POST-OTP=========================>

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
            
            self.heperny.updateAccAppsPullid(1, self.pull_id, self.pull_id, "com.yowhatsapp", self.data_account[0])        
        else:
            self.heperny.updateAccApps(1, "com.yowhatsapp", self.data_account[0])
            return True
            
    def registerAero(self, phone_num, name):
        # Granting permission and starting app
        try:
            self.grantPermission("com.aero")
            self.d.app_start("com.aero")
            # self.adb("adb -s "+self.device_id+" shell am start -n com.aero.Main")
            print("Permission granted and app started")
        except: 
            print("Permission not granted and app not started")


        status = "com.aero/com.aero.registration.EULA"
        print("RegisterWhatsappAero starting...")
        if status == "com.aero/com.aero.registration.EULA":

            # AGREE AND CONTINUE
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

            # <===========================OTP===========================>
            
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


                updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
                print("Set pullid otp to null")
                print("Success input otp")
            except Exception:
                updatemspull = self.heperny.updateSmspullOtp(None, self.device_id, self.pull_id)
                print("Set pullid otp to null")
                print("Failed input otp")


            # <=======================POST-OTP=======================>

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

            self.heperny.updateAccAppsPullid(1, self.pull_id, self.pull_id, "com.aero", self.data_account[0])
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
        try:
            a = self.adbs(f'adb -s '+ self.device_id +' shell dumpsys activity activities | grep mCurrentFocus')
            b = a.split()[2][:-1]
            c = b.split("/")[1]
            return c
        except:
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
        # Buka chatroom whatsapp
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=62'+ phone_num + '" ' + packageName)
        sleep(3)
        os.system(f'adb -s '+ self.device_id +' shell input tap 900 190')
        self.d(text="CALLz").click()
        # try:
        #     d(text="CONTINUE").click()
        #     d(text="While using the app").click()
        #     d(text="CONTINUE").click()
        #     d(text="Allow").click()
        # finally:
        os.system(f'adb -s '+ self.device_id +' shell input tap 900 190')
        
    def resetAdb(self):
        os.system(f'adb kill-server')
        sleep(15)
        os.system(f'adb start-server')