import os
import helper
from time import sleep
import subprocess
import uiautomator2 as u2

d = u2.connect("R9CT4007GBM")
device_id = "R9CT4007GBM"
phone_num = "87815494888"
packagename = "com.whatsapp"

proc = subprocess.Popen('adb -s R9CT4007GBM shell dumpsys window | findstr "mFocusedApp"', stdout=subprocess.PIPE, shell=True)
(out, _) = proc.communicate()
data = str(out.decode("utf-8"))
print(data)
first = data.split('{', 1)[1]
datafix = first.split(' ',2)[0]
print(datafix)

def frontPageLanguage():
    try:
        d(text="Bahasa Indonesia", resourceId="com.whatsapp:id/language_name")
    except:
        print("Gak ketemu")
    else:
        if d(resourceId="com.whatsapp:id/language_picker").get_text().split()[0] == "Bagikan":
            d(text="SETUJU DAN LANJUTKAN", resourceId="com.whatsapp:id/eula_accept").click()
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
    # Pencet lanjut
    os.system(f'adb -s ' + device_id + ' shell input tap 540 1230')
        
    # Check ada perlu pencet oke atau tidak
        # Pengecekan
   
    while True:
        # if data == "mFocusedApp=ActivityRecord{ "+ datafix +" u0 com.whatsapp/.registration.RegisterPhone t397}":
        #     os.system(f'adb -s ' + device_id + ' shell input tap 885 1390')
        #     break

        try:
            # d(resourceId="android:id/message").get_text().split()[0] == "Anda"
            d(text="OKE", resourceId="android:id/button1").click()
            sleep(5)
        except:
            print("gagal cok")
             
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
    frontPageLanguage()
    contactMediaPerm()
    drivePerm()
    profileSetup('Justin Timberlake')

# mainFunction()