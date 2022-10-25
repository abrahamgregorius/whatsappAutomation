import os
import helper
from time import sleep
import subprocess
import uiautomator2 as u2

d = u2.connect("R9CT4007GBM")
device_id = "R9CT4007GBM"
phone_num = "87815494888"
packagename = "com.whatsapp"

def chooseLanguage():
    os.system(f'adb -s ' + device_id + ' shell input tap 525 1023')
    os.system(f'adb -s ' + device_id + ' shell input tap 955 2155')

def frontPageLanguage():
    chooseLanguage()
    status = os.system(f'adb -s R9CT4007GBM shell dumpsys window | findstr "mCurrentFocus"')
    if status == " mCurrentFocus=Window{23d25ab u0 com.whatsapp/com.whatsapp.registration.EULA}":
        os.system(f'adb -s ' + device_id + ' shell input tap 650 1660') 
        os.system(f'adb -s ' + device_id + ' shell input tap 515 600')
        for i in phone_num:
            helper.pressKey(i)
        os.system(f'adb -s ' + device_id + ' shell input tap 530 1250')
    else:
        return
def frontPage():
    # Selamat datang di whatsapp
    os.system(f'adb -s ' + device_id + ' shell input tap 515 2060')
    # Klik nomor telponnya
    os.system(f'adb -s ' + device_id + ' shell input tap 515 600')
    # Masukkan nomor telepon
    for i in phone_num:
        helper.pressKey(i)
    # Check ada perlu pencet oke atau tidak
        # Pengecekan
    proc = subprocess.Popen('adb -s R9CT4007GBM shell dumpsys window | findstr "mFocusedApp"', stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    data = str(out.decode("utf-8"))
    print("proc = " + data)
    while "com.whatsapp/.registration.VerifyPhoneNumber" in data:
        print("Masuk bro")
        break
        # Kondisi
    if proc == "mFocusedApp=ActivityRecord{4f59308 u0 com.whatsapp/.registration.RegisterPhone t361}":
        # Klik oke
        os.system(f'adb -s ' + device_id + ' shell input tap 889 1370')
    else:
    # Klik lanjutkan    
        os.system(f'adb -s ' + device_id + ' shell input tap 530 1250')

        
def contactMediaPerm():
    status = os.system(f'adb -s R9CT4007GBM shell dumpsys window | findstr "mCurrentFocus"')
    if status == "mCurrentFocus=Window{b356581 u0 com.whatsapp/com.whatsapp.RequestPermissionActivity}":
        # Klik lanjut
        os.system(f'adb -s ' + device_id + ' shell input tap 755 1585')
        # Pengecekan
        status = os.system(f'adb -s R9CT4007GBM shell dumpsys window | findstr "mCurrentFocus"')
        if status == "mCurrentFocus=Window{6734374 u0 com.google.android.permissioncontroller/com.android.permissioncontroller.permission.ui.GrantPermissionsActivity}":
            # Klik izinkan kontak
            os.system(f'adb -s ' + device_id + ' shell input tap 535 1980')
            # Pengecekan 
            status = os.system(f'adb -s R9CT4007GBM shell dumpsys window | findstr "mCurrentFocus"')
            if status == "mCurrentFocus=Window{6734374 u0 com.google.android.permissioncontroller/com.android.permissioncontroller.permission.ui.GrantPermissionsActivity}":
                # Klik izinkkan media
                os.system(f'adb -s ' + device_id + ' shell input tap 535 1980')

def drivePerm():
    # Klik lewati
    os.system(f'adb -s ' + device_id + ' shell input tap 645 1360')

def profileSetup(name):
    # Klik input nama
    os.system(f'adb -s ' + device_id + ' shell input tap 530 900')
    # Input nama
    nama = [*name.upper()]
    for i in nama:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)
    # Klik lanjut
    os.system(f'adb -s ' + device_id + ' shell input tap 525 1300')

def mainFunction():
    frontPage()
    #contactMediaPerm()
    #drivePerm()
    #profileSetup('Justin Timberlake')

mainFunction()