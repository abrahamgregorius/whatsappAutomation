import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")
device_id = "R9CT4007GBM"
packagename = "com.whatsapp"

def frontPage(phone_num):
    # For Original Whatsapp and Whatsapp Business
    try:
        d(text="English").click()
    except Exception:
        print("No need to choose language")
    finally:
        d(text="AGREE AND CONTINUE").click()
        for i in phone_num:
            helper.pressKey(i)
        d(text="NEXT").click()
        d(text="OK").click()

def contactMediaPerm():
    if d(text="Contacts and media").get_text().split()[0] == "Contacts":
         d(text="CONTINUE").click()
    d(text="Allow").click()
    d(text="Allow").click()

def drivePerm():
     if d(resourceId="android:id/message").get_text().split()[0] == "If":
        d(text="SKIP").click()

def profileSetup(name):
    d.click(280, 915)
    nama = name.upper()
    for i in nama:
        if i == " ":
            helper.pressKey("SPACE")
        helper.pressKey(i)

    d(text="NEXT").click()

def mainFunction():
    frontPage("895410810680")
    contactMediaPerm()
    drivePerm()
    profileSetup("Carlo Vigano")

mainFunction()  