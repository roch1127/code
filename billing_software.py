from tkinter import *
import math,random
import os
from tkinter import messagebox



class bill:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1370x700+0+0")
        title=Label(self.root,font=("times new roman",30,"bold"),text="BILLING SOFTWARE",relief=GROOVE,bd=10,fg="white",bg="blue")
        title.pack(fill='x')

#=======variables==================
#=======cosmetics==================
        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.hair_gel=IntVar()
        self.shampoo=IntVar()
#=======grocery=====================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
#======cold_drinks==================
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.limca=IntVar()
        self.pepsi=IntVar()
        self.sprite=IntVar()

#=======total price===============
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
#========tax=======================
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
#========customer details=========
        self.cname=StringVar()
        self.contactno=StringVar()
        self.bilno=StringVar()
        x=random.randint(1000,9999)
        self.bilno.set(str(x))
        self.search=StringVar()




        customer_details=LabelFrame(self.root,text=" Customer Details ",bg="light blue",fg="white",bd=10,relief=GROOVE,font=("times new roman",14))
        customer_details.place(x=0,y=80,relwidth=1)

        cname_label=Label(customer_details,text="Customer Name",font=("times new roman",18,"bold"),bg="light blue",fg="blue")
        cname_label.grid(row=0,column=0,padx=20,pady=5)
        cname_entry=Entry(customer_details,textvariable=self.cname,width=20,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        cname_entry.grid(row=0,column=1)

        cphone_label=Label(customer_details,text="Contact Number",font=("times new roman",18,"bold"),bg="light blue",fg="blue")
        cphone_label.grid(row=0,column=2,padx=20,pady=5)
        cphone_entry=Entry(customer_details,textvariable=self.contactno,width=20,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        cphone_entry.grid(row=0,column=3)

        cbill_label=Label(customer_details,text="Bill Number",font=("times new roman",18,"bold"),bg="light blue",fg="blue")
        cbill_label.grid(row=0,column=4,padx=20,pady=5)
        cbill_entry=Entry(customer_details,textvariable=self.search,width=20,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        cbill_entry.grid(row=0,column=5)

        search_button=Button(customer_details,command=self.search_bill,text="Search",bg="blue",width=12,bd=6,font=("times new roman",12,"bold"))
        search_button.grid(row=0,column=6,padx=15,pady=7)

        cosmetics=LabelFrame(self.root,text=" Cosmetics ",bg="light blue",fg="white",bd=10,relief=GROOVE,font=("times new roman",14))
        cosmetics.place(x=5,y=170,width=325,height=380)

        bathsoap_label=Label(cosmetics,text="Bath Soap",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        bathsoap_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        bathsoap_entry=Entry(cosmetics,textvariable=self.bath_soap,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        bathsoap_entry.grid(row=0,column=1,padx=10,pady=10)

        facecream_label=Label(cosmetics,text="Face Cream",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        facecream_label.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        facecream_entry=Entry(cosmetics,textvariable=self.face_cream,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        facecream_entry.grid(row=1,column=1,padx=10,pady=10)

        facewash_label=Label(cosmetics,text="Facewash",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        facewash_label.grid(row=2,column=0,padx=10,pady=5,sticky="w")
        facewash_entry=Entry(cosmetics,textvariable=self.face_wash,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        facewash_entry.grid(row=2,column=1,padx=10,pady=10)

        hairspray_label=Label(cosmetics,text="Hair Spray",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        hairspray_label.grid(row=3,column=0,padx=10,pady=5,sticky="w")
        hairspray_entry=Entry(cosmetics,textvariable=self.hair_spray,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        hairspray_entry.grid(row=3,column=1,padx=10,pady=10)

        hairgel_label=Label(cosmetics,text="Hair Gel",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        hairgel_label.grid(row=4,column=0,padx=10,pady=5,sticky="w")
        hairgel_entry=Entry(cosmetics,textvariable=self.hair_gel,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        hairgel_entry.grid(row=4,column=1,padx=10,pady=10)

        Shampoo_label=Label(cosmetics,text="Shampoo",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        Shampoo_label.grid(row=5,column=0,padx=10,pady=5,sticky="w")
        shampoo_entry=Entry(cosmetics,textvariable=self.shampoo,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        shampoo_entry.grid(row=5,column=1,padx=10,pady=10)

        grocery=LabelFrame(self.root,text=" Grocery ",bg="light blue",fg="white",bd=10,relief=GROOVE,font=("times new roman",14))
        grocery.place(x=350,y=170,width=325,height=380)

        rice_label=Label(grocery,text="Rice",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        rice_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        rice_entry=Entry(grocery,textvariable=self.rice,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        rice_entry.grid(row=0,column=1,padx=10,pady=10)

        foodoil_label=Label(grocery,text="Food Oil",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        foodoil_label.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        foodoil_entry=Entry(grocery,textvariable=self.food_oil,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        foodoil_entry.grid(row=1,column=1,padx=10,pady=10)

        daal_label=Label(grocery,text="Daal",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        daal_label.grid(row=2,column=0,padx=10,pady=5,sticky="w")
        daal_entry=Entry(grocery,textvariable=self.daal,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        daal_entry.grid(row=2,column=1,padx=10,pady=10)

        wheat_label=Label(grocery,text="Wheat",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        wheat_label.grid(row=3,column=0,padx=10,pady=5,sticky="w")
        wheat_entry=Entry(grocery,textvariable=self.wheat,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        wheat_entry.grid(row=3,column=1,padx=10,pady=10)

        sugar_label=Label(grocery,text="Sugar",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        sugar_label.grid(row=4,column=0,padx=10,pady=5,sticky="w")
        sugar_entry=Entry(grocery,textvariable=self.sugar,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        sugar_entry.grid(row=4,column=1,padx=10,pady=10)

        tea_label=Label(grocery,text="Tea",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        tea_label.grid(row=5,column=0,padx=10,pady=5,sticky="w")
        tea_entry=Entry(grocery,textvariable=self.tea,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        tea_entry.grid(row=5,column=1,padx=10,pady=10)

        cold_drink=LabelFrame(self.root,text=" Cold Drinks ",bg="light blue",fg="white",bd=10,relief=GROOVE,font=("times new roman",14))
        cold_drink.place(x=695,y=170,width=325,height=380)

        maza_label=Label(cold_drink,text="Maza",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        maza_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        maza_entry=Entry(cold_drink,textvariable=self.maza,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        maza_entry.grid(row=0,column=1,padx=10,pady=10)

        coke_label=Label(cold_drink,text="Coke",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        coke_label.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        coke_entry=Entry(cold_drink,textvariable=self.coke,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        coke_entry.grid(row=1,column=1,padx=10,pady=10)

        frooti_label=Label(cold_drink,text="Frooti",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        frooti_label.grid(row=2,column=0,padx=10,pady=5,sticky="w")
        frooti_entry=Entry(cold_drink,textvariable=self.frooti,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        frooti_entry.grid(row=2,column=1,padx=10,pady=10)

        limca_label=Label(cold_drink,text="Limca",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        limca_label.grid(row=3,column=0,padx=10,pady=5,sticky="w")
        limca_entry=Entry(cold_drink,textvariable=self.limca,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        limca_entry.grid(row=3,column=1,padx=10,pady=10)

        pepsi_label=Label(cold_drink,text="Pepsi",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        pepsi_label.grid(row=4,column=0,padx=10,pady=5,sticky="w")
        pepsi_entry=Entry(cold_drink,textvariable=self.pepsi,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        pepsi_entry.grid(row=4,column=1,padx=10,pady=10)

        sprite_label=Label(cold_drink,text="Sprite",font=("times new roman",16,"bold"),bg="light blue",fg="blue")
        sprite_label.grid(row=5,column=0,padx=10,pady=5,sticky="w")
        sprite_entry=Entry(cold_drink,textvariable=self.sprite,width=15,bd=7,relief=SUNKEN,font=("arial",10),bg="white",fg="black")
        sprite_entry.grid(row=5,column=1,padx=10,pady=10)

        bill_area=Frame(self.root,bd=10,relief=GROOVE)
        bill_area.place(x=1030,y=170,width=332,height=380)
        billarea_label=Label(bill_area,text="Bill Area",font=("arial",16,"bold"),relief=GROOVE,bd=7,fg="black")
        billarea_label.pack(fill='x')
        scroll_y=Scrollbar(bill_area,orient=VERTICAL)
        self.textarea=Text(bill_area,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill='y')
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        billing_menu=LabelFrame(self.root,text=" Billing Menu ",bg="light blue",fg="white",bd=10,relief=GROOVE,font=("times new roman",14))
        billing_menu.place(x=0,y=550,relwidth=1,height=149)
        totalcosmeticprice_label=Label(billing_menu,text="Total Cosmetic Price",font=("arial",10,"bold"),bg="light blue",fg="blue")
        totalcosmeticprice_label.grid(row=0,column=0,padx=6,pady=3,sticky="w")
        totalcosmeticprice_entry=Entry(billing_menu,textvariable=self.cosmetic_price,width=15,bd=7,relief=SUNKEN,font=("times new roman",8),bg="white",fg="black")
        totalcosmeticprice_entry.grid(row=0,column=1,padx=10,pady=4)

        totalgroceryprice_label=Label(billing_menu,text="Total Grocery Price",font=("arial",10,"bold"),bg="light blue",fg="blue")
        totalgroceryprice_label.grid(row=1,column=0,padx=6,pady=3,sticky="w")
        totalgroceryprice_entry=Entry(billing_menu,textvariable=self.grocery_price,width=15,bd=7,relief=SUNKEN,font=("times new roman",8),bg="white",fg="black")
        totalgroceryprice_entry.grid(row=1,column=1,padx=10,pady=4)

        totalcold_drinkprice_label=Label(billing_menu,text="Total Cold Drink Price",font=("arial",10,"bold"),bg="light blue",fg="blue")
        totalcold_drinkprice_label.grid(row=2,column=0,padx=6,pady=3,sticky="w")
        totalcold_drinkprice_entry=Entry(billing_menu,textvariable=self.cold_drink_price,width=15,bd=7,relief=SUNKEN,font=("times new roman",8),bg="white",fg="black")
        totalcold_drinkprice_entry.grid(row=2,column=1,padx=10,pady=4)

        cosmetictax_label=Label(billing_menu,text="Cosmetic Tax",font=("arial",10,"bold"),bg="light blue",fg="blue")
        cosmetictax_label.grid(row=0,column=2,padx=6,pady=3,sticky="w")
        cosmetictax_entry=Entry(billing_menu,textvariable=self.cosmetic_tax,width=15,bd=7,relief=SUNKEN,font=("times new roman",8),bg="white",fg="black")
        cosmetictax_entry.grid(row=0,column=3,padx=10,pady=4)

        grocerytax_label=Label(billing_menu,text="Grocery Tax",font=("arial",10,"bold"),bg="light blue",fg="blue")
        grocerytax_label.grid(row=1,column=2,padx=6,pady=3,sticky="w")
        grocerytax_entry=Entry(billing_menu,textvariable=self.grocery_tax,width=15,bd=7,relief=SUNKEN,font=("times new roman",8),bg="white",fg="black")
        grocerytax_entry.grid(row=1,column=3,padx=10,pady=4)

        cold_drink_label=Label(billing_menu,text="Cold Drink Tax",font=("arial",10,"bold"),bg="light blue",fg="blue")
        cold_drink_label.grid(row=2,column=2,padx=6,pady=3,sticky="w")
        cold_drink_entry=Entry(billing_menu,textvariable=self.cold_drink_tax,width=15,bd=7,relief=SUNKEN,font=("times new roman",8),bg="white",fg="black")
        cold_drink_entry.grid(row=2,column=3,padx=10,pady=4)

        button_frame=Frame(self.root,bd=7,relief=GROOVE)
        button_frame.place(x=550,y=569,width=800,height=115)

        total_btn=Button(button_frame,command=self.total,text="Total",font=("arial",10,"bold"),bg="light blue",fg="white", width=17,height=3,bd=7,relief=GROOVE)
        total_btn.grid(row=0,column=0,padx=18,pady=8)
        generatebill_btn=Button(button_frame,command=self.bill_area,text="Generate Bill",font=("arial",10,"bold"),bg="light blue",fg="white", width=17,height=3,bd=7,relief=GROOVE)
        generatebill_btn.grid(row=0,column=1,padx=18,pady=8)
        clear_btn=Button(button_frame,command=self.clear_data,text="Clear",font=("arial",10,"bold"),bg="light blue",fg="white", width=17,height=3,bd=7,relief=GROOVE)
        clear_btn.grid(row=0,column=2,padx=18,pady=8)
        exit_btn=Button(button_frame,command=self.exit,text="Exit",font=("arial",10,"bold"),bg="light blue",fg="white", width=17,height=3,bd=7,relief=GROOVE)
        exit_btn.grid(row=0,column=3,padx=18,pady=8)
        self.welcome_bill()

    def total(self):
        self.cosmetic_bath_soap=self.bath_soap.get()*40
        self.cosmetic_face_cream=self.face_cream.get()*120
        self.cosmetic_face_wash=self.face_wash.get()*60
        self.cosmetic_hairspray=self.hair_spray.get()*180
        self.cosmetic_hairgel=self.hair_gel.get()*140
        self.cosmetic_shampoo=self.shampoo.get()*180
        self.total_cosmetic_price=float(
                                     self.cosmetic_bath_soap+
                                     self.cosmetic_face_cream+
                                     self.cosmetic_face_wash+
                                     self.cosmetic_hairspray+
                                     self.cosmetic_hairgel+
                                     self.cosmetic_shampoo

                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        self.grocery_rice=self.rice.get()*180
        self.grocery_foodoil=self.food_oil.get()*180
        self.grocery_daal=self.daal.get()*60
        self.grocery_wheat=self.wheat.get()*240
        self.grocery_sugar=self.sugar.get()*45
        self.grocery_tea=self.tea.get()*150
        self.total_grocery_price=float(
                 self.grocery_rice+
                 self.grocery_foodoil+
                 self.grocery_daal+
                 self.grocery_wheat+
                 self.grocery_sugar+
                 self.grocery_tea

        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.10),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cold_drink_maza=self.maza.get()*60
        self.cold_drink_coke=self.coke.get()*60
        self.cold_drink_frooti=self.frooti.get()*50
        self.cold_drink_limca=self.limca.get()*40
        self.cold_drink_pepsi=self.pepsi.get()*50
        self.cold_drink_sprite=self.sprite.get()*60
        self.total_cold_drink_price=float(
                self.cold_drink_maza+
                self.cold_drink_coke+
                self.cold_drink_frooti+
                self.cold_drink_limca+
                self.cold_drink_pepsi+
                self.cold_drink_sprite

        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.15),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drink_price+self.c_tax
                              +self.g_tax+self.d_tax)

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t\tWELCOME\n")
        self.textarea.insert(END,f"\n Bill Number: {self.bilno.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.cname.get()}")
        self.textarea.insert(END,f"\n Customer Contact Number: {self.contactno.get()}")
        self.textarea.insert(END,f"\n ===================================")
        self.textarea.insert(END,f"\n Product\t\tQty\tPrice")
        self.textarea.insert(END,f"\n ===================================")

    def bill_area(self):
        if self.cname.get()=="" or self.contactno.get()=="":
            messagebox.showerror("ERROR","Customer details is required")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("ERROR","No product has been purchased")
        else:
            self.welcome_bill()
            if self.bath_soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.bath_soap.get()}\t{self.cosmetic_bath_soap}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t{self.cosmetic_face_cream}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.cosmetic_face_wash}")
            if self.hair_spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.hair_spray.get()}\t{self.cosmetic_hairspray}")
            if self.hair_gel.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t{self.cosmetic_hairgel}")
            if self.shampoo.get()!=0:
                self.textarea.insert(END,f"\n Shampoo\t\t{self.shampoo.get()}\t{self.cosmetic_shampoo}")

            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t{self.grocery_rice}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t{self.grocery_foodoil}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t{self.grocery_daal}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t{self.grocery_wheat}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t{self.grocery_wheat}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t{self.grocery_tea}")

            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t{self.cold_drink_maza}")
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t{self.cold_drink_coke}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t{self.cold_drink_frooti}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t{self.cold_drink_limca}")
            if self.pepsi.get()!=0:
                self.textarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t{self.cold_drink_pepsi}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t{self.cold_drink_sprite}")

            self.textarea.insert(END,f"\n ===================================")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic tax: {self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery tax: {self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic tax: {self.cold_drink_tax.get()}")

            self.textarea.insert(END,f"\n Total Bill:Rs. {str(self.total_bill)}")
            self.textarea.insert(END,f"\n ===================================")
            self.save_bill()

    def save_bill(self):
        promt=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if promt>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bilno.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No: {self.bilno.get()} biil saved sucessfully")
        else:
            return

    def search_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for i in f1:
                  self.textarea.insert(END,i)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("ERROR","Invalid bill no")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            self.bath_soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gel.set(0)
            self.shampoo.set(0)
            #=======grocery=====================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #======cold_drinks==================
            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.limca.set(0)
            self.pepsi.set(0)
            self.sprite.set(0)

            #=======total price===============
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            #========tax=======================
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #========customer details=========
            self.cname.set("")
            self.contactno.set("")
            self.bilno.set("")
            x=random.randint(1000,9999)
            self.bilno.set(str(x))
            self.search.set("")
            self.welcome_bill()

    def exit(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()





















root=Tk()
obj=bill(root)
root.mainloop()
