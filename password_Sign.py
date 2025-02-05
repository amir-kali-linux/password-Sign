#github -----> https://github.com/amir-kali-linux/
import time
from tkinter import *
time.sleep(1)
print("https://github.com/amir-kali-linux/")

def iran():
    password = ent.get()
    if password == '1234':
       lab1.config(text = 'IRAN ALFA')
    else:
        lab1.config(text = 'ERROR')

window = Tk()
window.geometry('400x360')
window.title('iran alfa')

ent=Entry(window)
ent.place(x=72,y=10)

lab=Label(window, text = 'password :')
lab.place(x=10,y=10)

lab1=Label(window)
lab1.place(x=10,y=100)

btn=Button(window, text = 'Next', command=iran)
btn.place(x=21,y=310)

window.mainloop()