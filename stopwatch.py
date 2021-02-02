import time
import pyttsx3
from tkinter import *
from tkinter import messagebox
import playsound
from tkinter import font as tkFont


name = input('What is your name?')
root = Tk()
voice = pyttsx3.init()
root.geometry("300x250")
root.title("Time Counter")
root.configure(bg='#293e40')

hour=StringVar()
minute=StringVar()
second=StringVar()


hour.set("00")
minute.set("00")
second.set("00")


hourEntry= Entry(root, width=3, font=("ds-digital",30,""),textvariable=hour)
hourEntry.place(relx=0.35, rely=0.2)

minuteEntry= Entry(root, width=3, font=("ds-digital",30,""),textvariable=minute)
minuteEntry.place(relx=0.5, rely=0.2)

secondEntry= Entry(root, width=3, font=("ds-digital",30,""),textvariable=second)
secondEntry.place(relx=0.65, rely=0.2)


def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60) 
        hours=0
        if mins >60:
            
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 0):
            voice.say(f'{name} Your time is up!')
            voice.runAndWait()
            playsound.playsound('Downloads/music-alarm.mp3', True)
            messagebox.showinfo("Time Countdown", "Time's up ")
        elif temp == 1200:
            voice.say(f'{name}, There is 20 minutes left on your timer!')
            voice.runAndWait()
        elif temp == 600:
            voice.say(f'{name}, There is 10 minutes left on your timer!')
            voice.runAndWait()       
        elif temp == 300:
            voice.say(f'{name}, There is 5 minutes left on your timer!')
            voice.runAndWait()
        temp -= 1



        
font = tkFont.Font(family='Kefa', size=27, weight='bold')
btn = Button(root, text='Set Time Countdown',bg='green',bd='5',command= submit)
btn['font'] = font
btn.place(relx=0.4, rely=0.7)

root.mainloop()  
