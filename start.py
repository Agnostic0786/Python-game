import Tkinter
from Tkinter import *
import time


root=Tk()
name=StringVar()



def ag():
    n1=name.get()
    n="Hello "+n1+" Lets Rockkkk"
    root.destroy()
    root1=Tk()
    a=Label(root1,text=n,width=30,bd=7,foreground="black",font="Times 20 bold italic")
    a.grid(row=0,column=0,rowspan=2,columnspan=2)
    theBut1=Button(root1,text="OK",relief="raised",activebackground="blue",height=2,width=20,command=root1.destroy)
    theBut1.grid(row=4,column=0,columnspan=3,rowspan=2)
    root1.mainloop()
    


g=Label(root,text="Enter your Name : ",foreground="black",font="Times 15 bold italic")
g.grid(row=0,column=0,rowspan=2)
g1=Label(root)
g1.grid(row=2,column=0,rowspan=2)
en=Entry(root,textvariable=name,width=30,bd=7,font="Times 20 bold italic")
en.grid(row=4,column=0,rowspan=2,columnspan=5)
theBut=Button(root,text="Let's Rockkk",relief="raised",activebackground="blue",height=2,width=20,command=ag)
theBut.grid(row=6,column=0,columnspan=4,rowspan=2)
root.mainloop()





