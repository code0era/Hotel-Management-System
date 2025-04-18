from  tkinter import *
from PIL import  Image , ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

# variables
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof= StringVar()
        self.var_id_number  = StringVar()
# Title

        lbl_title = Label(self.root, text="ADD CUSTMER DETAILS", font=("times new roman", 18, "bold"), bg="blue", fg="gold" , bd=4 , relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

# LOGO image
        img2 =  Image.open(r"C:\Users\syshu\OneDrive\Desktop\Code_Era\3rd Year Projects\Hotel_Management_System\luxury-business-logo_1028264-5882.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2 , bd = 4 , relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

# Label Frame
        labelframeleft = LabelFrame(self.root, text="CUSTMER DETAILS", font=("times new roman", 12, "bold"), bd=2 , relief=RIDGE)
        labelframeleft.place(x=5, y=50, width=425, height=490)

# label & entry

#  cust_ref
        lbl_cust_ref = Label(labelframeleft, text="CUSTMER REF NO.", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0 , sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref, width =22 ,font=("times new roman", 13, "bold" ), state="readonly")
        entry_ref.grid(row=0, column=1)

#  cust_name
        cname = Label(labelframeleft, text="CUSTMER NAME", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0 , sticky=W)

        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust, width =22 ,font=("times new roman", 13, "bold"))
        txtcname.grid(row=1, column=1)

#  cust_MOTHER NAME
        lblmname = Label(labelframeleft, text="MOTHER NAME", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0 , sticky=W)

        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother, width =22 ,font=("times new roman", 13, "bold"))
        txtmname.grid(row=2, column=1)

# GENDER COMBOBOX
        label_gender = Label(labelframeleft, text="GENDER", font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0 , sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=22)
        combo_gender["value"] = ("Male", "Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)


#  post code

        lblPostCode = Label(labelframeleft, text="POST CODE", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0 , sticky=W)

        txtPostCode= ttk.Entry(labelframeleft,textvariable=self.var_post, width =22 ,font=("times new roman", 13, "bold"))
        txtPostCode.grid(row=4, column=1)
#  mobile number
        lblMobile = Label(labelframeleft, text="MOBILE NO.", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0 , sticky=W)

        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width =22 ,font=("times new roman", 13, "bold"))
        txtMobile.grid(row=5, column=1)

# email
        lblEmail = Label(labelframeleft, text="EMAIL", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0 , sticky=W)

        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, width =22 ,font=("times new roman", 13, "bold"))
        txtEmail.grid(row=6, column=1)


# nationality
        lblNationality = Label(labelframeleft, text="NATIONALITY", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0 , sticky=W)
        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("times new roman", 12, "bold"), state="readonly", width=22)
        combo_nationality["value"] = ("Indian", "American", "British", "Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        


# ID Proof
        lblIdProof = Label(labelframeleft, text="ID PROOF", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0 , sticky=W)

        combo_idproof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("times new roman", 12, "bold"), state="readonly", width=22)
        combo_idproof["value"] = ("Aadhar Card", "Passport", "Driving License", "Voter ID")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)



# Id Number
        lblIdNumber = Label(labelframeleft, text="ID NUMBER", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0 , sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number, width =22 ,font=("times new roman", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

# Address
        lblAddress = Label(labelframeleft, text="ADDRESS", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0 , sticky=W)

        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_address, width =22 ,font=("times new roman", 13, "bold"))
        txtAddress.grid(row=10, column=1)


# btn frame

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)


        btnAdd = Button(btn_frame,command=self.add_data, text="ADD", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnAdd.grid(row=0 ,column=0,padx=3)
        btnUpdate = Button(btn_frame,command=self.update, text="UPDATE", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnUpdate.grid(row=0 ,column=1,padx=3)
        btnDelete = Button(btn_frame,command=self.mdelete, text="DELETE", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnDelete.grid(row=0 ,column=2,padx=3)
        btnReset = Button(btn_frame,command=self.reset, text="RESET", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnReset.grid(row=0 ,column=3 ,padx=3)


# right table frame
        
# table of details Frame search system
        Table_Frame = LabelFrame(self.root, text="VIEW AND SEARCH  DETAILS", font=("times new roman", 12, "bold"), bd=2 , relief=RIDGE)
        Table_Frame.place(x=435, y=50, width=860, height=490)

         

        lblSearchBy = Label(Table_Frame, text="Search", font=("times new roman", 12, "bold"), bg="red" ,fg="white" , relief=RIDGE)
        lblSearchBy.grid(row=0, column=0 , sticky=W, padx=2)

        self.search_var = StringVar()


        combo_search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman", 12, "bold"), state="readonly", width=24)
        combo_search["value"] = ("Ref", "Name", "Mother", "Gender", "PostCode", "Mobile", "Email"," Nationality", "IdProof", "IdNumber", "Address")
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
        details_table.place(x=0, y=50, width=860, height=350)
        
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,columns =("ref", "name","mother" ,"gender","post", "mobile","email", "nationality","idproof","idnumber","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

#  Nameing the columns

        self.Cust_Details_Table.heading("ref", text="REF")
        self.Cust_Details_Table.heading("name", text=" NAME")
        self.Cust_Details_Table.heading("mother", text="MOTHER NAME")
        self.Cust_Details_Table.heading("gender", text="GENDER")
        self.Cust_Details_Table.heading("post", text="POSTCODE")
        self.Cust_Details_Table.heading("mobile", text="MOBILE NO.")
        self.Cust_Details_Table.heading("email", text="EMAIL")
        self.Cust_Details_Table.heading("nationality", text="NATIONALITY")
        self.Cust_Details_Table.heading("idproof", text="ID PROOF")
        self.Cust_Details_Table.heading("idnumber", text="ID NUMBER")
        self.Cust_Details_Table.heading("address", text="ADDRESS")

        self.Cust_Details_Table["show"]="headings"

#  Settig the width of columns

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#  Function to add data to the database and table usging mysql
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
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
                                "INSERT INTO customer (Ref, Name, Mother, Gender, PostCode, Mobile, Email, Nationality, IdProof, IdNumber, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                self.var_ref.get(),
                                self.var_cust.get(),
                                self.var_mother.get(),
                                self.var_gender.get(),
                                self.var_post.get(),
                                self.var_mobile.get(),
                                self.var_email.get(),
                                self.var_nationality.get(),
                                self.var_id_proof.get(),
                                self.var_id_number.get(),
                                self.var_address.get()
                                )
                        )
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Customer details added successfully", parent=self.root)
                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)
                except Exception as e:
                        messagebox.showerror("Error", f"Unexpected error: {str(e)}", parent=self.root)

       
            


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,events=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        self.var_ref.set(row[0])
        self.var_cust.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name = %s,Mother = %s, Gender= %s ,PostCode = %s , Mobile= %s, Email= %s, Nationality= %s, Idproof= %s, idnumber= %s , Address =%s where Ref = %s",  (
                                                        self.var_cust.get(),
                                                        self.var_mother.get(),
                                                        self.var_gender.get(),
                                                        self.var_post.get(),
                                                        self.var_mobile.get(),
                                                        self.var_email.get(),
                                                        self.var_nationality.get(),
                                                        self.var_id_proof.get(),
                                                        self.var_id_number.get(),
                                                        self.var_address.get(),
                                                        self.var_ref.get()
                                                ))
                
            conn.commit()
            self.fetch_data()  # to refresh the table
            conn.close()
            messagebox.showinfo("Success", "Customer details updated successfully", parent=self.root)
      


    def mdelete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if mdelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        # self.var_ref.set("")
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust.set("")
        self.var_mother.set("")
        # self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        # self.var_nationality.set("")
        # self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set(r"")         
         
    
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

if __name__ == "__main__":

    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
