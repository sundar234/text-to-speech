from tkinter import *
from gtts import gTTS
from playsound import playsound


root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Sundar - TEXT_TO_SPEECH')

Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='white smoke',fg="Blue").pack()
Label(root, text ='Sundar' , font ='arial 15 bold', bg = 'white smoke',fg="Blue").pack(side = BOTTOM)


Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)


Msg = StringVar()


entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Sundar.mp3')
    playsound('Sundar.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4,bg="green").place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'Orange').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset,fg="Red").place(x=175 , y =140)


root.mainloop()
