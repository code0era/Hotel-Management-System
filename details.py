from  tkinter import *
from PIL import  Image , ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



# Title

        lbl_title = Label(self.root, text="ROOM MANAGEMENT", font=("times new roman", 18, "bold"), bg="blue", fg="gold" , bd=4 , relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

# LOGO image
        img2 =  Image.open(r"C:\Users\syshu\OneDrive\Desktop\Code_Era\3rd Year Projects\Hotel_Management_System\luxury-business-logo_1028264-5882.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2 , bd = 4 , relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)
# Label Frame
        labelframeleft = LabelFrame(self.root, text="ADD ROOM  DETAILS", font=("times new roman", 12, "bold"), bd=2 , relief=RIDGE)
        labelframeleft.place(x=5, y=50, width=425, height=390)
# Floor No
        lbl_floor = Label(labelframeleft, text="Floor No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        entry_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, width=22, font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0, column=1)
#  Room 
        lbl_room = Label(labelframeleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room.grid(row=1, column=0, sticky=W)

        self.var_room = StringVar()
        entry_room = ttk.Entry(labelframeleft, textvariable=self.var_room, width=22, font=("times new roman", 13, "bold"))
        entry_room.grid(row=1, column=1)
# Room Type
        lbl_type = Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_type.grid(row=2, column=0, sticky=W)

        self.var_roomType = StringVar()
        combo_ROOM = ttk.Combobox(labelframeleft,textvariable=self.var_roomType, font=("times new roman", 12, "bold"), width=22)
        combo_ROOM["value"] = ("SINGLE", "DOUBLE","LUXURY")
        combo_ROOM.current(0)
        combo_ROOM.grid(row=2, column=1, sticky=W)

# btn frame

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=412, height=40)


        btnAdd = Button(btn_frame, text="ADD",command=self.add_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnAdd.grid(row=0 ,column=0,padx=3)
        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnUpdate.grid(row=0 ,column=1,padx=3)
        btnDelete = Button(btn_frame,text="DELETE" ,command=self.mdelete ,width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnDelete.grid(row=0 ,column=2,padx=3)
        btnReset = Button(btn_frame, text="RESET",command=self.reset, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="gold" , bd=0, relief=RIDGE , cursor="hand2")
        btnReset.grid(row=0 ,column=3 ,padx=3)

# table of details Frame search system
        Table_Frame = LabelFrame(self.root, text="VIEW AND SEARCH  DETAILS", font=("times new roman", 12, "bold"), bd=2 , relief=RIDGE)
        Table_Frame.place(x=450, y=50, width=800, height=390)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_Table = ttk.Treeview(Table_Frame,columns =("floor", "roomno","roomType" ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

#  Naming the columns

        self.room_Table.heading("floor", text="FLOOR NO")
        self.room_Table.heading("roomno", text="ROOM NO")
        self.room_Table.heading("roomType", text="ROOM TYPE")


        self.room_Table["show"]="headings"

#  Setting the width of columns

        self.room_Table.column("floor", width=100)
        self.room_Table.column("roomno", width=100)
        self.room_Table.column("roomType", width=100)

        
        self.room_Table.pack(fill=BOTH, expand=1)
        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

#  Function to add data to the database and table usging mysql
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomType.get() == "":
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
                                "INSERT INTO details VALUES (%s, %s, %s)",(
                                                                    self.var_floor.get(),
                                                                    self.var_room.get(),
                                                                    self.var_roomType.get(),
                                                                 
                                                                    ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "New Room details added successfully", parent=self.root)
                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)
                except Exception as e:
                        messagebox.showerror("Error", f"Unexpected error: {str(e)}", parent=self.root)


# fetch function 


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
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
        self.var_floor.set(row[0])
        self.var_room.set(row[1])
        self.var_roomType.set(row[2])
    

# Update function
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="3030", database="new_schema")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set  floor= %s ,roomType = %s where roomno = %s",  (
                                                                 
                                                                    self.var_floor.get(),
                                                                    self.var_roomType.get(), 
                                                                    self.var_room.get()              
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
            query = "delete from details where roomno=%s"
            value = (self.var_room.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
# reset function 
    def reset(self):
        self.var_floor.set(""),
        self.var_room.set(""),
        self.var_roomType.set(""), 
        


if __name__ == "__main__":



    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
