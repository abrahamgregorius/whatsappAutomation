import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")
device_id = "R9CT4007GBM"
phone_num = "87815494888"
packagename = "com.whatsapp"

def frontPage():
    if d(text="Selamat datang di WhatsApp").get_text().split()[0] == "Selamat":
            d(resourceId="com.whatsapp:id/eula_accept").click()
    d(resourceId="com.whatsapp:id/registration_phone").click()
    for i in phone_num:
        helper.pressKey(i)
    d(text="LANJUT").click()
    d(text="OKE").click()

def contactMediaPerm():
    if d(text="Kontak dan media").get_text().split()[0] == "Kontak":
         d(text="LANJUT").click()
    d(text="Izinkan").click()
    d(text="Izinkan").click()

def drivePerm():
     if d(resourceId="android:id/message").get_text().split()[0] == "Jika":
         d(text="LEWATI").click()

def profileSetup(name):
    d.click(280, 915)
    nama = name.upper()
    for i in nama:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)

    d(text="LANJUT").click()

def mainFunction():
    frontPage()
    contactMediaPerm()
    drivePerm()
    profileSetup("Carlo Vigano")

mainFunction()