import pyautogui
import webbrowser as web
import string

from time import sleep

web.open("https://web.whatsapp.com/send?phone=+573112969582")
sleep(10)


welcome = "Esto es un scrip para recordarte que me debes dinero\
            Primero te recordara 161023 veces que me debes dinero\
            luego te contara el quijote entero por lineas.\
            quedo super atento a tu llamada. Saludos."

injection = "Recuerda que me debes 600K"

abc = list(string.ascii_lowercase)

var = 0

with open("quijote.txt", "r") as file:
    content = file.read()
    content_splited = content.split(" ")

while var <= 24:

    # pyautogui.typewrite(welcome)
    # pyautogui.press("enter")
    # sleep(5)

    # for kek in range(5):
    #     var = kek.toString()
    #     pyautogui.typewrite(var)
    #     pyautogui.press("enter")

    with open("quijote.txt", "r") as file:
        content = file.read()
        var = content.split(" ")
        print(len(var))
        for i in range(161023):
            pyautogui.typewrite(injection + " " + var[i])
            pyautogui.press("enter")
            sleep(30)
        if i == 161023:
            with open("quijote.txt", "r") as file:
                for line in file:
                    pyautogui.typewrite(line)
                    pyautogui.press("enter")
                    sleep(60)
                var+=1    
        else :
            pass