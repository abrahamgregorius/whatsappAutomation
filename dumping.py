import uiautomator2 as u2 
from xml.dom import minidom
from time import sleep
import helper
import os

device_id = "R9CT300FQRE"

os.system(f'adb -s '+ device_id +' shell uiautomator dump --compressed /sdcard/' + device_id + '.xml ')
os.system(f'adb -s '+ device_id +' pull /sdcard/' + device_id + '.xml')