from  tkinter import *
from PIL import  Image , ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
# Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomType = StringVar() 
        self.var_room = StringVar()
        self.var_meal = StringVar()        
        self.var_noOfDays = StringVar()
        self.var_paidTax = StringVar()
        self.var_actualTotal = StringVar()
        self.var_total = StringVar()


# Title

        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="blue", fg="gold" , bd=4 , relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

# LOGO image
        img2 =  Image.open(r"C:\Users\syshu\OneDrive\Desktop\Code_Era\3rd Year Projects\Hotel_Management_System\luxury-business-logo_1028264-5882.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2 , bd = 4 , relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)
# Label Frame
        labelframeleft = LabelFrame(self.root, text="ROOM DETAILS", font=("times new roman", 12, "bold"), bd=2 , relief=RIDGE)
        labelframeleft.place(x=5, y=50, width=425, height=490)


# label & entry

#  Customer contact
        lbl_cust_contact = Label(labelframeleft, text="CUSTMER CONTACT:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0 , sticky=W)

        entry_contact= ttk.Entry(labelframeleft,textvariable=self.var_contact, width =16 ,font=("times new roman", 13, "bold" ))
        entry_contact.grid(row=0, column=1 , sticky=W)
# fetch btn
        btnfetch = Button(labelframeleft, command=self.fetch_contact,text="Fetch", width=10, font=("times new roman", 10, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnfetch.place(x=330, y=6)

#  Check_in Date
        lbl_inDate = Label(labelframeleft, text="CHECK_IN DATE:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_inDate.grid(row=1, column=0 , sticky=W)

        entry_inDate= ttk.Entry(labelframeleft,textvariable=self.var_checkin, width =22 ,font=("times new roman", 13, "bold" ))
        entry_inDate.grid(row=1, column=1)

#  Check_out Date
        lbl_outDate = Label(labelframeleft, text="CHECK_OUT DATE:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_outDate.grid(row=2, column=0 , sticky=W)

        entry_outDate= ttk.Entry(labelframeleft,textvariable=self.var_checkout, width =22 ,font=("times new roman", 13, "bold" ))
        entry_outDate.grid(row=2, column=1)

#  Room Type
        lbl_roomType = Label(labelframeleft, text="ROOM TYPE:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_roomType.grid(row=3, column=0 , sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomType from details")
        row = my_cursor.fetchall()

        combo_ROOM = ttk.Combobox(labelframeleft,textvariable=self.var_roomType, font=("times new roman", 12, "bold"), width=22)
        combo_ROOM["value"] = row
        combo_ROOM.current(0)
        combo_ROOM.grid(row=3, column=1)

#  Available Room
        lbl_Available = Label(labelframeleft, text="ROOM:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Available.grid(row=4, column=0 , sticky=W)

        # entry_Available= ttk.Entry(labelframeleft, textvariable=self.var_room,width =22 ,font=("times new roman", 13, "bold" ))
        # entry_Available.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from details")
        rows = my_cursor.fetchall()

        combo_ROOM = ttk.Combobox(labelframeleft,textvariable=self.var_room, font=("times new roman", 12, "bold"), width=22)
        combo_ROOM["value"] =rows
        combo_ROOM.current(0)
        combo_ROOM.grid(row=4, column=1)
#  Meal
        lbl_meal = Label(labelframeleft, text="MEAL:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0 , sticky=W)

        combo_meal = ttk.Combobox(labelframeleft,textvariable=self.var_meal, font=("times new roman", 12, "bold"), width=22)
        combo_meal["value"] = ("BreakFast", "Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5, column=1)
#  No Of Days
        lbl_NoOfDay = Label(labelframeleft, text="NO OF DAYS:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_NoOfDay.grid(row=6, column=0 , sticky=W)

        entry_NoOfDay= ttk.Entry(labelframeleft, textvariable=self.var_noOfDays,width =22 ,font=("times new roman", 13, "bold" ))
        entry_NoOfDay.grid(row=6, column=1)
#  Sub Total
        lbl_sub = Label(labelframeleft, text="SUB TOTAL :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_sub.grid(row=7, column=0 , sticky=W)

        entry_sub= ttk.Entry(labelframeleft,textvariable=self.var_actualTotal, width =22 ,font=("times new roman", 13, "bold" ))
        entry_sub.grid(row=7, column=1)
#  Paid Tax
        lbl_paidTax = Label(labelframeleft, text="PAID TAX:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_paidTax.grid(row=8, column=0 , sticky=W)

        entry_paidTax= ttk.Entry(labelframeleft,textvariable=self.var_paidTax, width =22 ,font=("times new roman", 13, "bold" ))
        entry_paidTax.grid(row=8, column=1)
#  Total cost
        lbl_Tcost = Label(labelframeleft, text="TOTAL COST:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_Tcost.grid(row=9, column=0 , sticky=W)

        entry_Tcost= ttk.Entry(labelframeleft,textvariable=self.var_total, width =22 ,font=("times new roman", 13, "bold" ))
        entry_Tcost.grid(row=9, column=1)

# Bill Button
        btnBill = Button(labelframeleft, text="BILL", command=self.total,width=10, font=("times new roman", 10, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnBill.grid(row=10, column=0 , padx=2, pady=10, sticky=W)


# btn frame

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)


        btnAdd = Button(btn_frame, text="ADD",command=self.add_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnAdd.grid(row=0 ,column=0,padx=3)
        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnUpdate.grid(row=0 ,column=1,padx=3)
        btnDelete = Button(btn_frame,text="DELETE", command=self.mdelete ,width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnDelete.grid(row=0 ,column=2,padx=3)
        btnReset = Button(btn_frame, text="RESET",command=self.reset, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnReset.grid(row=0 ,column=3 ,padx=3)

# right table frame
        
# table of details Frame search system
        Table_Frame = LabelFrame(self.root, text="VIEW AND SEARCH  DETAILS", font=("times new roman", 12, "bold"), bd=2 , relief=RIDGE)
        Table_Frame.place(x=435, y=280, width=860, height=260)

         

        lblSearchBy = Label(Table_Frame, text="Search", font=("times new roman", 12, "bold"), bg="red" ,fg="white" , relief=RIDGE)
        lblSearchBy.grid(row=0, column=0 , sticky=W, padx=2)

        self.search_var = StringVar()


        combo_search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman", 12, "bold"), state="readonly", width=24)
        combo_search["value"] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search, width =24 ,font=("times new roman", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnSearch.grid(row=0 ,column=3,padx=1)
        btnShowAll = Button(Table_Frame, text="Show ALL", command=self.fetch_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnShowAll.grid(row=0 ,column=4,padx=1)

# Show data table (Details)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)
        
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_Table = ttk.Treeview(details_table,columns =("contact", "checkinDate","checkoutDate" ,"roomType","room", "meal","noOfDays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

#  Naming the columns

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkinDate", text="CheckinDate")
        self.room_Table.heading("checkoutDate", text="CheckoutDate")
        self.room_Table.heading("roomType", text="RoomType")
        self.room_Table.heading("room", text="Room")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noOfDays", text="NoOfDays")
        

        self.room_Table["show"]="headings"

#  Setting the width of columns

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkinDate", width=100)
        self.room_Table.column("checkoutDate", width=100)
        self.room_Table.column("roomType", width=100)
        self.room_Table.column("room", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noOfDays", width=100)
        
        self.room_Table.pack(fill=BOTH, expand=1)
        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
       
        self.fetch_data()

#  Function to add data to the database and table usging mysql
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
                messagebox.showerror("Error", "Please Enter Required Fields", parent=self.root)
        else:
                try:
                        conn = mysql.connector.connect(
                                host="localhost",
                                username="root",
                                password="3030",
                                database="new_schema"
                        )
                        my_cursor = conn.cursor()
                        my_cursor.execute(
                                "INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)",(
                                                                    self.var_contact.get(),
                                                                    self.var_checkin.get(),
                                                                    self.var_checkout.get(),
                                                                    self.var_roomType.get(), 
                                                                    self.var_room.get(),
                                                                    self.var_meal.get(),        
                                                                    self.var_noOfDays.get()
                                                                    ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Customer details added successfully", parent=self.root)
                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)
                except Exception as e:
                        messagebox.showerror("Error", f"Unexpected error: {str(e)}", parent=self.root)

       
# fetch function 


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

# get cursor function
    def get_cursor(self,events=""):
        cursor_row = self.room_Table.focus()
        content = self.room_Table.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomType.set(row[3])
        self.var_room.set(row[4])
        self.var_meal.set(row[5])       
        self.var_noOfDays.set(row[6])

# Update function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in = %s, check_out= %s ,roomtype = %s , roomavailable= %s, meal= %s, noOfdays= %s where Contact = %s",  (
                                                                 
                                                                    self.var_checkin.get(),
                                                                    self.var_checkout.get(),
                                                                    self.var_roomType.get(), 
                                                                    self.var_room.get(),
                                                                    self.var_meal.get(),        
                                                                    self.var_noOfDays.get( ),
                                                                    self.var_contact.get()
                                                       
                                                ))
                
            conn.commit()
            self.fetch_data()  # to refresh the table
            conn.close()
            messagebox.showinfo("Success", "ROOM details updated successfully", parent=self.root)
      
# delete function
    def mdelete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this detail?", parent=self.root)
        if mdelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
            my_cursor = conn.cursor()
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
# reset function 
    def reset(self):
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomType.set(""), 
        self.var_room.set(""),
        self.var_meal.set(""),        
        self.var_noOfDays.set("" ),
        self.var_contact.set(""),
        self.var_paidTax.set(""),
        self.var_actualTotal.set(""),
        self.var_total.set("")


#  Data fetch for room 
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Contact Number")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
            my_cursor = conn.cursor()
            query = ("SELECT Name FROM customer WHERE Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Contact Number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx =2) 
                
                showDataframe.place(x=455, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblName.grid(row=0, column=0 , sticky=W)
                lbl = Label(showDataframe, text = row[0], font=("times new roman", 12, "bold"), padx=2, pady=6)
                lbl.grid(row=0, column=1 , sticky=W)


                conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
                my_cursor = conn.cursor()
                query = ("SELECT Gender FROM customer WHERE Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender:", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=1, column=0 , sticky=W)
                lblgender = Label(showDataframe, text = row[0], font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=1, column=1 , sticky=W)


                conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
                my_cursor = conn.cursor()
                query = ("SELECT Email FROM customer WHERE Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Email:", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=2, column=0 , sticky=W)
                lblgender = Label(showDataframe, text = row[0], font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=2, column=1 , sticky=W)


                conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
                my_cursor = conn.cursor()
                query = ("SELECT Nationality FROM customer WHERE Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Nationality:", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=3, column=0 , sticky=W)
                lblgender = Label(showDataframe, text = row[0], font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=3, column=1 , sticky=W)

                conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
                my_cursor = conn.cursor()
                query = ("SELECT Address FROM customer WHERE Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Address:", font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=4, column=0 , sticky=W)
                lblgender = Label(showDataframe, text = row[0], font=("times new roman", 12, "bold"), padx=2, pady=6)
                lblgender.grid(row=4, column=1 , sticky=W)

# round up bill functions 
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        delta = outDate - inDate
        self.var_noOfDays.set(delta.days)


        if (self.var_meal.get() == "BreakFast" and self.var_roomType.get() == "SINGLE"):
            meal_cost = float(300)
            room_cost  =float(1000)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   

        elif (self.var_meal.get() == "BreakFast" and self.var_roomType.get() == "LUXURY"):
            meal_cost = float(300)
            room_cost  =float(2000)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "Lunch" and self.var_roomType.get() == "SINGLE"):
            meal_cost = float(400)
            room_cost  =float(1000)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "Lunch" and self.var_roomType.get() == "LUXURY"):
            meal_cost = float(400)
            room_cost  =float(2000)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "Lunch" and self.var_roomType.get() == "DOUBLE"):
            meal_cost = float(400)
            room_cost  =float(1500)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "Dinner" and self.var_roomType.get() == "SINGLE"):
            meal_cost = float(500)
            room_cost  =float(1000)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "Dinner" and self.var_roomType.get() == "LUXURY"):
            meal_cost = float(500)
            room_cost  =float(2000)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "Dinner" and self.var_roomType.get() == "DOUBLE"):
            meal_cost = float(500)
            room_cost  =float(1500)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   
        elif (self.var_meal.get() == "BreakFast" and self.var_roomType.get() == "DOUBLE"):
            meal_cost = float(300)
            room_cost  =float(1500)
            n1 = float(self.var_noOfDays.get())
            n2 =float(room_cost + meal_cost)
            n3 = float(n1 * n2)
            Tax = "Rs." + str("%.2f" % ((n3 * 0.1)))
            self.var_paidTax.set(Tax)
            self.var_actualTotal.set("Rs." + str("%.2f" % (n3))) 
            self.var_total.set("Rs." + str("%.2f" % (n3 + (n3 * 0.1))))   

# der search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()




if __name__ == "__main__":

    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
