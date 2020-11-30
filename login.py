from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1348x700+0+0")
        self.bg=ImageTk.PhotoImage(file="pexels-riccardo-bertolo-4245826.jpg")
        self.bg_image=Label(self.root,image=self.bg)
        self.bg_image.place(x=0,y=0,relwidth=1,relheight=1)
        frame_login=Frame(self.root,bg="light blue",width=500,height=350)
        frame_login.place(x=150,y=150)
        Title=Label(frame_login,text="Login Here",font=("impact",30,"bold"),fg="blue",bg="light blue")
        Title.place(x=40,y=20)
        username_label=Label(frame_login,text="Username",font=("times new roman",20),fg="blue",bg="light blue")
        username_label.place(x=40,y=100)
        self.username_entry=Entry(frame_login,fg="black",bg="white",width=40)
        self.username_entry.place(x=40,y=140)
        password_label=Label(frame_login,text="Password",font=("times new roman",20),fg="blue",bg="light blue")
        password_label.place(x=40,y=180)
        self.password_entry=Entry(frame_login,fg="black",bg="white",width=40)
        self.password_entry.place(x=40,y=220)

        forget_button=Button(frame_login,text="Forgot Password?", bg="light blue",fg="white",bd=0,font=("times new roman",15,"bold"))
        forget_button.place(x=40,y=260)
        login_button=Button(self.root,text="Login", bg="blue",fg="white",width=15,bd=0,command=self.login_function,font=("times new roman",15,"bold"))
        login_button.place(x=250,y=480)

    def login_function(self):
        if self.username_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        elif self.username_entry.get()!="Rochelle" or self.password_entry.get()!="rochelle123":
            messagebox.showerror("Error","Wrong username or password",parent=self.root)
        else:
            messagebox.showinfo("success","you have logged in successfully",parent=self.root)










root=Tk()
obj=login(root)
root.mainloop()