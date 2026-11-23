from tkinter import *
from tkinter import messagebox
from tkinter import ttk

with open ("Student_data.txt","w")as t1:
    pass

def Submit_Button():

    if us.get() =="" or em.get()=="" or mn.get()=="" or pass1.get()=="" or pass2.get()=="":
        messagebox.showerror("Error!","Please complete all fields!")
    else:
        if pass1.get()!=pass2.get():
            messagebox.showerror("Error!","pasword dont match!")
        else:    
           pass
    g=""
    if gender.get()=="male":
        g="male"
    elif gender.get()=="female":
        g="female"
    else:
        pass

    print(gender.get())

    skills=""
    if python_var.get()==1:
        skills+="python"
    if java_var.get()==1:
        skills+=","+"java"
    if sql_var.get()==1:
        skills+=","+"SQL"


    s=""
    s+=us.get()+"\t"+em.get()+"\t"+mn.get()+"\t"+pass1.get()+"\t"+pass2.get()+"\t"+g+"\t"+skills+"\t"+edu.get()+"\t"+str(st_age.get())+"\n"

    with open ("Student_data.txt","a")as t1:
        t1.write(s)


    # print(skills)
    
    # print(edu.get())
    # print(st_age.get())

def Exit_Button():
    print("Clicked Exit Button")    

root = Tk()
#root.geometry("500x300")
#root.resizable(False, False)
root.title("Registration Application")

us=StringVar()
em=StringVar()
mn=StringVar()
pass1=StringVar()
pass2=StringVar()
gender=StringVar(value="Male")
python_var=IntVar(value=0)
java_var=IntVar(value=0)
sql_var=IntVar(value=0)
edu=StringVar(value="None")
st_age=IntVar(value=17)


L = Label( root,text="Registration Form",font=("segoe print", 50, "bold"),fg="dark blue")
L.grid(row=0,  columnspan=2, pady=25)


L1 = Label( root,text="Enter User Name :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L1.grid(row=1, column=0,padx=5, pady=5)

Username=Entry( root,font=("Arial", 18, "bold"),textvariable=us)
Username.grid(row=1, column=1,padx=5, pady=5)

L2 = Label( root,text="Enter Email :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L2.grid(row=2, column=0,padx=5, pady=5)

Email=Entry( root,font=("Arial", 18, "bold"),textvariable=em)
Email.grid(row=2, column=1,padx=5, pady=5)

L3 = Label( root,text="Enter Mobile Number :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L3.grid(row=3, column=0,padx=5, pady=5)

Mobile=Entry( root,font=("Arial", 20, "bold"),textvariable=mn)
Mobile.grid(row=3, column=1,padx=5, pady=5)

L4 = Label( root,text="Enter Password :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L4.grid(row=4, column=0,padx=5, pady=5)

Password= Entry( root,font=("Arial", 20, "bold"),show="*",textvariable=pass1)
Password.grid(row=4, column=1,padx=5, pady=5)

L5 = Label( root,text=" Verify Password :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L5.grid(row=5, column=0,padx=5, pady=5)

VerifyPassword= Entry( root,font=("Arial", 18, "bold"),show="*",textvariable=pass2)
VerifyPassword.grid(row=5, column=1,padx=5, pady=5)

L6 = Label( root,text="select Gender:",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L6.grid(row=6, column=0,padx=5, pady=5)

Male=Radiobutton( root,text="Male",font=("Arial", 18, "bold"),value="Male",variable=gender,justify="left",anchor="w",width=10)
Male.grid(row=7, column=0,padx=5, pady=5)

Female=Radiobutton( root,text="Female",font=("Arial", 18, "bold"),value="Female",variable=gender,justify="left",anchor="w",width=10)
Female.grid(row=7, column=1,padx=5, pady=5)

L7=Label(root,text="Check skills ! :",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L7.grid(row=8, column=0,padx=5, pady=5)

p=Checkbutton(root,text="Python",font=("Arial", 18, "bold"),variable=python_var,justify="left",anchor="w",width=10)
p.grid(row=9, column=0,padx=5, pady=5)

j=Checkbutton(root,text="Java",font=("Arial", 18, "bold"),variable=java_var,justify="left",anchor="w",width=10)
j.grid(row=9, column=1,padx=5, pady=5)

s=Checkbutton(root,text="SQL",font=("Arial", 18, "bold"),variable=sql_var,justify="left",anchor="w",width=10)
s.grid(row=10, column=0,padx=5, pady=5)

c=Checkbutton(root,text="  C++  ",font=("Arial", 18, "bold"),variable=sql_var,justify="left",anchor="w",width=10)
c.grid(row=10, column=1,padx=5, pady=5)
#combobox
L8=Label(root,text="Select Education:",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L8.grid(row=11, column=0,padx=5, pady=5)

Education=ttk.Combobox(root,values=["None","SSC","HSC","Diploma","BCA"],textvariable=edu,font=("Arial", 18, "bold"))
Education.grid(row=11, column=1,padx=5, pady=5)

#spinbox
L9=Label(root,text="Select age:",font=("Arial", 18, "bold"),justify="left",anchor="w",width=20)
L9.grid(row=12, column=0,padx=5, pady=5)

age=Spinbox(root,from_=11,to=30,textvariable=st_age,font=("Arial", 18, "bold"))
age.grid(row=12, column=1,padx=5, pady=5)

B1 = Button(root,text="Submit",font=("Arial", 18, "bold"),command=Submit_Button,fg="green")
B1.grid(row=14, column=0,padx=5, pady=5)

B2 = Button(root,text="Exit",font=("Arial", 18, "bold"),command=Exit_Button,fg="red")
B2.grid(row=14, column=1,padx=5, pady=5)

root.mainloop()


