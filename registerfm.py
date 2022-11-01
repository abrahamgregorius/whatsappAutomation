import os
import uiautomator2 as u2
import helper


device_id = "R9CT4007GBM"

d = u2.connect(device_id)


def frontPage(phone_num, name):
     try:
          # Allow access media
          d(text="Allow").click()
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
                    helper.pressKey("SPACE")
               helper.pressKey(i)
          d(text="NEXT").click()
          d(text="CLOSE").click()
          
def mediaPermission():
     d(text="SETTINGS").click()
     d(text="Permissions").click()
     os.system(f'adb -s' + device_id + ' shell input swipe 550 1690 550 970')
     d(text="Files and media").click()
     d(resourceId="com.android.permissioncontroller:id/allow_radio_button")

          
# frontPage("895410810680", "Carlo Vigano")
