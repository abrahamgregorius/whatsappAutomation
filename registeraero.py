import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")


def frontPage(phone_num, name):
     try:
          # Allow access media
          d(text="NOT NOW").click()
          pass
     except Exception:
          print("There is no permission request")
     finally:
          # Front page
          d(text="AGREE AND CONTINUE").click()
          # Input number
          d(text="phone number").click()
          for i in phone_num:
               helper.pressKey(i)
          d(text="NEXT").click()
     try:
          d(text="SWITCH").click()
     except:
          print("No switch requested")
     finally:
          # Confirmation
          d(text="OK").click()
          # Verify hanya 7 jam sekali
          d(text="CONTINUE").click()
          d(text="Allow").click()
          
          nama = name.upper()
          for i in nama:
               if i == " ":
                    helper.pressKey("SPACE")
               helper.pressKey(i)
          d(text="NEXT").click()
          d(text="THANKS!")

# frontPage("895410808875", "Carlo Vigano")