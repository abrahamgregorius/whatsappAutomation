import os
from time import sleep
import uiautomator2 as u2
import helper

data = [["85811403649", "com.whatsapp"], ["895410810679", "com.fmwhatsapp"], ["895410810680", "com.yowhatsapp"], ["895410808876", "com.whatsapp.w4b"]]
numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b"]

autoHelper = helper.AutoHelper()

#     first = Main("Nenek", helper.generateNumber(), "R9CT4007GBM")
#     first.pushVideo(helper.generatePackage())

# autoHelper.registerWhatsapp('85892284244', "Abang Ganteng")

# A | 81527650313 || 085811403517   
# B | 82163438039(BUSINESS WHATSAPP) || 82163438037(WHATSAPP)
# C | 82163438032(BANNED) || 82163438038(FMWHATSAPP)
# 85641312392, 85641312394

autoHelper.installPackages()

# autoHelper.makeConnection("Tselhome-FFC6", "wpa2", "71313451")

# 62 - 85892284244

# 62 - 82170186532

# 62 - 85811403649

# autoHelper.dumpUi('R9CT4000AAM')
