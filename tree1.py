from tkinter import *
from tkinter import ttk
import csv

def show_data():
    with open ("student record1.csv","r") as r1:
        csvreader=csv.reader(r1)
        for lines in csvreader:
            tree1.insert("","end",values=(lines[0],lines[1],lines[2],lines[3]))

root=Tk()
heading1 = Label(root,text="STUDENT INFORMATION",font=("Arial", 18, "bold"),fg="blue")
heading1.grid(row=0, column=0, pady=10)

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
'''
for i in range(len(rn)):
    tree1.insert("",END,values=(rn[i],names[i],gender[i],age[i]))
    '''
tree1.grid(row=0,column=0,padx=5,pady=5)

b=Button(root,text="Show Data",command=show_data)
b.grid(row=1,column=0)
root.mainloop()