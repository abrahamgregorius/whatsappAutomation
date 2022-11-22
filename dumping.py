import uiautomator2 as u2 
from xml.dom import minidom
import os
import helper

d = u2.connect("R9CT300GE1D")

helpera = helper.AutoHelper()

print("blm")

print(helpera.adbs("whoami"))
print(helpera.adbs("adb shell dumpsys activity activities | grep mCurrentFocus "))

print("udh")
