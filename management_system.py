from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class employee():
    def __init__(self,root):
        self.root = root
        self.root.title(" Employee Management System")
        self.root.geometry("1370x750")

        title = Label(self.root, text="Employee Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),fg="white",bg="blue")
        title.pack(side=TOP,fill='x')

        #==========VARIABLES==========
        self.NAME=StringVar()
        self.MOBILENO=StringVar()
        self.DEPARTMENT=StringVar()
        self.GENDER=StringVar()
        self.EXPERIENCE=StringVar()
        self.EDUCATION=StringVar()
        self.search_by=StringVar()
        self.search_entry=StringVar()


        manageframe=Frame(bd=5,relief=RIDGE,bg="blue")
        manageframe.place(x=20,y=110,width=450,height=550)

        managetitle=Label(manageframe,text="Manage Employees",font=("times new roman",35,"bold"),fg="white",bg="blue")
        managetitle.grid(row=0,columnspan=2,pady=20)

        label_name=Label(manageframe,text="NAME",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_name.grid(row=1,column=0,sticky="w",padx=15,pady=10)
        entry_name=Entry(manageframe,textvariable=self.NAME,font=("times new roman",15,"bold"),fg="black",bg="white")
        entry_name.grid(row=1,column=1,sticky="w",padx=15,pady=10)

        label_address=Label(manageframe,text="ADDRESS",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_address.grid(row=2,column=0,sticky="w",padx=15,pady=10)
        self.text_address=Text(manageframe,width=20,height=2,font=("times new roman",15,"bold"),fg="black",bg="white")
        self.text_address.grid(row=2,column=1,sticky="w",padx=15,pady=10)

        label_mobileno=Label(manageframe,text="MOBILE NO.",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_mobileno.grid(row=3,column=0,sticky="w",padx=15,pady=10)
        entry_mobileno=Entry(manageframe,textvariable=self.MOBILENO,font=("times new roman",15,"bold"),fg="black",bg="white")
        entry_mobileno.grid(row=3,column=1,sticky="w",padx=15,pady=10)

        label_department=Label(manageframe,text="DEPARTMENT",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_department.grid(row=4,column=0,sticky="w",padx=15,pady=10)
        combo_department=ttk.Combobox(manageframe,textvariable=self.DEPARTMENT,font=("times new roman",15,"bold"))
        combo_department['values']=('Production','Quality','Research & Development', 'Human Resource Management','Marketing')
        combo_department.grid(row=4,column=1,sticky="w",padx=15,pady=10)

        label_gender=Label(manageframe,text="GENDER",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_gender.grid(row=5,column=0,sticky="w",padx=15,pady=10)
        combo_gender=ttk.Combobox(manageframe,textvariable=self.GENDER,font=("times new roman",15,"bold"))
        combo_gender['values']=('Male','Female','Other')
        combo_gender.grid(row=5,column=1,sticky="w",padx=15,pady=10)

        label_experience=Label(manageframe,text="EXPERIENCE",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_experience.grid(row=6,column=0,sticky="w",padx=15,pady=10)
        entry_experience=Entry(manageframe,textvariable=self.EXPERIENCE,font=("times new roman",15,"bold"),fg="black",bg="white")
        entry_experience.grid(row=6,column=1,sticky="w",padx=15,pady=10)

        label_education=Label(manageframe,text="EDUCATION",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_education.grid(row=7,column=0,sticky="w",padx=15,pady=10)
        entry_education=Entry(manageframe,textvariable=self.EDUCATION,font=("times new roman",15,"bold"),fg="black",bg="white")
        entry_education.grid(row=7,column=1,sticky="w",padx=15,pady=10)

#===============BUTTON FRAME===========

        button_frame=Frame(manageframe,bd=5,bg="blue",relief=RIDGE)
        button_frame.place(x=10,y=480,width=420)

        add_button=Button(button_frame,text="ADD",width=10,command=self.add_butn)
        add_button.grid(row=0,column=0,padx=10,pady=10)

        delete_button=Button(button_frame,text="DELETE",width=10,command=self.delete)
        delete_button.grid(row=0,column=1,padx=10,pady=10)

        update_button=Button(button_frame,text="UPDATE",width=10,command=self.update)
        update_button.grid(row=0,column=2,padx=10,pady=10)

        clear_button=Button(button_frame,command=self.clear_data,text="CLEAR",width=10)
        clear_button.grid(row=0,column=3,padx=10,pady=10)







        detailframe=Frame(bd=5,relief=RIDGE,bg="blue")
        detailframe.place(x=700,y=110,width=600,height=550)

        label_search=Label(detailframe,text="SEARCH BY",font=("times new roman",15,"bold"),fg="white",bg="blue")
        label_search.grid(row=0,column=0,sticky="w",pady=7,padx=6)
        combo_search=ttk.Combobox(detailframe,width=6,textvariable=self.search_by,font=("times new roman",15,"bold"))
        combo_search['values']=('NAME','MOBILENO','DEPARTMENT')
        combo_search.grid(row=0,column=1,sticky="w",pady=7,padx=6)

        entry_search=Entry(detailframe,width=13,textvariable=self.search_entry,font=("times new roman",15,"bold"),fg="black",bg="white")
        entry_search.grid(row=0,column=2,sticky="w",pady=7,padx=6)

        search_button=Button(detailframe,command=self.search_data,text="SEARCH",width=12)
        search_button.grid(row=0,column=3,pady=7,padx=6)

        showall_button=Button(detailframe,command=self.fetch_data,text="SHOW ALL",width=12)
        showall_button.grid(row=0,column=4,pady=7,padx=6)

        table_frame=Frame(detailframe,bd=5,bg="green",relief=RIDGE)
        table_frame.place(x=10,y=50,width=570,height=480)

        scrollx=Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(table_frame,orient=VERTICAL)

        scrollx.pack(side=BOTTOM,fill='x')
        scrolly.pack(side=RIGHT,fill='y')

        self.list_table = ttk.Treeview(table_frame,columns=('NAME','ADDRESS','MOBILENO','DEPARTMENT','GENDER','EXPERIENCE','EDUCATION'))
        scrollx.configure(command=self.list_table.xview)
        scrolly.configure(command=self.list_table.yview)

        self.list_table.heading("NAME", text="NAME")
        self.list_table.heading("ADDRESS",text="ADDRESS")
        self.list_table.heading("MOBILENO",text="MOBILE NO")
        self.list_table.heading("DEPARTMENT",text="DEPARTMENT")
        self.list_table.heading("GENDER",text="GENDER")
        self.list_table.heading("EXPERIENCE",text="EXPERIENCE")
        self.list_table.heading("EDUCATION",text="EDUCATION")
        self.list_table['show'] = 'headings'
        self.list_table.column("NAME",width=50)
        self.list_table.column("ADDRESS",width=100)
        self.list_table.column("MOBILENO",width=100)
        self.list_table.column("DEPARTMENT",width=100)
        self.list_table.column("GENDER",width=100)
        self.list_table.column("EXPERIENCE",width=100)
        self.list_table.column("EDUCATION",width=100)
        self.list_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.list_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_butn(self):
        if self.NAME.get()==""or self.text_address.get('1.0', END)==""or self.MOBILENO.get()== ""or self.DEPARTMENT.get()== ""or self.GENDER.get()== ""or self.EXPERIENCE.get()== ""or self.EDUCATION.get()=="":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
        elif self.MOBILENO.get().isnumeric()==FALSE:
            messagebox.showerror("ERROR","mobile number should be an integer")
        else:
            connectn = pymysql.connect(host="localhost", user="root", password="",database="employee management system")
            cur = connectn.cursor()  # to execute query
            cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s)",(self.NAME.get(), self.text_address.get('1.0', END), self.MOBILENO.get(), self.DEPARTMENT.get(),self.GENDER.get(), self.EXPERIENCE.get(),self.EDUCATION.get()))  # to access variables
            connectn.commit()  # to commit query
            self.fetch_data()
            self.clear_data()
            connectn.close()
            messagebox.showinfo("SUCCESS","RECORD HAS BEEN INSERTED")
    def fetch_data(self):
        connectn=pymysql.connect(host="localhost",user="root",password="",database="employee management system")
        cur=connectn.cursor()         #to execute query
        cur.execute("select * from employee")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.list_table.delete(*self.list_table.get_children())
            for row in rows:
                self.list_table.insert('',END,values=row)
            connectn.commit()
        connectn.close()

    def clear_data(self):
        self.NAME.set("")
        self.text_address.delete("1.0",END)
        self.MOBILENO.set("")
        self.DEPARTMENT.set("")
        self.GENDER.set("")
        self.EXPERIENCE.set("")
        self.EDUCATION.set("")

    def get_cursor(self,event):
        cursor_row=self.list_table.focus()
        contents=self.list_table.item(cursor_row)
        row=contents['values']
        self.NAME.set(row[0])
        self.text_address.delete("1.0",END)
        self.text_address.insert("1.0",row[1])
        self.MOBILENO.set(row[2])
        self.DEPARTMENT.set(row[3])
        self.GENDER.set(row[4])
        self.EXPERIENCE.set(row[5])
        self.EDUCATION.set(row[6])

    def update(self):
        connectn=pymysql.connect(host="localhost",user="root",password="",database="employee management system")
        cur=connectn.cursor()         #to execute query
        cur.execute("update employee set ADDRESS=%s,MOBILENO=%s, DEPARTMENT=%s,GENDER=%s,EXPERIENCE=%s,EDUCATION=%s where NAME=%s",(self.text_address.get('1.0',END),
                                                                         self.MOBILENO.get(),self.DEPARTMENT.get(),
                                                                         self.GENDER.get(),self.EXPERIENCE.get(),
                                                                         self.EDUCATION.get(),self.NAME.get())) #to access variables
        connectn.commit()#to commit query
        self.fetch_data()
        self.clear_data()
        connectn.close()

    def delete(self):
        connectn=pymysql.connect(host="localhost",user="root",password="",database="employee management system")
        cur=connectn.cursor()         #to execute query
        cur.execute("delete from employee where name =%s",self.NAME.get())
        connectn.commit()

        self.fetch_data()
        self.clear_data()
        connectn.close()

    def search_data(self):
        connectn=pymysql.connect(host="localhost",user="root",password="",database="employee management system")
        cur=connectn.cursor()         #to execute query
        cur.execute("select * from employee where "+str(self.search_by.get())+" LIKE '%"+str(self.search_entry.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.list_table.delete(*self.list_table.get_children())
            for row in rows:
                self.list_table.insert('',END,values=row)
            connectn.commit()
        connectn.close()



root = Tk()
obj = employee(root)
root.mainloop()
