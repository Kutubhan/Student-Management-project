from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):

        self.root=root

        self.root.title("IIT ASHRAM")
        self.root.geometry("1360x700+0+0")

    # =====All variables========
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.address_var = StringVar()
        self.search_com_var = StringVar()
        self.search_var = StringVar()

        title=Label(self.root,text="IIT ASHRAM",bd=10,relief=GROOVE,font=("times new roman",40,"bold","italic"),bg="white",fg="blue")
        title.pack(side=TOP,fill=X)


    #=======Manage Frame=====


        Manage_Frame=Frame(self.root,bd=4,relief=GROOVE,bg="#1560BD")
        Manage_Frame.place(x=20,y=100,width=450,height=560)



        m_title=Label(Manage_Frame,text="Manage Students",bg="#1560BD",fg="white",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=5)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=5,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,padx=5,pady=10,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=5,sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=5, pady=10, sticky="w")

        lbl_Email = Label(Manage_Frame, text="E-Mail", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=5, sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=5, pady=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=5, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 13, "bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=5,pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=5, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=5, pady=10, sticky="w")

        lbl_Address = Label(Manage_Frame,text="Address", bg="#1560BD", fg="white",font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=5, sticky="w")

        txt_Address=Entry(Manage_Frame,textvariable=self.address_var,font=("",15),bd=5,relief=GROOVE)
        txt_Address.grid(row=6,column=1,pady=20,padx=5,sticky="w")

#============Button Frame======

        btn_Frame = Frame(Manage_Frame,bd=0, relief=RIDGE, bg="#1560BD")
        btn_Frame.place(x=40,y=480, width=380)

        Addbtn=Button(btn_Frame,text="Add",command=self.add_students,width=10).grid(row=0,column=0,padx=5, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=5, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=5, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10,command = self.clear).grid(row=0, column=3, padx=5, pady=10)


        # ======Detail Frame======

        Detail_Frame = Frame(self.root,bd=4, relief=RIDGE, bg="#1560BD")
        Detail_Frame.place(x=500, y=100, width=800, height=560)

        lbl_search=Label(Detail_Frame, text="Search By:", bg="#1560BD", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=5, sticky="w")


        combo_search = ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_com_var, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=5, pady=10)

        txt_search = Entry(Detail_Frame,textvariable=self.search_var ,font=("times new roman", 10, "bold"), bd=4, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=5, pady=10, sticky="w")
        searchbtn = Button(Detail_Frame,command=self.search_data,text="Search", width=10,pady=5).grid(row=0, column=3, padx=5, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all",command=self.fetch_data ,width=10,pady=5).grid(row=0, column=4, padx=5, pady=10)

#=======Table frame======
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#1560BD")
        Table_Frame.place(x=10,y=70,width=760,height=480)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("Address", text="Address")
        self.Student_table["show"]='headings'
        self.Student_table.column("Roll",width=50)
        self.Student_table.column("Name", width=150)
        self.Student_table.column("Email", width=150)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=150)
        self.Student_table.column("Address", width=200)

        self.Student_table.pack(fill= BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if(self.Roll_No_var.get() == "" or self.email_var.get() == "" or self.name_var.get() == "" or self.gender_var.get() == "" or self.contact_var.get() == "" or self.address_var.get() == ""):
           messagebox.showerror("error","all fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kutubkhan",database="studentmanagementsys")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.Roll_No_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.address_var.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent= self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to:2{str(es)}",parent=self.root)
#fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                       database="studentmanagementsys")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from student")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for a in data :
                self.Student_table.insert('',END,values= a)
            conn.commit()
        conn.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.address_var.set("")

    #get cursor
    def get_cursor(self,ev):
        cursor_row= self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents["values"]

        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.address_var.set(row[5])

    def update_data(self):
        if (self.Roll_No_var.get() == "" or self.email_var.get() == "" or self.name_var.get() == "" or self.gender_var.get() == "" or self.contact_var.get() == "" or self.address_var.get() == ""):
            messagebox.showerror("error", "all fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                               database="studentmanagementsys")
                my_cursur = conn.cursor()
                my_cursur.execute("update student set roll=%s,name=%s,email=%s,gender=%s,contact=%s,address=%s where Roll=%s", (
                    self.Roll_No_var.get(),
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.address_var.get()
                    self.Roll_No_var.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been updated!", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to:2{str(es)}", parent=self.root)

    def delete_data(self):
        if self.Roll_No_var.get()=="":
            messagebox.showerror("error", "all fields are required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("delete","are sure delete this statment",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                           database="studentmanagementsys")
                    my_cursur = conn.cursor()
                    my_cursur.execute("delete from student where Roll=%s",(
                        self.Roll_No_var.get(),
                    ))

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","your student has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to:2{str(es)}", parent=self.root)

    def search_data(self):
        if self.search_com_var.get()=="" or self.search_var.get()=="":
            messagebox.showerror("error","please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                               database="studentmanagementsys")
                my_cursur = conn.cursor()
                my_cursur.execute("select * from student where " +str(self.search_com_var.get()) + " LIKE '%" +str(self.search_var.get())+ "%'")
                data=my_cursur.fetchall()
                if len(data) != 0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for i in data:
                        self.Student_table.insert('',END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("error", f"due to:2{str(es)}", parent=self.root)








root=Tk()
ob=Student(root)
root.mainloop()




