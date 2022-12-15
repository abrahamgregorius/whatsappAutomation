import uiautomator2 as u2 
from xml.dom import minidom
from time import sleep
import helper

d = u2.connect("R9CT300FQRE")
helpernya = helper.AutoHelper()


d(resourceId="com.whatsapp.w4b:id/registration_name").click()
d(resourceId="com.whatsapp.w4b:id/registration_name").clear_text()
nama = "anjay mabar".upper()
for i in nama:
    if i == " ":
        helpernya.pressKey("SPACE")
    helpernya.pressKey(i)
d.click(990, 988)

category = "other"
kategori = category.upper()

d(resourceId="com.whatsapp.w4b:id/search_src_text").click()
d(resourceId="com.whatsapp.w4b:id/search_src_text").clear_text()

for i in kategori:
    if i == " ":
        helpernya.pressKey("SPACE")
    helpernya.pressKey(i)

sleep(1.5)

d(text="Other Business").click()
d(text="Other Business").click()

