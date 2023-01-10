import uiautomator2 as u2 
from xml.dom import minidom
from time import sleep
import helper
import os
import time
import sys

device_id = "R9CT300FQRE"
d = u2.connect(device_id)

def installPackages(device_id):
    os.system(f'adb -s ' + device_id + ' install apk/com.whatsapp.apk')
    os.system(f'adb -s ' + device_id + ' install apk/com.whatsapp.w4b.apk')
    os.system(f'adb -s ' + device_id + ' install apk/com.aero.apk')
    os.system(f'adb -s ' + device_id + ' install apk/com.yowhatsapp.apk')
    os.system(f'adb -s ' + device_id + ' install apk/com.fmwhatsapp.apk')

def uninstallPackages(device_id):
    os.system(f'adb -s ' + device_id + ' uninstall com.whatsapp')
    os.system(f'adb -s ' + device_id + ' uninstall com.whatsapp.w4b')
    os.system(f'adb -s ' + device_id + ' uninstall com.aero')
    os.system(f'adb -s ' + device_id + ' uninstall com.yowhatsapp')
    os.system(f'adb -s ' + device_id + ' uninstall com.fmwhatsapp')

def makeConnection(device_id, wifiName, security, password):
    os.system(f'adb -s '+ device_id +' shell cmd -w wifi connect-network '+ wifiName + ' '+ security + ' '+ password)

def resetConnection(device_id):
    os.system(f'adb -s '+ device_id +' shell am start -n "com.android.settings/.Settings"')
    os.system(f'adb -s '+ device_id +' shell input swipe 500 2000 500 100')
    sleep(1)
    os.system(f'adb -s '+ device_id +' shell input tap 500 900')
    sleep(1)
    os.system(f'adb -s '+ device_id +' shell input tap 500 2150')
    sleep(1)
    d(text="Reset netowrk settings").click()
    sleep(2)
    d(text="Reset settings").click()
    sleep(2)
    d(text="Reset").click()
    sleep(3)
    pressKey("HOME")

def grantPermission(device_id, packageName):
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.READ_CALL_LOG')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.ACCESS_FINE_LOCATION')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.ANSWER_PHONE_CALLS')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.RECEIVE_SMS')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.READ_EXTERNAL_STORAGE')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.ACCESS_COARSE_LOCATION')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.READ_PHONE_STATE')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.SEND_SMS')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.CALL_PHONE')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.WRITE_CONTACTS')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.CAMERA')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.GET_ACCOUNTS')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.WRITE_EXTERNAL_STORAGE')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.RECORD_AUDIO')
        os.system(f'adb -s '+ device_id +' shell pm grant '+ packageName +' android.permission.READ_CONTACTS')

def setLanguage(device_id):
    os.system("adb -s " + device_id + " shell am start -a android.settings.LOCALE_SETTINGS")
    print("In the menu")
    try:
        d(text="English (United States)").click()
        d(text="Terapkan").click()
    except Exception:
        print("No English option")
        try:
            print("Adding language")
            d(text="Tambah bahasa").click()
            d(text="English").click()
            d(text="United States").click()
            d(text="Atr sbg default").click()
        except Exception:
            print("Already in English")
            return 

# <<========================================================>>

if sys.argv[1] == "install":
    try:
        installPackages(sys.argv[2])
    except:
        print("Install Failed")
    sys.exit()


elif sys.argv[1] == "uninstall":
    try:
        uninstallPackages(sys.argv[2])
        print("Uninstall Successful")
    except:
        print("Uninstall Failed")
    sys.exit()


elif sys.argv[1] == "connect":
    try:
        makeConnection(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        print("Connect Successful")
    except:
        print("Connect Failed")
    sys.exit()


elif sys.argv[1] == "reset":
    try:
        resetConnection(sys.argv[2])
        print("Reset connection Successful")
    except:
        print("Reset connection failed")
    sys.exit()

elif sys.argv[1] == "grant":
    try:
        grantPermission(sys.argv[2], sys.argv[3])
        print("Grant Successful")
    except:
        print("Set language Failed")
    sys.exit()

elif sys.argv[1] == "language":
    try:
        setLanguage(sys.argv[2])
        print("Set language Successful")
    except:
        print("Set language Failed")
    sys.exit()

