from tkinter import *
from tkinter import ttk

root=Tk()
#treeview Decliration
mycolumns=["R.No","Name","Gender","Age"]
tree1=ttk.Treeview(root,columns=mycolumns,show="headings",height=5)

#Creat columns
tree1.column("R.No",anchor=CENTER,width=50)
tree1.column("Name",anchor=CENTER,width=150)
tree1.column("Gender",anchor=CENTER,width=100)
tree1.column("Age",anchor=CENTER,width=50)

#Creat column heading
tree1.heading("R.No",text="Roll No")
tree1.heading("Name",text="Student Name")
tree1.heading("Gender",text="Gender")
tree1.heading("Age",text="Age")

#Add data into a rows
rn=[1,2,3,4,5]
names=["Ali","Aamna","Aarish","Sana","Aabid"]
gender=["Male","Female","Male","Female","Male"]
age=[18,20,21,19,22]
for i in range(len(rn)):
    tree1.insert("",END,values=(rn[i],names[i],gender[i],age[i]))
    
tree1.grid(row=0,column=0,padx=5,pady=5)
root.mainloop()