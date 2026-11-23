from tkinter import *
def my_function():
    print("Button clicked")

root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("First Application")

label = Label( root,text="Hello World",font=("Arial", 20, "bold"))
label.grid(row=0, column=0,padx=5, pady=5)

label = Label( root,text="How are you !",font=("Arial", 20, "bold"))
label.grid(row=1, column=0,padx=5, pady=5)

label = Label( root,text="My first Application",font=("Arial", 20, "bold"))
label.grid(row=2, column=0,padx=5, pady=5)



button = Button(root,text="Click Me",font=("Arial", 20, "bold"),command=my_function)
button.grid(row=3, column=0,padx=5, pady=5)

root.mainloop()


#label = Label(root, text="Hello World", font=("Arial", 20, "bold"))
#label.grid(row=0, column=0, padx=5, pady=5)