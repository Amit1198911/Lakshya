import tkinter
from tkinter import *

m=Tk()
m.geometry('500x500')
m.configure(background='black')

m.title('casino')
acbal=1000
window = tkinter.Toplevel(m)
Message(window , text='choose random value between 1 to 5 ',font=('pristina',20)).grid(row=1,column=1)
Message(window , text=("your current acount balance is" ,acbal),font=('pristina',20)).grid(row=2,column=1)
window.configure(bg='black')
def click1():
       Message(window , text='you pressed 1',font=('pristina',20)).grid(row=3,column=1)
       if r==1:
          Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
          Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
          Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
          Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
def click2():
       Message(window , text =' you pressed 2 ',font=('pristina',20)).grid(row=3,column=1)
       if r==2:
          Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
          Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
          Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
          Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
def click3():
       Message(window , text = 'you pressed 3',font=('pristina',20)).grid(row=3,column=1)
       if r==3:
         Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
         Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
         Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
         Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
def click4():
       Message(window , text = 'you pressed 4',font=('pristina',20)).grid(row=3,column=1)
       if r==4:
         Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
         Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
         Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
         Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
def click5():
       Message(window , text='you pressed 5',font=('pristina',20)).grid(row=3,column=1)
       if r==5:
         Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
         Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
         Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
         Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
         
  
b1=Button(window ,text='1',width='25',height='2',bg='green',font=('aerial',20),command=click1).grid(row=2,column=7)
b2=Button(window ,text='2',width='25',height='2',bg='green',font=('aerial',20),command=click2).grid(row=3,column=6)
b3=Button(window ,text='3',width='25',height='2',bg='green',font=('aerial',20),command=click3).grid(row=4,column=7)
b4=Button(window ,text='4',width='25',height='2',bg='green',font=('aerial',20),command=click4).grid(row=5,column=6)
b5=Button(window ,text='5',width='25',height='2',bg='green',font=('aerial',20),command=click5).grid(row=6,column=7)
window.destroy()
Button(m,text='login',width='25',height='2',font=('aerial',20),command=create_window).grid(row=10,column=20)
m.mainloop()
