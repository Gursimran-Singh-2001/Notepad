from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfile, asksaveasfilename
import tkinter.messagebox as tmsg
import os
root=Tk()
root.title("Untitled-Notepad")
def save():
    tmsg.showinfo("Info","Designed and Developed by Gursimran Singh")
def Openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Files","*.txt")])
    if(file==""):
        file=None
    else:
        f=open(file,"r")
        root.title(os.path.basename(file)+"-Notepad")
        textarea.insert(1.0,f.read())
        f.close()
def Savefile():
    global file
    file=asksaveasfilename(initialfile="Untitled.txt" , defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Files","*.txt")])
    if(file==""):
        file=None
    else:
        f=open(file,"w")
        root.title(os.path.basename(file)+"-Notepad")
        f.write(textarea.get(1.0,END))
        f.close()
def Exitfile():
    root.destroy()
def paste():
    textarea.event_generate(("<<Paste>>"))
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
yourmenu=Menu(root)
m1=Menu(yourmenu,tearoff=0)
m1.add_command(label="Open",command=Openfile)
m1.add_command(label="Save",command=Savefile)
m1.add_command(label="Exit",command=Exitfile)
yourmenu.add_cascade(label="File",menu=m1)

m2=Menu(yourmenu,tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
yourmenu.add_cascade(menu=m2,label="Edit")
root.config(menu=yourmenu)

m3=Menu(yourmenu,tearoff=0)
m3.add_command(label="Info",command=save)
yourmenu.add_cascade(menu=m3,label="About")
root.config(menu=yourmenu)


textarea=Text(root,font="LUCIDA 14 italic")
SCROLL=Scrollbar(root)
SCROLL.pack(side=RIGHT,fill=Y)
SCROLL.config(command=textarea.yview)
textarea.config(yscrollcommand=SCROLL.set)
textarea.pack(anchor="w",fill=BOTH)
root.mainloop()
