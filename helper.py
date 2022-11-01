import os
import random
import requests
import uiautomator2 as u2

device_id = "R9CT4007GBM"
d = u2.connect(device_id)
packagename = "com.whatsapp"


response = requests.get("https://names.drycodes.com/1?combine=2&nameOptions=boy_names")
names = response.json()

def generateAPassword():
    for i in names:
        res = i
        return res

def generateFirstName():
    for i in names:
        res = i.split('_')[0]
        return res

def generateLastName():
    for i in names:
        res = i.split('_')[1]
        return res

def generatePassword():
    for i in names:
        res = i
        return res

def pressKey(keycode):
    os.system(f'adb -s '+ device_id +' shell input keyevent KEYCODE_' + keycode)

def pressSend():
    os.system(f'adb -s ' + device_id + ' shell input tap 985 2230') 

    
def randomMonth():
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

def randomDay():
    day = random.randrange(1, 28, 1)
    return day

def randomYear():
    year = random.randrange(1975, 1999, 1)
    return year

def randomGender():
    genderCoordinates = {
        "m":"255 750",
        "f":"255 650"
    }
    res = random.choice(list(genderCoordinates.values()))
    return res

def generateNumber(arr):
    a = []
    for i in arr:
        a.append(i[0])
    number = random.choice(a)
    return number

def generatePackageName(arr):
    b = []
    for i in arr:
        b.append(i[1])
    package = random.choice(b)
    return package

def registerWhatsapp(phone_num, name):
    try:
        d(text="English").click()
    except Exception:
        print("No need to choose language")
    finally:
        d(text="AGREE AND CONTINUE").click()
        for i in phone_num:
            pressKey(i)
        d(text="NEXT").click()
        d(text="OK").click()

    if d(text="Contacts and media").get_text().split()[0] == "Contacts":
         d(text="CONTINUE").click()
    d(text="Allow").click()
    d(text="Allow").click()

    if d(resourceId="android:id/message").get_text().split()[0] == "If":
       d(text="SKIP").click()

    d.click(280, 915)
    nama = name.upper()
    for i in nama:
        if i == " ":
            pressKey("SPACE")
        pressKey(i)

    d(text="NEXT").click()

def registerBusiness(phone_num, name):
    # For Original Whatsapp and Whatsapp Business
    try:
        d(text="English").click()
    except Exception:
        print("No need to choose language")
    finally:
        d(text="AGREE AND CONTINUE").click()
        d(text="USE A DIFFERENT NUMBER").click()
        for i in phone_num:
            pressKey(i)
        d(text="NEXT").click()
        d(text="CONTINUE").click()

        d(text="CONTINUE").click()
        d(text="Allow").click()
        d(text="Allow").click()
        d(text="SKIP").click()
        d.click(300, 840)

        nama = name.upper()
        for i in nama:
            if i == " ":
                pressKey("SPACE")
            pressKey(i)
        d.click(990, 988)

        category = "other business"
        kategori = category.upper()
        for i in kategori:
            if i == " ":
                pressKey("SPACE")
            pressKey(i)

        d(text="Other Business").click()
        d(text="NEXT").click()
        d(text="NOT NOW").click()

def registerFm(phone_num, name):
    try:
        # Allow access media
        d(text="Allow").click()
    except:
        print("There is no permission request")
    finally:
        # Front page
        d(text="AGREE AND CONTINUE").click()
        # Input number
        d(text="phone number").click()
        for i in phone_num:
             pressKey(i)
        d(text="NEXT").click()
     
     # Switching from business
    try:
        d(text="SWITCH").click()
    except:
        print("No switch requested")
    finally:
        d(text="CONTINUE").click()
        d(text="Allow").click()   
        # Contacts and media permission
        d(text="CONTINUE").click()
        d(text="Allow").click()

          # Google permission
        d(text="SKIP").click()
          
        nama = name.upper()
        for i in nama:
             if i == " ":
                  pressKey("SPACE")
             pressKey(i)
        d(text="NEXT").click()
        d(text="CLOSE").click()

def registerYo(phone_num, name):
    try:
          # Allow access media
          d(text="Allow").click()
    except:
        print("There is no permission request")
    finally:
        # Front page
        d(text="AGREE AND CONTINUE").click()
        # Input number
        d(text="phone number").click()
        for i in phone_num:
             pressKey(i)
        d(text="NEXT").click()
    try:
        d(text="SWITCH").click()
    except:
        print("There is no switch request")
    finally:
        # Confirmation
        d(text="OK").click()
        # Verify hanya 7 jam sekali
        d(text="CONTINUE").click()
        d(text="Allow").click()
          
          # Contacts and media permission
        d(text="CONTINUE").click()
        d(text="Allow").click()
        
        # Google permission request
        d(text="SKIP").click()
        nama = name.upper()
        for i in nama:
             if i == " ":
                  pressKey("SPACE")
             pressKey(i)
        d(text="NEXT").click()
        d(text="CLOSE").click()
        
def registerAero(phone_num, name):
    # In development
    pass 

def mediaPermissionFm():
     d(text="SETTINGS").click()
     d(text="Permissions").click()
     os.system(f'adb -s' + device_id + ' shell input swipe 550 1690 550 970')
     d(text="Files and media").click()
     d(resourceId="com.android.permissioncontroller:id/allow_radio_button")



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