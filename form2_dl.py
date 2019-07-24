from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("DL Form")

l1=Label(window,text="First Name:")
l1.grid(column=0,row=0)
txt1=Entry(window,width=25)
txt1.grid(column=1,row=0)

l2=Label(window,text="Last Name:")
l2.grid(column=0,row=1)
txt2=Entry(window,width=25)
txt2.grid(column=1,row=1)

l3=Label(window,text="Gender:")
l3.grid(column=0,row=2)
txt3=Entry(window,width=25)
txt3.grid(column=1,row=2)

l4=Label(window,text="Address:")
l4.grid(column=0,row=3)
txt4=Entry(window,width=25)
txt4.grid(column=1,row=3)

l5=Label(window,text="License Type:")
l5.grid(column=0,row=4)

combo=Combobox(window)
combo['values']=['LMV','HMV']
#combo.current(1)
combo.grid(column=1,row=4)



bt1=Button(window,text="Save")
bt1.grid(column=0,row=5)
bt2=Button(window,text="Close")
bt2.grid(column=0,row=6)

window.geometry("400x300")
window.mainloop()