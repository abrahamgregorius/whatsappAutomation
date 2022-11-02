import random

numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
packdata = ["com.whatsapp", "com.fmwhatsapp", "com.yowhatsapp", "com.whatsapp.w4b", "com.aero"]


def generateNumber():
    number = random.choice(numdata)
    return number

def generatePackage():
    package = random.choice(packdata)
    return package

def cobaPrint(func):
    return "ini adalah sesuatu mantap: " + func

po = generateNumber()
while True:
    b = generateNumber()
    print(b)
    print(po)
    print(cobaPrint(generateNumber))
    print(generateNumber())
    print("------------------------------")

    
def printa():
    print("abrama")

def printb():
    print("b")

functions = [printa, printb]

a = random.choice(functions)

a()