from tkinter import *
from PIL import Image, ImageTk

class contactUs:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Title
        lbl_title = Label(self.root, text="CONTACT US", font=("times new roman", 18, "bold"), bg="blue", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=50, width=1295, height=500)

        # Left Label Frame for Contact Information
        labelframeleft = LabelFrame(main_frame, text="CONTACT US", font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        labelframeleft.place(x=5, y=5, width=950, height=480)

        # Contact Information
        contact_info = [
            "Name: ULTRA HOMES",
            "Founder: YADAV AND SON'S",
            "Established: 2002",
            "Location: VARANASI, UTTAR PRADESH",
            "Email: ULTRAHOME@GMAIL.COM",
            "Mobile No.: 9569768198",
            "Twitter: @ultrahomes",
            "Instagram: @ultrahomes",
            "Facebook: facebook.com/ultrahomes"
        ]

        y_pos = 20
        for info in contact_info:
            label = Label(labelframeleft, text=info, font=("times new roman", 12, "bold"), anchor="w")
            label.place(x=10, y=y_pos)
            y_pos += 30

        # Load and Display Logo Image on the Right Side
        logo_path = r"C:\Users\syshu\OneDrive\Desktop\Code_Era\3rd Year Projects\Hotel_Management_System\luxury-business-logo_1028264-5882.jpg"
        img = Image.open(logo_path)
        img = img.resize((300, 300), Image.Resampling.LANCZOS )
        self.photoimg = ImageTk.PhotoImage(img)

        logo_label = Label(main_frame, image=self.photoimg, bd=2, relief=RIDGE)
        logo_label.place(x=970, y=100, width=300, height=300)

        # Welcoming Quote
        self.quote = "Ultra Homes Your Comfort Our Priority"
        self.quote_label = Label(main_frame, text=self.quote, font=("times new roman", 14, "italic"), fg="white", bg="black")
        self.quote_label.place(x=970, y=250, width=300, height=50)

        # Start the fade-in animation
        self.fade_in(self.quote_label, 0)

    def fade_in(self, widget, alpha):
        fg_color = (255, 255, 255)  # White color
        bg_color = (0, 0, 0)        # Black color
        new_color = tuple(int(bg + (fg - bg) * alpha) for fg, bg in zip(fg_color, bg_color))
        hex_color = "#%02x%02x%02x" % new_color
        widget.config(fg=hex_color)
        if alpha < 1:
            alpha += 0.01
            self.root.after(10, self.fade_in, widget, alpha)

if __name__ == "__main__":
    root = Tk()
    obj = contactUs(root)
    root.mainloop()
