import uiautomator2 as u2

d = u2.connect("R9CT4007GBM")

def frontPageLanguage():
    if d(resourceId="com.whatsapp:id/title").get_text().split()[0] == "Selamat":
            d(resourceId="com.whatsapp:id/eula_accept").click()

frontPageLanguage()