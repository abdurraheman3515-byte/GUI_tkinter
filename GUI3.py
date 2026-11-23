from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("Student record")

with open("Student record.csv","r")as t1:
    pass


def Submit_Button():
    s=""
    s+=str(sn.get())+"\t"+str(gender.get())+"\t"+str(rn.get())+"\t"+str(std.get())+"\t"+str(physics.get())+"\t"+str(chemistry.get())+"\t"+str(maths.get())+"\n"
   
    with open("Student record.csv","a")as t1:
        t1.write(s)
        messagebox.showinfo("Success","Record submited succesfuly")
    

sn=StringVar()
gender=StringVar(value="Male")
rn=IntVar()
std=StringVar(value="None")
physics=StringVar()
chemistry=StringVar()
maths=StringVar()



L1=Label(root,text="Enter Student Name :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L1.grid(row=0, column=0,padx=5, pady=5)

stname=Entry( root,font=("Arial", 18, "bold"),textvariable=sn)
stname.grid(row=0, column=1,padx=5, pady=5)

L1=Label(root,text="Select Gender :",font=("Arial", 20, "bold"),justify="left",anchor="w",width=20)
L1.grid(row=1, columnspan=3,padx=5, pady=5)

Male=Radiobutton( root,text="Male",font=("Arial", 18, "bold"),value="Male",variable=gender,justify="left",anchor="w",width=10)
Male.grid(row=2, column=0,padx=5, pady=5)

Female=Radiobutton( root,text="Female",font=("Arial", 18, "bold"),value="Female",variable=gender,justify="left",anchor="w",width=10)
Female.grid(row=2, column=1,padx=5, pady=5)

L2=Label(root,text="Enter Roll No :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L2.grid(row=3, column=0,padx=5, pady=5)

role=Spinbox( root,from_=1,to=60,font=("Arial", 18, "bold"),textvariable=rn)
role.grid(row=3, column=1,padx=5, pady=5)

L3=Label(root,text="Select Standard :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L3.grid(row=4, column=0,padx=5, pady=5)

Std=ttk.Combobox( root,values=["None","11th sci","12th sci"],textvariable=std,font=("Arial", 18, "bold"))
Std.grid(row=4, column=1,padx=5, pady=5)

L6=Label(root,text="Enter marks :",font=("Arial", 20, "bold"),justify="left",anchor="w",width=20)
L6.grid(row=5, columnspan=3,padx=5, pady=5)

L7=Label(root,text="Physics :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L7.grid(row=6, column=0,padx=5, pady=5)

p=Entry( root,font=("Arial", 18, "bold"),textvariable=physics)
p.grid(row=6, column=1,padx=5, pady=5)

L8=Label(root,text="Chemistry :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L8.grid(row=7, column=0,padx=5, pady=5)

c=Entry( root,font=("Arial", 18, "bold"),textvariable=chemistry)
c.grid(row=7, column=1,padx=5, pady=5)

L9=Label(root,text="Maths :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L9.grid(row=8, column=0,padx=5, pady=5)

m=Entry( root,font=("Arial", 18, "bold"),textvariable=maths)
m.grid(row=8, column=1,padx=5, pady=5)


B1 = Button(root,text="Submit",font=("Arial", 18, "bold"),command=Submit_Button,fg="green")
B1.grid(row=10, column=1,padx=5, pady=5)








root.mainloop()