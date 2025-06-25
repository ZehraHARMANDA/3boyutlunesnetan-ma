# -*- coding: utf-8 -*-
"""
#06.2025zehraharmanda

@author: USER
"""
from tkinter import *
import tkinter as tk


window = tk.Tk()
window.title("DEMO")
window.geometry('700x420')
#lbl = tk.Label(window, text="Object Detection Module", font=("Arial Bold", 14))
#lbl.grid(column=9000, row=0)
def sign_in():
    sifre=entry.get()
    if sifre=="yazılım":
        label.config(text="Giriş başarılı")
        yolo_image_nms.process()
    else:
        print("yanlış giriş")

entry=Entry(window)
entry.place(x=20,y=70)
label=Label(window)
label.config(text="Şifrenizi giriniz",font=("Arial",20))
label.place(x=20,y=20)
buton=Button(window)
buton.config(text="Giriş yap",bg="black",fg="white",command=sign_in)
buton.place(x=20,y=100)


window.mainloop()








def sign_in():
    sifre=entry.get()
    if sifre=="yazılım":
        label.config(text="Giriş başarılı")
        cv2.namedWindow("Detection Window", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 900, 900)
        cv2.imshow("Detection Window", img)
        start_video.destroy()

    else:
        print("yanlış giriş")
        
def start_video():
    text1 = "Detected object: " + label
    color1 = (0, 0, 0) 
    cv2.putText(img, text1,(start_x-20,start_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color1, 2)

entry=Entry(window)
entry.place(x=20,y=70)

label=Label(window)
label.config(text="Şifrenizi giriniz",font=("Arial",20))
label.place(x=20,y=20)
buton=Button(window)
buton.config(text="Giriş yap",bg="black",fg="white",command=sign_in)
buton.place(x=20,y=50)



window.mainloop()
