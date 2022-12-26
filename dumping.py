import uiautomator2 as u2 
from xml.dom import minidom
from time import sleep
import helper
import os
import time


device_id = "R9CT300FQRE"


currentTime = time.ctime().split(" ")[3].replace(":", "_")
print(currentTime)
