import uiautomator2 as u2
import helper

d = u2.connect("R9CT4007GBM")


def frontPage(phone_num):
    if d(text="To restore from backup, allow WhatsApp access to your device's photos, media, and files. Tap Settings > Permissions, and turn Storage on").get_text().split()[0] == "To":
         d(text="NOT NOW").click()
    if d(text="Allow FMWhatsApp to access photos, media, and files on your device?").get_text().split()[0] == "Allow":
         d(text="Allow").click()
    if d(text="Welcome to WhatsApp").get_text().split()[0] == "Welcome":
         d(text="AGREE AND CONTINUE").click()

    d(text="phone number").click()
    for i in phone_num:
        helper.pressKey(i)
    d(text="NEXT").click()
    d(text="OK").click()
    
    if d(text="To easily verify your number, WhatsApp can automatically detect WhatsApp to view SMS messages.").get_text().split()[0] == "To":
         d(text="CONTINUE").click()
    
    d(text="Allow").click()

frontPage("85811403649")