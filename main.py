import os
from time import sleep
import uiautomator2 as u2
import helper

d = u2.connect("R9CT4000AAM")

data = [["85811403649", "com.whatsapp"], ["895410810679", "com.fmwhatsapp"], ["895410810680", "com.yowhatsapp"], ["895410808876", "com.whatsapp.w4b"]]
numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b"]
device_id = "R9CT4007GBM"

autoHelper = helper.AutoHelper("R9CT4000AAM")

#     first = Main("Nenek", helper.generateNumber(), "R9CT4007GBM")
#     first.pushVideo(helper.generatePackage())

# autoHelper.registerWhatsapp('85892284244', "Abang Ganteng")
while True:
    autoHelper.makeCall('com.whatsapp', '81527650313')
