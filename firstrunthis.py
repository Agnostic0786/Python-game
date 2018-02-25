from Tkinter import *
import tkMessageBox
import Tkinter
import random
import string
import start


def msg(event=None):
     mainset()
     randompics()

def randompics():
    mainset()
    Apic=picflag
    hang(Apic)

def OK():
     var=mvar.get()
     var=string.upper(var)
     if var==picflag[1]:
          tkMessageBox.showinfo("Event Triggered","Congratulations")
          num2=Var2.get()
          Var2.set(num2+10)
          mvar.set('')
          msg()
     else:
          tkMessageBox.showinfo("Sorry","Worng Guess")
          mvar.set('')
          num=Var1.get()
          if num==1:
               t=tkMessageBox.askretrycancel("YOU are HANGED","Game Over \n Click on retry to play again")
               if t==False:
                    root.destroy()
               num=4
               Var2.set(0)
          Var1.set(num-1)
          


#----------------keyboard values -------------------------------------#

def af():
     a=mvar.get()
     mvar.set(a+'A')
def bf():
     a=mvar.get()
     mvar.set(a+'B')
def cf():
     a=mvar.get()
     mvar.set(a+'C')
def df():
     a=mvar.get()
     mvar.set(a+'D')
def ef():
     a=mvar.get()
     mvar.set(a+'E')
def ff():
     a=mvar.get()
     mvar.set(a+'F')
def gf():
     a=mvar.get()
     mvar.set(a+'G')
def hf():
     a=mvar.get()
     mvar.set(a+'H')
def iif():
     a=mvar.get()
     mvar.set(a+'I')
def jf():
     a=mvar.get()
     mvar.set(a+'J')
def kf():
     a=mvar.get()
     mvar.set(a+'K')
def lf():
     a=mvar.get()
     mvar.set(a+'L')
def mf():
     a=mvar.get()
     mvar.set(a+'M')
def nf():
     a=mvar.get()
     mvar.set(a+'N')
def of():
     a=mvar.get()
     mvar.set(a+'O')
def pf():
     a=mvar.get()
     mvar.set(a+'P')
def qf():
     a=mvar.get()
     mvar.set(a+'Q')
def rf():
     a=mvar.get()
     mvar.set(a+'R')
def sf():
     a=mvar.get()
     mvar.set(a+'S')
def tf():
     a=mvar.get()
     mvar.set(a+'T')
def uf():
     a=mvar.get()
     mvar.set(a+'U')
def vf():
     a=mvar.get()
     mvar.set(a+'V')
def wf():
     a=mvar.get()
     mvar.set(a+'W')
def xf():
     a=mvar.get()
     mvar.set(a+'X')
def yf():
     a=mvar.get()
     mvar.set(a+'Y')
def zf():
     a=mvar.get()
     mvar.set(a+'Z')



def mainset():
     global picflag
     direct=[[A0,"IRONMAN"],[A1,"SADBOY"],[A2,"BABY"],[A3,"SADGIRL"],[A4,"TRANSFORMER"],[A5,"COUPLE"],[A6,"BATMAN"],[A7,"THOR"],[A8,"FLASH"],[A9,"NODDY"],[A10,"TOM"],[A11,"JERRY"],[A12,"SUPERMAN"],[A13,"PIKACHU"],[A14,"WOLVERINE"]]
     picflag=random.choice(direct)


def hang(Apic):
    #tp=Frame(root)
    But1=Button(root,image=Apic[0],height=200,width=180)
    But1.grid(row=1,column=0,rowspan=2)
    #tp.grid(row=2,column=0)
    

root=Tk()
root.title("HangMan")

Var1=IntVar()
Var1.set(3)
Var2=IntVar()
Var2.set(0)
mvar=StringVar()

#root.geometry("400x400+300+300")

#root.resizable(width=False, height=False)

A0=PhotoImage(file="pics/iron.gif")
A1=PhotoImage(file="pics/alo2.gif")
A2=PhotoImage(file="pics/kid1.gif")
A3=PhotoImage(file="pics/sa2.gif")
A4=PhotoImage(file="pics/samp5.gif")
A5=PhotoImage(file="pics/cup1.gif")
A6=PhotoImage(file="pics/1.gif")
A7=PhotoImage(file="pics/3.gif")
A8=PhotoImage(file="pics/4.gif")
A9=PhotoImage(file="pics/5.gif")
A10=PhotoImage(file="pics/6.gif")
A11=PhotoImage(file="pics/7.gif")
A12=PhotoImage(file="pics/8.gif")
A13=PhotoImage(file="pics/9.gif")
A14=PhotoImage(file="pics/10.gif")
direct=[[A0,"IRONMAN"],[A1,"SADBOY"],[A3,"SADGIRL"]]
picflag=random.choice(direct)




tf=Frame(root)
head=Label(tf,text='Hangman',activebackground="blue",height=2,width=28,foreground="black",font="Times 20 bold italic")
head.grid(row=0,column=0)
tf.grid(row=0,column=0,columnspan=3)
hang(picflag)
theBut=Button(root,text="New Word",relief="raised",activebackground="blue",height=2,width=20,command=msg)
theBut.grid(row=1,column=1)
Butok=Button(root,text='OK',height=2,width=20,relief=RAISED,command=OK)
Butok.grid(row=2,column=1)


head3=Label(root)
head3.grid(row=5,column=0,rowspan=2)
en=Entry(root,textvariable=mvar,show='*',width=30,bd=7,font="Times 20 bold italic")
en.grid(row=7,column=0,rowspan=2,columnspan=5)
head4=Label(root)
head4.grid(row=9,column=0,rowspan=2)
head5=Label(root)
head5.grid(row=11,column=0,rowspan=2)

#-------------------------------------------keyboard----------------------------------------------------------------#
key=Frame(root)

Buta=Button(key,text='A',height=2,width=7,relief=RAISED,command=af)
Buta.grid(row=0,column=0,rowspan=2,columnspan=2)
Butb=Button(key,text='B',height=2,width=7,relief=RAISED,command=bf)
Butb.grid(row=0,column=2,rowspan=2,columnspan=2)
Butc=Button(key,text='C',height=2,width=7,relief=RAISED,command=cf)
Butc.grid(row=0,column=4,rowspan=2,columnspan=2)
Butd=Button(key,text='D',height=2,width=7,relief=RAISED,command=df)
Butd.grid(row=0,column=6,rowspan=2,columnspan=2)
Bute=Button(key,text='E',height=2,width=7,relief=RAISED,command=ef)
Bute.grid(row=0,column=8,rowspan=2,columnspan=2)
Butf=Button(key,text='F',height=2,width=7,relief=RAISED,command=ff)
Butf.grid(row=0,column=10,rowspan=2,columnspan=2)
Butg=Button(key,text='G',height=2,width=7,relief=RAISED,command=gf)
Butg.grid(row=0,column=12,rowspan=2,columnspan=2)
Buth=Button(key,text='H',height=2,width=7,relief=RAISED,command=hf)
Buth.grid(row=0,column=14,rowspan=2,columnspan=2)
Buti=Button(key,text='I',height=2,width=7,relief=RAISED,command=iif)
Buti.grid(row=2,column=0,rowspan=2,columnspan=3)
Butj=Button(key,text='J',height=2,width=7,relief=RAISED,command=jf)
Butj.grid(row=2,column=2,rowspan=2,columnspan=3)
Butk=Button(key,text='K',height=2,width=7,relief=RAISED,command=kf)
Butk.grid(row=2,column=4,rowspan=2,columnspan=3)
Butl=Button(key,text='L',height=2,width=7,relief=RAISED,command=lf)
Butl.grid(row=2,column=6,rowspan=2,columnspan=3)
Butm=Button(key,text='M',height=2,width=7,relief=RAISED,command=mf)
Butm.grid(row=2,column=8,rowspan=2,columnspan=3)
Butn=Button(key,text='N',height=2,width=7,relief=RAISED,command=nf)
Butn.grid(row=2,column=10,rowspan=2,columnspan=3)
Buto=Button(key,text='O',height=2,width=7,relief=RAISED,command=of)
Buto.grid(row=2,column=12,rowspan=2,columnspan=3)
Butp=Button(key,text='P',height=2,width=7,relief=RAISED,command=pf)
Butp.grid(row=4,column=1,rowspan=2,columnspan=3)
Butq=Button(key,text='Q',height=2,width=7,relief=RAISED,command=qf)
Butq.grid(row=4,column=3,rowspan=2,columnspan=3)
Butr=Button(key,text='R',height=2,width=7,relief=RAISED,command=rf)
Butr.grid(row=4,column=5,rowspan=2,columnspan=3)
Buts=Button(key,text='S',height=2,width=7,relief=RAISED,command=sf)
Buts.grid(row=4,column=7,rowspan=2,columnspan=3)
Butt=Button(key,text='T',height=2,width=7,relief=RAISED,command=tf)
Butt.grid(row=4,column=9,rowspan=2,columnspan=3)
Butu=Button(key,text='U',height=2,width=7,relief=RAISED,command=uf)
Butu.grid(row=4,column=11,rowspan=2,columnspan=3)
Butv=Button(key,text='V',height=2,width=7,relief=RAISED,command=vf)
Butv.grid(row=6,column=2,rowspan=2,columnspan=3)
Butw=Button(key,text='W',height=2,width=7,relief=RAISED,command=wf)
Butw.grid(row=6,column=4,rowspan=2,columnspan=3)
Butx=Button(key,text='X',height=2,width=7,relief=RAISED,command=xf)
Butx.grid(row=6,column=6,rowspan=2,columnspan=3)
Buty=Button(key,text='Y',height=2,width=7,relief=RAISED,command=yf)
Buty.grid(row=6,column=8,rowspan=2,columnspan=3)
Butz=Button(key,text='Z',height=2,width=7,relief=RAISED,command=zf)
Butz.grid(row=6,column=10,rowspan=2,columnspan=3)

key.grid(row=13,column=0,columnspan=2)

#-------------------------Guess-------------------------------#

head6=Label(root)
head6.grid(row=21,column=0,rowspan=2)
g=Label(root,text="Your Points : ",foreground="red",font="Times 15 bold italic")
g.grid(row=23,column=0,rowspan=2)
en1=Label(root,textvariable=Var2,width=2,bd=4,relief=FLAT,font="Times 15 bold italic")
en1.grid(row=23,column=0,rowspan=2,columnspan=4)
g2=Label(root,text="no. of guesses remaining : ",foreground="black",font="Times 15 bold italic")
g2.grid(row=27,column=0,rowspan=2,columnspan=2)
en=Label(root,textvariable=Var1,width=2,bd=4,relief=FLAT,font="Times 15 bold italic")
en.grid(row=27,column=1,rowspan=2,columnspan=3)


root.mainloop()
