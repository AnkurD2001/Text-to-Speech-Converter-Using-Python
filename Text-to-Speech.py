## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'yellow')
root.title('Yellow Moose - TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='lime').pack()
Label(root, text ='Yellow Moose' , font ='arial 15 bold', bg = 'lime').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='yellow').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Yellow Moose.mp3')
    playsound('Yellow Moose.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4,  bg = 'blue',fg = 'white').place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'Red1').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset,  bg = 'blue',fg = 'white').place(x=175 , y =140)


#infinite loop to run program
root.mainloop()
