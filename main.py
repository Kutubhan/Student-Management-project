from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as mp


class Student:
    def __init__(self,root):

        self.root=root

        self.root.title("IIT ASHRAM")
        self.root.geometry("1360x700+0+0")

    # =====All variables========
        self.Roll_No_var = StringVar()
        self.physicsmarks_var = StringVar()
        self.mathsmarks_var = StringVar()
        self.testdate_var=StringVar()
        self.chemistrymarks_var = StringVar()
        self.totalmarks_var = StringVar()
        self.search_com_var = StringVar()
        self.search_var = StringVar()

        title=Label(self.root,text="IIT ASHRAM",bd=10,relief=GROOVE,font=("times new roman",40,"bold","italic"),bg="white",fg="blue")
        title.pack(side=TOP,fill=X)


    #=======Manage Frame=====


        Manage_Frame=Frame(self.root,bd=4,relief=GROOVE,bg="#1560BD")
        Manage_Frame.place(x=20,y=100,width=450,height=560)



        m_title=Label(Manage_Frame,text="Manage Students Results",bg="#1560BD",fg="white",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=5)

        lbl_roll=Label(Manage_Frame,text="Roll no.",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=5,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,padx=5,pady=10,sticky="w")

        lbl_testdate=Label(Manage_Frame,text="Test Date",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_testdate.grid(row=2,column=0,pady=10,padx=5, sticky="w")

        txt_testdate=Entry(Manage_Frame,textvariable=self.testdate_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_testdate.grid(row=2,column=1,padx=5,pady=10,sticky="w")

        lbl_name=Label(Manage_Frame,text="Physics Marks",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=3,column=0,pady=10,padx=5,sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.physicsmarks_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=3, column=1, padx=5, pady=10, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Maths Marks", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=4, column=0, pady=10, padx=5, sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.mathsmarks_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=4, column=1, padx=5, pady=10, sticky="w")

        lbl_Contact = Label(Manage_Frame, text="Chemsitry Marks", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=5, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.chemistrymarks_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=5, pady=10, sticky="w")

        lbl_Address = Label(Manage_Frame,text="Total Marks", bg="#1560BD", fg="white",font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=5, sticky="w")

        txt_Address=Entry(Manage_Frame,textvariable=self.totalmarks_var,font=("",13),bd=5,relief=GROOVE)
        txt_Address.grid(row=6,column=1,pady=30,padx=5,sticky="w")

#============Button Frame======

        btn_Frame = Frame(Manage_Frame,bd=0, relief=RIDGE, bg="#1560BD")
        btn_Frame.place(x=40,y=480, width=380)

        Addbtn=Button(btn_Frame,text="Add",command=self.add_students,width=10).grid(row=0,column=0,padx=5, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=5, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=5, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10,command = self.clear).grid(row=0, column=3, padx=5, pady=10)
        showgraph = Button(btn_Frame, text="Show Graph",command = self.graphplotting, width=10).grid(row=1, column=2, padx=5, pady=10)

        # ======Detail Frame======

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#1560BD")
        Detail_Frame.place(x=500, y=100, width=800, height=560)

        lbl_search = Label(Detail_Frame, text="Search By:", bg="#1560BD", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=5, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.search_com_var,
                                    font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Rollno", "Date")
        combo_search.grid(row=0, column=1, padx=5, pady=10)

        txt_search = Entry(Detail_Frame, textvariable=self.search_var, font=("times new roman", 10, "bold"), bd=4,
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=5, pady=10, sticky="w")
        searchbtn = Button(Detail_Frame, command=self.search_data, text="Search", width=10, pady=5).grid(row=0,
                                                                                                         column=3,
                                                                                                         padx=5,
                                                                                                         pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", command=self.fetch_data, width=10, pady=5).grid(row=0,
                                                                                                           column=4,
                                                                                                           padx=5,
                                                                                                           pady=10)

        # =======Table frame======
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#1560BD")
        Table_Frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Result_table = ttk.Treeview(Table_Frame,
                                          columns=("Rollno", "Date", "PhysicsMarks", "MathsMarks", "ChemistryMarks",
                                                   "TotalMarks"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Result_table.xview)
        scroll_y.config(command=self.Result_table.yview)
        self.Result_table.heading("Rollno", text="Rollno")
        self.Result_table.heading("Date", text="Date")
        self.Result_table.heading("PhysicsMarks", text="Physics Marks")
        self.Result_table.heading("MathsMarks", text="Maths Marks")
        self.Result_table.heading("ChemistryMarks", text="Chemistry Marks")
        self.Result_table.heading("TotalMarks", text="Total Marks")
        self.Result_table["show"] = 'headings'
        self.Result_table.column("Rollno", width=50)
        self.Result_table.column("Date", width=50)
        self.Result_table.column("PhysicsMarks", width=100)
        self.Result_table.column("MathsMarks", width=75)
        self.Result_table.column("ChemistryMarks", width=100)
        self.Result_table.column("TotalMarks", width=100)

        self.Result_table.pack(fill=BOTH, expand=1)
        self.Result_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #===============functionality=========
    def add_students(self):
        if(self.Roll_No_var.get() == "" or self.physicsmarks_var.get() == "" or self.mathsmarks_var.get() == "" or self.chemistrymarks_var.get() == "" or self.totalmarks_var.get() == ""):
           messagebox.showerror("error","all fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="kutubkhan",database="studentmanagementsys")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into results values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.Roll_No_var.get(),
                                                                                    self.testdate_var.get(),
                                                                                    self.physicsmarks_var.get(),
                                                                                    self.mathsmarks_var.get(),
                                                                                    self.chemistrymarks_var.get(),
                                                                                    self.totalmarks_var.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent= self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to:2{str(es)}",parent=self.root)

        # fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                           database="studentmanagementsys")
        my_cursur = conn.cursor()
        my_cursur.execute("select * from results")
        data = my_cursur.fetchall()
        if len(data) != 0:
            self.Result_table.delete(*self.Result_table.get_children())
            for a in data:
                self.Result_table.insert('', END, values=a)
            conn.commit()
            conn.close()



    def clear(self):
        self.Roll_No_var.set("")
        self.testdate_var.set("")
        self.physicsmarks_var.set("")
        self.mathsmarks_var.set("")
        self.chemistrymarks_var.set("")
        self.totalmarks_var.set("")

    def update_data(self):
        if (self.Roll_No_var.get() == "" or self.physicsmarks_var.get() == "" or self.mathsmarks_var.get() == "" or self.chemistrymarks_var.get() == "" or self.totalmarks_var.get() == ""):
            messagebox.showerror("error", "all fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                               database="studentmanagementsys")
                my_cursur = conn.cursor()
                my_cursur.execute("update results set rollno=%s, Date=%s, PhysicsMarks=%s,MathsMarks=%s,ChemsitryMarks=%s,TotalMarks=%s", (
                    self.Roll_No_var.get(),
                    self.testdate_var.get(),
                    self.physicsmarks_var.get(),
                    self.mathsmarks_var.get(),

                    self.chemistrymarks_var.get(),
                    self.totalmarks_var.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been updated!", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"due to:2{str(es)}", parent=self.root)

        # get cursor

    def get_cursor(self, ev):
        cursor_row = self.Result_table.focus()
        contents = self.Result_table.item(cursor_row)
        row = contents["values"]

        self.Roll_No_var.set(row[0])
        self.testdate_var.set(row[1])
        self.physicsmarks_var.set(row[2])
        self.mathsmarks_var.set(row[3])
        self.chemistrymarks_var.set(row[4])
        self.totalmarks_var.set(row[5])

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
                    my_cursur.execute("delete from results where Rollno=%s",(
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
        if self.search_com_var.get() == "" or self.search_var.get() == "":
            messagebox.showerror("error", "please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="kutubkhan",
                                               database="studentmanagementsys")
                my_cursur = conn.cursor()
                my_cursur.execute("select * from results where " + str(self.search_com_var.get()) + " LIKE '%" + str(
                    self.search_var.get()) + "%'")
                data = my_cursur.fetchall()
                if len(data) != 0:
                    self.Result_table.delete(*self.Result_table.get_children())
                    for i in data:
                        self.Result_table.insert('', END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("error", f"due to:2{str(es)}", parent=self.root)


    def graphplotting(self):
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="kutubkhan",
                                       database="studentmanagementsys")
        mycursor = mydb.cursor()

        # Fecthing Data From mysql to my python progame
        mycursor.execute("select Date, TotalMarks from results where Rollno=%s",(
                        self.Roll_No_var.get(),
                    ))
        result = mycursor.fetchall

        Date = []
        Marks = []

        for i in mycursor:
            Date.append(i[0])
            Marks.append(int(i[1]))

        print("Date of Test = ", Date)
        print("Marks of Students = ", Marks)

        # Visulizing Data using Matplotlib
        mp.plot(Date, Marks)
        mp.xlabel("Test Date")
        mp.ylabel("Student's Marks")
        mp.title("Student's Result")
        mp.show()

root=Tk()
ob=Student(root)
root.mainloop()

