#gui
import tkinter
import random
import time
from tkinter import *
import winsound
def sound():
   filename='game'
   winsound.PlaySound(filename, winsound.SND_ASYNC)
m=Tk()
m.geometry('1366x768')


m.title('casino')
C = Canvas(m, bg="blue", height=250, width=300)
filename = PhotoImage(file = "casinoimg.png")
background_label = Label(m, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.grid(row=0,column=0)
ourMessage =' WELCOME TO THE GAME CASINO '
messageVar = Message(m, text = ourMessage,width=500,bg='light green',font=('Helvetica',40,'bold')).grid(row=0,column=7)

Label(m,text='Username',bg='yellow',fg='red',font=('Helvetica',20)).grid(row=1)
Label(m,text='Password',bg='yellow',fg='red',font=('Helvetica',20)).grid(row=2)
e1=Entry(m)
e2=Entry(m)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)

acbal=1000
Message(m, text ="WANT A SOUND",width='400',bg='light green',font=('Helvetica',30)).grid(row=4,column=9)

Button(m ,text='YES',width='15',height='2',bg='green',font=('aerial',15),command=sound).grid(row=5,column=9)
Button(m ,text='NO',width='15',height='2',bg='green',font=('aerial',15)).grid(row=5,column=10)

def create_window():
   window = tkinter.Toplevel(m)
   Message(window , text='choose random value between 1 to 5 ',font=('pristina',20)).grid(row=1,column=1)
   Message(window , text=("your current acount balance is" ,acbal),font=('pristina',20)).grid(row=2,column=1)
   window.configure(bg='black')
   r=random.randint(1,5)
   
   def click1():
       Message(window , text='you pressed 1',font=('pristina',20)).grid(row=3,column=1)
       if r==1: 
          Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
          Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
          Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
      
          Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
          time.sleep(0.5)
         
          window.destroy()
          create_window()
   def click2():
       Message(window , text =' you pressed 2 ',font=('pristina',20)).grid(row=3,column=1)
       if r==2:
          Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
         
          Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
          Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
          
          Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
          time.sleep(0.5)
          window.destroy()
          create_window()
   def click3():
       Message(window , text = 'you pressed 3',font=('pristina',20)).grid(row=3,column=1)
       if r==3:
         Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
         
         Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
         Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
        
         Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
         time.sleep(0.5)
         window.destroy()
         create_window()
   def click4():
       Message(window , text = 'you pressed 4',font=('pristina',20)).grid(row=3,column=1)
       if r==4:
         Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
   
         Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
         Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
     
         Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
         time.sleep(0.5)
         window.destroy()
         create_window()
   def click5():
       Message(window , text='you pressed 5',font=('pristina',20)).grid(row=7,column=10)
       if r==5:
         Message(window , text='you  won',font=('pristina',20)).grid(row=4,column=1)
         
         Message(window , text=acbal+200,font=('pristina',20)).grid(row=5,column=1)
       else:
         Message(window , text='you loose',font=('pristina',20)).grid(row=4,column=1)
       
         Message(window , text=acbal-200,font=('pristina',20)).grid(row=5,column=1)
         time.sleep(0.5)
         window.destroy()
         create_window()
         
   b1=Button(window ,text='1',width='25',height='2',bg='green',font=('aerial',20),command=click1).grid(row=2,column=7)
   b2=Button(window ,text='2',width='25',height='2',bg='green',font=('aerial',20),command=click2).grid(row=3,column=6)
   b3=Button(window ,text='3',width='25',height='2',bg='green',font=('aerial',20),command=click3).grid(row=4,column=7)
   b4=Button(window ,text='4',width='25',height='2',bg='green',font=('aerial',20),command=click4).grid(row=5,column=6)
   b5=Button(window ,text='5',width='25',height='2',bg='green',font=('aerial',20),command=click5).grid(row=6,column=7)

   b6=Button(window,text='EXIT',width='25',height='2',bg='green',font=('aerial',20),command=window.destroy).grid(row=7,column=8)
    

Button(m,text='LOGIN',width='25',height='2',font=('aerial',20,'bold'),bg='#A25EEB',command=create_window).grid(row=10,column=7)

m.mainloop()

