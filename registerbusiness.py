import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")
device_id = "R9CT4007GBM"
packagename = "com.whatsapp"

def frontPage(phone_num, name):
    # For Original Whatsapp and Whatsapp Business
    try:
        d(text="English").click()
    except Exception:
        print("No need to choose language")
    finally:
        d(text="AGREE AND CONTINUE").click()
        d(text="USE A DIFFERENT NUMBER").click()
        for i in phone_num:
            helper.pressKey(i)
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
                helper.pressKey("SPACE")
            helper.pressKey(i)
        d.click(990, 988)

        category = "other business"
        kategori = category.upper()
        for i in kategori:
            if i == " ":
                helper.pressKey("SPACE")
            helper.pressKey(i)

        d(text="Other Business").click()
        d(text="NEXT").click()
        d(text="NOT NOW").click()

def mainFunction():
    frontPage("895410808876", "Carlo Vigano")