import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")


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
          

frontPage("895410810680", "Carlo Vigano")