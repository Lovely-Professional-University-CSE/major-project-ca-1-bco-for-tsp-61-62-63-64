#tkinter
from tkinter import *
top=Tk()
top.geometry("500x250")
def sel1():
    a=float(e1.get())
    b=float(e2.get())
    fp=open("C:/Users/Shiva Chandra/Documents/Project/datasets/new-data.txt","a")
    fp.write(str(id_num)+" "+str(a)+" "+str(b))
    fp.close()
    top.destroy()
    import again
def sel2():
    a=float(e1.get())
    b=float(e2.get())
    fp=open("C:/Users/Shiva Chandra/Documents/Project/datasets/new-data.txt","a")
    fp.write(str(id_num)+" "+str(a)+" "+str(b))
    fp.close()
    top.destroy()
    import submit
import os
if os.path.exists("C:/Users/Shiva Chandra/Documents/Project/datasets/new-data.txt"):
  os.remove("C:/Users/Shiva Chandra/Documents/Project/datasets/new-data.txt")

id_num=1
top.title("    Data    ")

l1=Label(top,text="Position of City")
l1.grid(row=2,column=2)

e1=Entry(top,bd=5)
e1.grid(row=2,column=5)

e2=Entry(top,bd=5)
e2.grid(row=2,column=9)

b1=Button(top,bd=10,text="Again",command=sel1)
b1.grid(row=10,column=2)

b2=Button(top,bd=10,text="SUBMIT",command=sel2)
b2.grid(row=10,column=5)


top.mainloop()

          
