from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from Location import region
from Location import province_select
from Location import municipality_select
from Location import brgy_select
from datetime import datetime
from reportGenerator import exportCSV
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os
import json

# Main window
root = Tk()
root.geometry("1350x800")
root.title("Mabel - Log in or Sign up")
root.configure(bg="black")

# Adding an image
img = PhotoImage(file="images/mabel.png")
image_label = Label(root, image=img, bg="black")
image_label.place(x=230, y=190)

# Frame for the sign-in section
signin_frame = Frame(root, width=350, height=450, bg="white", relief="solid", bd=2.)
signin_frame.place(x=800, y=130)

# Heading for signin frame
signin_label = Label(signin_frame, text="Mabel", font=("Lucida Handwriting", 19, 'italic', 'bold'), bg="white",fg="#1c2026")
signin_label.place(x=120, y=20)

# Function for Username and Password Entry Enter and Leave
# When the user clicks the username entry, the label will disappear.
# If the user doesn't click anything and clicks the password entry, the label for the username will appear again.
# Vice versa

def enter(event):
    if username_entry.get() == "Phone number, username, or email":
        username_entry.delete(0, "end")
        username_entry.config(fg='black')

def leave(event):
    if username_entry.get() == '':
        username_entry.insert(0, "Phone number, username, or email")
        username_entry.config(fg='grey')

# For password, using the images button, the users are able to show and hide the password being input

def on_enter(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, "end")
        password_entry.config(fg='black', show="*")

def off_leave(event):
    if password_entry.get() == '':
        password_entry.insert(0, "Password")
        password_entry.config(fg='grey', show="")

def show_pass():
    global hide_button
    password_entry.config(show="")
    show_button.place_forget()
    hide_button = Button(signin_frame, image=hide, bg="white", bd=0, command=hide_pass, cursor="hand2")
    hide_button.place(x=280, y=150)

def hide_pass():
    password_entry.config(show="*")
    hide_button.place_forget()
    show_button = Button(signin_frame, image=show, bg="white", bd=0, command=show_pass, cursor="hand2")
    show_button.place(x=280, y=150)

img1 = PhotoImage(file="images/signin.png")
image1_label = Label(signin_frame, image=img1, bg="white")
image1_label.place(x=35, y=90)

username_entry = Entry(signin_frame, width=37, bd=0, bg="white", fg="black", font=("Cambria", 10))
username_entry.place(x=45, y=105)
username_entry.insert(0, "Phone number, username, or email")
username_entry.bind("<FocusIn>", enter)
username_entry.bind("<FocusOut>", leave)

img2 = PhotoImage(file="images/signin.png")
image2_label = Label(signin_frame, image=img2, bg="white")
image2_label.place(x=35, y=140)

password_entry = Entry(signin_frame, width=37, bd=0, bg="white", fg="black", font=("Cambria", 10), show="")
password_entry.place(x=45, y=155)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", on_enter)
password_entry.bind("<FocusOut>", off_leave)

show = PhotoImage(file="images/show.png")
hide = PhotoImage(file="images/hide.png")

show_button = Button(signin_frame, image=show, bg="white", bd=0, command=show_pass, cursor="hand2")
show_button.place(x=280, y=150)

# Forgot password label with underlined button
def underline_on_enter(event=None):
    current_font = forgot_button["font"]
    if "underline" not in current_font:
        current_font += " underline"
    forgot_button.config(font=current_font)

def remove_underline_on_leave(event=None):
    current_font = forgot_button["font"]
    if "underline" in current_font:
        current_font = current_font.replace("underline", "")
    forgot_button.config(font=current_font)

def ForgotPassword():
   resetPassword()

# New window for forgot password
def resetPassword():
    ReEntryPassword = Toplevel()
    ReEntryPassword.geometry("500x520")
    ReEntryPassword.title("Forgot your password?")
    ReEntryPassword.configure(bg="black")
    ReEntryPassword.iconbitmap("mabel.ico")

    # Adding Labels, Frames, Images
    forgotImage = PhotoImage(file="images/mabel2.png")
    forgotImage_label = Label(ReEntryPassword, image=forgotImage, bg="black")
    forgotImage_label.image = forgotImage
    forgotImage_label.place(x=230, y=20)

    firstLabel = Label(ReEntryPassword, text="Find your M account", font=("Arial", 15, "bold"), bg="black", fg="white")
    secondLabel = Label(ReEntryPassword, text="Enter the email, phone number, or username associated with", font=("Century", 9), bg="black", fg="gray")
    thirdLabel = Label(ReEntryPassword, text="your account account to change your password", font=("Century", 9), bg="black", fg="gray")

    firstLabel.place(x=75, y=75)
    secondLabel.place(x=75, y=105)
    thirdLabel.place(x=75, y=125)

    rounded2Image = PhotoImage(file="images/rounded2.png")
    rounded2Image_label = Label(ReEntryPassword, image=rounded2Image, bg="black")
    rounded2Image_label.image = rounded2Image  
    rounded2Image_label.place(x=65, y=150)

    forgotEntry = Entry(ReEntryPassword, width=37, bd=0, bg="black", fg="gray", font=("Cambria", 10))
    forgotEntry.place(x=95, y=175)
    forgotEntry.insert(0, "Email, phone number, or username")

    # Same as the sigin enter and leave
    def enterForgot(event):
        if forgotEntry.cget('fg') == 'gray':
            forgotEntry.delete(0, "end")
            forgotEntry.config(fg='white')

    def leaveForgot(event):
        if forgotEntry.get() == '':
            forgotEntry.insert(0, "Email, phone number, or username")
            forgotEntry.config(fg='gray')

    forgotEntry.bind("<FocusIn>", enterForgot)
    forgotEntry.bind("<FocusOut>", leaveForgot)

    nextForgot = PhotoImage(file="images/nextFogo.png")
    nextForgotImage_label = Label(ReEntryPassword, image=nextForgot, bg="black")
    nextForgotImage_label.image = nextForgot  
    nextForgotImage_label.place(x=65, y=400)

    # Next button for resetEntry password
    # When the user input his username then clicked next, he/she will able to change and create new password
    nextButton = Button(ReEntryPassword, text="Next", font=("Arial", 12, "bold"), bg="white", fg="black", activeforeground="black", cursor="hand2", activebackground="white", padx=135, pady=4, bd=0, command=lambda: changePassword(ReEntryPassword, forgotEntry.get()))
    nextButton.place(x=90, y=415)

# New window for New Password
def changePassword(ReEntryPassword, username):
    ReEntryPassword.destroy()
    changePass = Toplevel()
    changePass.geometry("500x520")
    changePass.title("Change your password")
    changePass.configure(bg="black")
    changePass.iconbitmap("mabel.ico")
    
    # Adding Labels, Images, Frames
    changePassImage = PhotoImage(file="images/mabel3.png")
    changePassImage_label = Label(changePass, image=changePassImage, bg="black")
    changePassImage_label.image = changePassImage
    changePassImage_label.place(x=230, y=20)

    reset1Label = Label(changePass, text="Reset Password", font=("Calibri", 17), bg="black", fg="white")
    reset2Label = Label(changePass, text="The password should have at least 6 characters", font=("Arial", 9), bg="black", fg="gray")
    reset3Label = Label(changePass, text="New Password", font=("Arial", 9, "bold"), bg="black", fg="white")
    reset4Label = Label(changePass, text="Confirm Password", font=("Arial", 9, "bold"), bg="black", fg="white")
    reset1Label.place(x=55, y=85)
    reset2Label.place(x=55, y=115)
    reset3Label.place(x=55, y=165)
    reset4Label.place(x=55, y=260)

    squareImage = PhotoImage(file="images/square.png")
    squareImage_label = Label(changePass, image=squareImage, bg="black")
    squareImage_label.image = squareImage  
    squareImage_label.place(x=42, y=182)

    square2Image = PhotoImage(file="images/square2.png")
    square2Image_label = Label(changePass, image=square2Image, bg="black")
    square2Image_label.image = square2Image  
    square2Image_label.place(x=42, y=277)

    toMake = Label(changePass, text="To make sure your account is secure, you'll be logged", font=("Consolas", 9), bg="black", fg="gray")
    toMake2 = Label(changePass, text="out from other devices once you set the new password.", font=("Consolas", 9), bg="black", fg="gray")
    toMake.place(x=50, y=440)
    toMake2.place(x=50, y=454)

    newpassword_entry = Entry(changePass, width=41, bd=0, bg="black", fg="white", font=("Cambria", 11), show="*")
    confirmpassword_entry = Entry(changePass, width=41, bd=0, bg="black", fg="white", font=("Cambria", 11), show="*")
    newpassword_entry.place(x=70, y=198, height=40)
    confirmpassword_entry.place(x=70, y=293, height=40)

    show3_img = PhotoImage(file="images/show3.png")
    hide3_img = PhotoImage(file="images/hide3.png")

    show3_button = Button(changePass, image=show3_img, bg="black", activebackground="black", activeforeground="white", bd=0, command=lambda: togglePass(show3_button, newpassword_entry, show3_img, hide3_img), cursor="hand2")
    show3_button.place(x=390, y=205)

    show4_img = PhotoImage(file="images/show4.png")
    hide4_img = PhotoImage(file="images/hide4.png")

    show4_button = Button(changePass, image=show4_img, bg="black", activebackground="black", activeforeground="white", bd=0, command=lambda: togglePass(show4_button, confirmpassword_entry, show4_img, hide4_img), cursor="hand2")
    show4_button.place(x=390, y=300)

    resetImage = PhotoImage(file="images/reset.png")
    resetImage_label = Label(changePass, image=resetImage, bg="black")
    resetImage_label.image = resetImage  
    resetImage_label.place(x=48, y=360)

    resetPassButton = Button(changePass, text="Reset password", font=("Arial", 12, "bold"), bg="white", fg="black", activeforeground="black", cursor="hand2", activebackground="white", padx=25, pady=4, bd=0, command=lambda: newPassword(newpassword_entry.get(), confirmpassword_entry.get(), username))
    resetPassButton.place(x=60, y=380)

# New Password and Confirm Password show and hide image button to see what is being inputted

def togglePass(button, entry, show_img, hide_img):
    if entry.cget('show') == '*':
        entry.config(show="")
        button.config(image=hide_img)
    else:
        entry.config(show="*")
        button.config(image=show_img)

# Automatically when the user changes his password, the password in the json file will change as well based on the password being created
def newPassword(new_password, confirm_password, username):
    if len(new_password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters")
        return

    if new_password!= confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    try:
        with open("finalproject.json", "r") as f:
            data = json.load(f)

        user_found = False
        for user in data["login_details"]:
            if user["username"] == username:
                user["password"] = new_password
                user_found = True
                break

        if not user_found:
            messagebox.showerror("Error", "Username not found")
            return

        with open("finalproject.json", "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Success", "Password reset successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", "An error occurred. Please check the console for more details.")

forgot_button = Button(signin_frame, text="Forgot password?", font=("Consolas", 9), cursor="hand2", fg="#36bfff", bd=0, bg="white", activebackground="white", activeforeground="#36bfff", command=lambda: ForgotPassword())
forgot_button.place(x=115, y=260)
forgot_button.bind("<Enter>", underline_on_enter)
forgot_button.bind("<Leave>", remove_underline_on_leave)

line_frame = Frame(signin_frame, bg="#cccecf", width=300)
line_frame.place(x=25, y=300)

# Button for creating new account to login
create_button = Button(signin_frame, width=17, pady=7, text="Create an account", font=("Book Antiqua", 12, "bold"), bd=0, cursor="hand2", bg="#3ddb45", fg="white", activebackground="#7a7d7b", activeforeground="white", command=lambda:createAccount())
create_button.place(x=90, y=320)

# Label for terms of service, privacy policy, and cookies use
termsLabel = Label(signin_frame, text="By signing up, you agree to the", font=("Arial", 8), bg="white", fg="gray")
terms2Label = Label(signin_frame, text="Terms of Service", font=("Arial", 8), bg="white", fg="#36bfff", cursor="hand2")
terms3Label = Label(signin_frame, text="and", font=("Arial", 8), bg="white", fg="gray")
terms4Label = Label(signin_frame, text="Privacy Policy", font=("Arial", 8), bg="white", fg="#36bfff", cursor="hand2")
terms5Label = Label(signin_frame, text=",", font=("Arial", 8), bg="white", fg="gray")
terms6Label = Label(signin_frame, text="including", font=("Arial", 8), bg="white", fg="gray")
terms7Label = Label(signin_frame, text="Cookie Use.", font=("Arial", 8), bg="white", fg="#36bfff", cursor="hand2")

termsLabel.place(x=40, y=380)
terms2Label.place(x=193,y=380)
terms3Label.place(x=278,y=380)
terms4Label.place(x=40,y=397)
terms5Label.place(x=110,y=397)
terms6Label.place(x=115,y=397)
terms7Label.place(x=162,y=397)

def createAccount():
    createWindows()

def createWindows():
    createWindow = Toplevel()
    createWindow.geometry("430x250")
    createWindow.title("Create an account")
    createWindow.configure(bg="black")
    createWindow.iconbitmap("mabel.ico")

    mabeLabel = Label(createWindow, text="Mabel", font=("Lucida Handwriting", 19, 'italic', 'bold'), bg="black",fg="white")
    mabeLabel.place(x=170, y=20)
    usernameLabel = Label(createWindow, text="Username", font=("Century", 12), bg="black", fg="white")
    passwordLabel = Label(createWindow, text="Password", font=("Century", 12), bg="black", fg="white")
    usernameLabel.place(x=30, y=87)
    passwordLabel.place(x=30, y=127)

    username_entry = Entry(createWindow, width=30, bd=0, bg="white", fg="black", font=("Cambria", 11))
    password_entry = Entry(createWindow, width=30, bd=0, bg="white", fg="black", font=("Cambria", 11), show="*")
    username_entry.place(x=130, y=85, height=27)
    password_entry.place(x=130, y=125, height=27)
    
    show_img = PhotoImage(file="images/show2.png")
    hide_img = PhotoImage(file="images/hide2.png")

    show_button = Button(createWindow, image=show_img, bg="white", bd=0, command=lambda: togglePassword(show_button), cursor="hand2")
    show_button.place(x=345, y=125)

    def togglePassword(button):
        if password_entry.cget('show') == '':
            password_entry.config(show="*")
            button.config(image=show_img)
        else:
            password_entry.config(show="")
            button.config(image=hide_img)
    
    crit = PhotoImage(file="images/crit.png")
    critImage_label = Label(createWindow, image=crit, bg="black")
    critImage_label.image = crit  
    critImage_label.place(x=150, y=180)


    def signup():
        username = username_entry.get()
        password = password_entry.get()

        file = "finalproject.json"
        try:
            with open(file, "r") as read_file:
                stud_rec = json.load(read_file)
        except FileNotFoundError:
            stud_rec = {"login_details": []}

        # Check if the username already exists
        for a in stud_rec["login_details"]:
            if a["username"] == username:
                messagebox.showerror("Error", "Username already exists")
                return

        # Create a new account
        new_account = {"username": username, "password": password}
        stud_rec["login_details"].append(new_account)

        with open(file, "w") as write_file:
            json.dump(stud_rec, write_file, indent=4)

        messagebox.showinfo("Success", "Account created successfully!")
        createWindow.destroy()

    upButton = Button(createWindow, text="Sign Up", bd=0, font=("Arial", 11, "bold"),bg="white", fg="black", activebackground="white", activeforeground="black", pady=4, padx=6, cursor="hand2", command=signup)
    upButton.place(x=187, y=192)

# Login Button
login_button = Button(signin_frame, width=38, pady=8, text="Log In", bd=0, cursor="hand2", activebackground="#36bfff", bg="#36bfff", fg="white", activeforeground="white", command=lambda: save_data())
login_button.place(x=38, y=210)

# THis is the function where the users are able to enter another window, which is the application form
# The login_details in the json file 
def save_data():
    username = username_entry.get()
    password = password_entry.get()

    filename = "finalproject.json"
    with open(filename, "r") as read_file:
        record_data = json.load(read_file)

    login_successful = False
    for i in record_data["login_details"]:
        if username == i["username"] and password == i["password"]:
            login_successful = True
            break

    if login_successful:
        messagebox.showinfo("Data Saved", "Login Successfully")
        root.withdraw()
        first_window()
    else:
        messagebox.showerror("Error", "Login Failed. Please try again.")

# Window for Student Scholarship Application Form
def first_window():
    first = Toplevel()
    first.geometry("1465x830")
    first.title("Student Scholarship Application Management System")
    first.configure(bg="black")

    tab_control = ttk.Notebook(first)
    style = ttk.Style()
    # Configure the style of the notebook tabs

    style.configure("TNotebook.Tab", font=("Cambria", 12), background="gray", foreground="black")
    
    # Create tabs
    tab1 = Frame(tab_control)
    tab2 = Frame(tab_control)
    tab_control.add(tab1, text="Application Form")
    tab_control.add(tab2, text="Application Information")
    tab_control.pack(expand=TRUE, fill=BOTH)
    tab1.configure(bg="black")
    tab2.configure(bg="black")

# TAB 1
    heading = PhotoImage(file="images/heading.png")
    heading_label = Label(tab1, image=heading, bg="black")
    heading_label.image = heading  
    heading_label.place(x=75, y=15)

    mabel4 = PhotoImage(file="images/mabel4.png")
    mabel4_label = Label(tab1, image=mabel4, bg="black")
    mabel4_label.image = mabel4  
    mabel4_label.place(x=115, y=45)

    applicationLabel = Label(tab1, text="M A B E L   S c h o l a r s h i p   A p p l i c a t i o n   F o r m   2 0 2 4 - 2 0 2 5", font=("Cambria", 20), bg="black", fg="yellow")
    applicationLabel.place(x=185, y=52)

    time = PhotoImage(file="images/time.png")
    time_label = Label(tab1, image=time, bg="black")
    time_label.image = time  
    time_label.place(x=1075, y=45)

    datetimeLabel = Label(first, text="", font=("Helvetica", 13), fg="white", bg="black")
    datetimeLabel.place(x=1145, y=85)

    def update_label():
        current_datetime = datetime.now()
        datetimeLabel.config(text=current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        first.after(1000, update_label) 

    update_label()

    perso = PhotoImage(file="images/perso.png")
    perso_label = Label(tab1, image=perso, bg="black")
    perso_label.image = perso  
    perso_label.place(x=40, y=130)

    persoFrame = Frame(tab1, width=560, height=340, bg="black")
    persoFrame.place(x=66, y=215)

    personalLabel = Label(tab1, text="Personal Information", font=("Arial", 13, "bold"), bg="#FFC000", fg="black") 
    personalLabel.place(x=75, y=155)
    
    nameLabel = Label(persoFrame, text="Name", font=("Century", 11), bg="black", fg="white")
    birthdateLabel = Label(persoFrame, text="Birthdate", font=("Century", 11), bg="black", fg="white")
    birthplaceLabel =  Label(persoFrame, text="Place of Birth", font=("Century", 11), bg="black", fg="white")
    sexLabel =  Label(persoFrame, text="Sex", font=("Century", 11), bg="black", fg="white")
    statusLabel =  Label(persoFrame, text="Civil Status", font=("Century", 11), bg="black", fg="white")
    regionLabel = Label(persoFrame, text="Region", font=("Century", 11), bg="black", fg="white")
    provinceLabel = Label(persoFrame, text="Provice", font=("Century", 11), bg="black", fg="white")
    municipality_label =  Label(persoFrame, text="Municipality", font=("Century", 11), bg="black", fg="white")
    barangayLabel =  Label(persoFrame, text="Barangay", font=("Century", 11), bg="black", fg="white")
    codeLabel =  Label(persoFrame, text="Zip Code", font=("Century", 11), bg="black", fg="white")
    numberLabel =  Label(persoFrame, text="Mobile No.", font=("Century", 11), bg="black", fg="white")
    emailLabel =  Label(persoFrame, text="Email", font=("Century", 11), bg="black", fg="white")
    fbLabel =  Label(persoFrame, text="Facebook Name/Username", font=("Century", 11), bg="black", fg="white")

    nameLabel.place(x=10, y=10)
    birthdateLabel.place(x=10, y=75)
    birthplaceLabel.place(x=180, y=75)
    sexLabel.place(x=400, y=75)
    statusLabel.place(x=10, y=135)
    regionLabel.place(x=160, y=135)
    provinceLabel.place(x=350, y=135)
    municipality_label.place(x=10, y=195)
    barangayLabel.place(x=190, y=195)
    codeLabel.place(x=370, y=195)
    numberLabel.place(x=10, y=255)
    emailLabel.place(x=170, y=255)
    fbLabel.place(x=340, y=255)

    nameEntry = Entry(persoFrame,font=("Cambria", 10), bd=0, width=30)
    birthdateEntry = DateEntry(persoFrame, font=("Cambria", 10), width=18, cursor="hand2") 
    birthplaceEntry = Entry(persoFrame,font=("Cambria", 10), bd=0, width=28)
    sexValues = ["Male", "Female"]
    sexCombobox = ttk.Combobox(persoFrame, width=19, values=sexValues, cursor="hand2")
    sexCombobox["state"]= "readonly"  
    statusValues = ["Single", "Married", "Widowed", "Annulled", "Separated", "Others"]
    statusCombobox = ttk.Combobox(persoFrame, width=17, values=statusValues, cursor="hand2")
    statusCombobox["state"]= "readonly"  
    codeSpinbox = Spinbox(persoFrame,font=("Cambria", 10), from_=0, width=22, to=10000, increment=1, cursor="hand2")
    numberEntry = Entry(persoFrame,font=("Cambria", 10), bd=0 )
    emailEntry = Entry(persoFrame,font=("Cambria", 10), width=21, bd=0 )
    fbEntry = Entry(persoFrame,font=("Cambria", 10), bd=0, width=28)

    nameEntry.place(x=12, y=40, height=20)
    birthdateEntry.place(x=12, y=105)
    birthplaceEntry.place(x=182, y=105, height=20)
    sexCombobox.place(x=402, y=105)
    statusCombobox.place(x=12, y=165)
    codeSpinbox.place(x=372, y=225)
    numberEntry.place(x=12, y=285, height=20)
    emailEntry.place(x=172, y=285, height=20)
    fbEntry.place(x=342, y=285, height=20)

    regionCombo = ttk.Combobox(persoFrame, values = region,  font=("Cambria", 10), width=20, cursor="hand2")
    regionCombo.place(x=162,y=165)

    def region_selector(event):
        selected_region = regionCombo.get()
        province = province_select(selected_region)
        provinceCombo.configure(values=province)
      
    regionCombo.bind("<<ComboboxSelected>>",region_selector)

    def province_selector(event):
        selected_region = regionCombo.get()
        selected_province = provinceCombo.get()
        municipality = municipality_select(selected_region, selected_province)
        cityCombo.configure(values=municipality)

    province = list()
    municipality = list()
    brgy = list()
    
    provinceCombo = ttk.Combobox(persoFrame, values=province,  font=("Cambria", 10), width=24, cursor="hand2")
    provinceCombo.place(x=352,y=165)
    provinceCombo.bind("<<ComboboxSelected>>", province_selector)

    def city_selector(event):
        selected_region = regionCombo.get()
        selected_province = provinceCombo.get()
        selected_city = cityCombo.get()

        brgy = brgy_select(selected_region, selected_province, selected_city)
        brgyCombo.configure(values=brgy)

    cityCombo = ttk.Combobox(persoFrame, font=("Cambria", 10), width=19, cursor="hand2")
    cityCombo.place(x=12,y=225)
    cityCombo.bind("<<ComboboxSelected>>", city_selector)

    brgyCombo = ttk.Combobox(persoFrame, font=("Cambria", 10), width=19, cursor="hand2")
    brgyCombo.place(x=192,y=225)

    
    perso2 = PhotoImage(file="images/perso2.png")
    perso2_label = Label(tab1, image=perso2, bg="black")
    perso2_label.image = perso2
    perso2_label.place(x=45, y=580)

    personal2Label = Label(tab1, text="Family Background", font=("Arial", 13, "bold"), bg="#FFC000", fg="black") 
    personal2Label.place(x=75, y=603)

    perso2Frame = Frame(tab1, width=560, height=120, bg="black")
    perso2Frame.place(x=65, y=655)
    
    fatherLabel = Label(perso2Frame, text="Father's Name", font=("Century", 11), bg="black", fg="white")
    occupationLabel = Label(perso2Frame, text="Occupation", font=("Century", 11), bg="black", fg="white")
    motherLabel = Label(perso2Frame, text="Mother's Name", font=("Century", 11), bg="black", fg="white")
    occupation2Label = Label(perso2Frame, text="Occupation", font=("Century", 11), bg="black", fg="white")
    siblingsLabel = Label(perso2Frame, text="No. of Siblings", font=("Century", 11), bg="black", fg="white")
    incomeLabel = Label(perso2Frame, text="Parent(s) Annual Gross of Income", font=("Century", 11), bg="black", fg="white")

    fatherLabel.place(x=10, y=10)
    occupationLabel.place(x=300, y=10)
    motherLabel.place(x=10, y=50)
    occupation2Label.place(x=300, y=50)
    siblingsLabel.place(x=10, y=90)
    incomeLabel.place(x=180, y=90)
    
    fatherEntry = Entry(perso2Frame,font=("Cambria", 10), bd=0)
    occupationEntry = Entry(perso2Frame,font=("Cambria", 10), bd=0)
    motherEntry = Entry(perso2Frame,font=("Cambria", 10), bd=0)
    occupation2Entry = Entry(perso2Frame,font=("Cambria", 10), bd=0) 
    siblingsEntry= Entry(perso2Frame,font=("Cambria", 10), bd=0, width=5)
    incomeEntry = Entry(perso2Frame,font=("Cambria", 10), bd=0, width=15)

    fatherEntry.place(x=130, y=15)
    occupationEntry.place(x=400, y=15)
    motherEntry.place(x=130, y=55)
    occupation2Entry.place(x=400, y=55)
    siblingsEntry.place(x=130, y=95)
    incomeEntry.place(x=436, y=95)
           
    perso3 = PhotoImage(file="images/perso3.png")
    perso3_label = Label(tab1, image=perso3, bg="black")
    perso3_label.image = perso3
    perso3_label.place(x=642, y=127)
    
    personal3Label = Label(tab1, text="Academic Information", font=("Arial", 13, "bold"), bg="#FFC000", fg="black") 
    personal3Label.place(x=670, y=155)
    
    perso3Frame = Frame(tab1, width=500, height=170, bg="black")
    perso3Frame.place(x=670, y=210)
    
    typeLabel = Label(perso3Frame, text="Application Type", font=("Century", 11), bg="black", fg="white")
    lrnLabel = Label(perso3Frame, text="LRN", font=("Century", 11), bg="black", fg="white")
    schoolLabel = Label(perso3Frame, text="Name of School Last Attended", font=("Century", 11), bg="black", fg="white")
    gwaLabel = Label(perso3Frame, text="GWA", font=("Century", 11), bg="black", fg="white")
    collegeLabel = Label(perso3Frame, text="Prospective College", font=("Century", 11), bg="black", fg="white")
    degreeLabel = Label(perso3Frame, text="Course", font=("Century", 11), bg="black", fg="white")
    typeLabel.place(x=10, y=10)
    lrnLabel.place(x=300, y=10)
    schoolLabel.place(x=10, y=50)
    gwaLabel.place(x=400, y=50)
    collegeLabel.place(x=10, y=90)
    degreeLabel.place(x=10, y=130)

    typeValues = ["Senior/High School Graduate", "Graduating Senior High"]
    typeCombobox = ttk.Combobox(perso3Frame, width=19, values=typeValues, cursor="hand2")
    typeCombobox["state"]= "readonly" 
    lrnEntry = Entry(perso3Frame,font=("Cambria", 10), bd=0)
    schoolEntry = Entry(perso3Frame,font=("Cambria", 10), bd=0)
    gwaEntry = Entry(perso3Frame,font=("Cambria", 10), bd=0, width=5)
    collegeEntry = Entry(perso3Frame,font=("Cambria", 10), bd=0, width=46)
    degreeEntry = Entry(perso3Frame,font=("Cambria", 10), bd=0, width=59)

    typeCombobox.place(x=150, y=15)
    lrnEntry.place(x=350, y=15)
    schoolEntry.place(x=245, y=55)
    gwaEntry.place(x=455, y=55)
    collegeEntry.place(x=167, y=95)
    degreeEntry.place(x=77, y=135)

    perso4 = PhotoImage(file="images/perso4.png")
    perso4_label = Label(tab1, image=perso4, bg="black")
    perso4_label.image = perso4  
    perso4_label.place(x=642, y=405)

    personal4Label = Label(tab1, text="Additional Academic Information", font=("Arial", 13, "bold"), bg="#FFC000", fg="black") 
    personal4Label.place(x=670, y=428)

    perso4Frame = Frame(tab1, width=500, height=85, bg="black")
    perso4Frame.place(x=670, y=490)

    askLabel =  Label(perso4Frame, text="Are you enjoying other source of educational/financial assistance?", font=("Century", 11), bg="black", fg="white")
    askLabel.place(x=5, y=5)
    yesnoVar = StringVar()
    yesRadiobutton = Radiobutton(perso4Frame, text="Yes", font=("Cambria", 10), variable=yesnoVar, value="Yes", cursor="hand2")
    noRadiobutton = Radiobutton(perso4Frame, text="No", font=("Cambria", 10), variable=yesnoVar, value="No", cursor="hand2")
    yesRadiobutton.place(x=100, y=50)
    noRadiobutton.place(x=300, y=50)

    perso5 = PhotoImage(file="images/perso5.png")
    perso5_label = Label(tab1, image=perso5, bg="black")
    perso5_label.image = perso5  
    perso5_label.place(x=1195, y=125)

    personal5Label = Label(tab1, text="Attachments", font=("Arial", 13, "bold"), bg="#FFC000", fg="black") 
    personal5Label.place(x=1240, y=155)

    perso5Frame = Frame(tab1, width=150, height=370, bg="black")
    perso5Frame.place(x=1220, y=205)

    picture2Label = Label(perso5Frame, text="2x2 Picture", font=("Century", 6, "italic"), bg="black", fg="white")
    certificate2Label = Label(perso5Frame, text="Birth Certificate", font=("Century", 6, "italic"), bg="black", fg="white")
    card2Label = Label(perso5Frame, text="Report Card", font=("Century", 6, "italic"), bg="black", fg="white")
    income2Label = Label(perso5Frame, text="Proof of Income", font=("Century", 6, "italic"), bg="black", fg="white")

    picture2Label.place(x=92, y=7)
    certificate2Label.place(x=83, y=102)
    card2Label.place(x=90, y=192)
    income2Label.place(x=85, y=290)

    # Images for uploading attachments and documents
    picture = PhotoImage(file="images/picture.png")
    picture_label = Label(perso5Frame, image=picture, bg="black")
    picture_label.image = picture  
    picture_label.place(x=0, y=5)
    
    certificate = PhotoImage(file="images/certificate.png")
    certificate_label = Label(perso5Frame, image=certificate, bg="black")
    certificate_label.image = certificate  
    certificate_label.place(x=0, y=95)

    card = PhotoImage(file="images/card.png")
    card_label = Label(perso5Frame, image=card, bg="black")
    card_label.image = card  
    card_label.place(x=0, y=190)

    income = PhotoImage(file="images/income.png")
    income_label = Label(perso5Frame, image=income, bg="black")
    income_label.image = income  
    income_label.place(x=0, y=285)

    # When users browse a picture on their computer and upload it to the application form, clicking that photo in the interface will open a new window to zoom in on it.

    def open_image(image_path):
        new_window = Toplevel(root)
        new_window.title("Student Information")
        new_window.configure(bg="white")
        new_window.iconbitmap("student.ico")
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        img_label = Label(new_window, image=img)
        img_label.image = img
        img_label.pack()

    def browse_picture():
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")])
        if filepath:
            img = Image.open(filepath)
            img = img.resize((80, 80), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            picture_label.config(image=img)
            picture_label.image = img
            picture_label.bind("<Button-1>", lambda e: open_image(filepath))

    def browse_certificate():
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")])
        if filepath:
            img = Image.open(filepath)
            img = img.resize((80, 80), Image.Resampling.LANCZOS) 
            img = ImageTk.PhotoImage(img)
            certificate_label.config(image=img)
            certificate_label.image = img
            certificate_label.bind("<Button-1>", lambda e: open_image(filepath))

    def browse_card():
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")])
        if filepath:
            img = Image.open(filepath)
            img = img.resize((80, 80), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            card_label.config(image=img)
            card_label.image = img
            card_label.bind("<Button-1>", lambda e: open_image(filepath))

    def browse_income():
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")])
        if filepath:
            img = Image.open(filepath)
            img = img.resize((70, 70), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            income_label.config(image=img)
            income_label.image = img
            income_label.bind("<Button-1>", lambda e: open_image(filepath))

    # Browse Buttons
    pictureButton = Button(perso5Frame, text="Browse", font=("Arial", 10), bd=0, bg="gray", fg="black", cursor="hand2", command=browse_picture)
    pictureButton.place(x=93, y=30)

    certificateButton = Button(perso5Frame, text="Browse", font=("Arial", 10), bd=0, bg="gray", fg="black", cursor="hand2", command=browse_certificate)
    certificateButton.place(x=93, y=125)

    cardButton = Button(perso5Frame, text="Browse", font=("Arial", 10), bd=0, bg="gray", fg="black", cursor="hand2", command=browse_card)
    cardButton.place(x=93, y=215)

    incomeButton = Button(perso5Frame, text="Browse", font=("Arial", 10), bd=0, bg="gray", fg="black", cursor="hand2", command=browse_income)
    incomeButton.place(x=93, y=310)

    # To reset the picture and re-uploaded
    def reset_picture():
        picture_label.config(image=picture)
        picture_label.image = picture
        picture_label.unbind("<Button-1>")

    def reset_certificate():
        certificate_label.config(image=certificate)
        certificate_label.image = certificate
        certificate_label.unbind("<Button-1>")

    def reset_card():
        card_label.config(image=card)
        card_label.image = card
        card_label.unbind("<Button-1>")


    def reset_income():
        income_label.config(image=income)
        income_label.image = income
        income_label.unbind("<Button-1>")

    # Reset Buttons
    resetpictureButton = Button(perso5Frame, text="Reset", font=("Arial", 10), bd=0,  padx=6, bg="gray", fg="black", cursor="hand2", command=lambda: reset_picture())
    resetpictureButton.place(x=93, y=60)

    resetcertificateButton = Button(perso5Frame, text="Reset", font=("Arial", 10),bd=0,  padx=6, bg="gray", fg="black", cursor="hand2", command=lambda: reset_certificate())
    resetcertificateButton.place(x=93, y=155)

    resetcardButton = Button(perso5Frame, text="Reset", font=("Arial", 10),bd=0,  padx=6, bg="gray", fg="black", cursor="hand2", command=lambda: reset_card())
    resetcardButton.place(x=93, y=245)

    resetincomeButton = Button(perso5Frame, text="Reset",font=("Arial", 10),bd=0, padx=6, bg="gray", fg="black", cursor="hand2", command=lambda: reset_income())
    resetincomeButton.place(x=93, y=340)

    perso6 = PhotoImage(file="images/perso6.png")
    perso6_label = Label(tab1, image=perso6, bg="black")
    perso6_label.image = perso6  
    perso6_label.place(x=640, y=592)

    perso6Frame = Frame(tab1, width=714, height=165, bg="white")
    perso6Frame.place(x=660, y=615)

    herebyValue = IntVar()
    herebyCheckbutton = Checkbutton(perso6Frame, text="", font=("Cambria", 9), bd=0, bg="white", fg="black", activebackground="white", activeforeground="black", cursor="hand2", variable=herebyValue,onvalue=1, offvalue=0)
    herebyCheckbutton.place(x=10, y=10)

    herebyLabel1 = Label(perso6Frame, text="I hereby certify that foregoing statements are true and correct. Any misinformation or witholding of information will", font=("Century", 9, "italic"), bg="white", fg="black")
    herebyLabel2 = Label(perso6Frame, text="automatically disqualify me from the MABEL Scholarship Program. I am willing to refund the financial benefits received if", font=("Century", 9, "italic"), bg="white", fg="black")
    herebyLabel3 = Label(perso6Frame, text="such information is discovered after acceptance of the award.", font=("Century", 9, "italic"), bg="white", fg="black")
    herebyLabel4 = Label(perso6Frame, text="I hereby express my consent to collect, record, organize, update or modify, retrieve, consult, use, consolidate, block, erase or", font=("Century", 9, "italic"), bg="white", fg="black")
    herebyLabel5 = Label(perso6Frame, text="destruct my personal data as part of my information. ", font=("Century", 9, "italic"), bg="white", fg="black")
    herebyLabel1.place(x=30, y=8)
    herebyLabel2.place(x=10, y=28)
    herebyLabel3.place(x=10, y=48)
    herebyLabel4.place(x=10, y=78)
    herebyLabel5.place(x=10, y=98)

    # Submit Application Button Border
    submitApp = PhotoImage(file="images/submit.png")
    submitApp_label = Label(perso6Frame, image=submitApp, bg="white")
    submitApp_label.image = submitApp  
    submitApp_label.place(x=500, y=118)

    # Cancel Button Border
    cancelApp = PhotoImage(file="images/cancel.png")
    cancelApp_label = Label(perso6Frame, image=cancelApp, bg="white")
    cancelApp_label.image = cancelApp  
    cancelApp_label.place(x=400, y=115)

# TAB 2
    heading2 = PhotoImage(file="images/heading2.png")
    heading2_label = Label(tab2, image=heading2, bg="black")
    heading2_label.image = heading2
    heading2_label.place(x=75, y=15)

    mabel5 = PhotoImage(file="images/mabel5.png")
    mabel5_label = Label(tab2, image=mabel5, bg="black")
    mabel5_label.image = mabel5
    mabel5_label.place(x=115, y=45)

    application2Label = Label(tab2, text="M A B E L   S c h o l a r s h i p   A p p l i c a t i o n   F o r m   2 0 2 4 - 2 0 2 5", font=("Cambria", 20), bg="black", fg="yellow")
    application2Label.place(x=185, y=52)

    time2 = PhotoImage(file="images/time2.png")
    time2_label = Label(tab2, image=time2, bg="black")
    time2_label.image = time2  
    time2_label.place(x=1075, y=45)

    perso7 = PhotoImage(file="images/perso7.png")
    perso7_label = Label(tab2, image=perso7, bg="black")
    perso7_label.image = perso7  
    perso7_label.place(x=45, y=130)

    search = PhotoImage(file="images/search.png")
    search_label = Label(tab2, image=search, bg="#FFC000")
    search_label.image = search
    search_label.place(x=1020, y=147)

    perso7Frame = Frame(tab2, width=1312, height=425, bg="black")
    perso7Frame.place(x=60, y=222)
    perso7Frame.pack_propagate()

    # Create columns
    myColumns = ("Name", "Birthdate", "Place of Birth", "Sex","Status", "Region", "Province","Municipality", "Barangay", "Code","Number","Email","Facebook Name","Father","Occupation1","Mother", "Occupation2", "Siblings", "Annual Income", "Type", "LRN", "Last Attended", "GWA", "College", "Course", "Other")
    DataView = ttk.Treeview(perso7Frame, columns=myColumns, show="headings", height=21)

    # Customize the size of the columns
    DataView.column("Name", stretch=False, width=50)
    DataView.column("Birthdate", stretch=False, width=58)
    DataView.column("Place of Birth", stretch=False, width=80)
    DataView.column("Sex", stretch=False, width=40)
    DataView.column("Status", stretch=False, width=45)
    DataView.column("Region", stretch=False, width=50)
    DataView.column("Province", stretch=False, width=55)
    DataView.column("Municipality", stretch=False, width=75)
    DataView.column("Barangay", stretch=False, width=55)
    DataView.column("Code", stretch=False, width=35)
    DataView.column("Number", stretch=False, width=55)
    DataView.column("Email", stretch=False, width=40)
    DataView.column("Facebook Name", stretch=False, width=50)
    DataView.column("Father", stretch=False, width=50)
    DataView.column("Occupation1", stretch=False, width=50)
    DataView.column("Mother", stretch=False, width=50)
    DataView.column("Occupation2", stretch=False, width=50)
    DataView.column("Siblings", stretch=False, width=50)
    DataView.column("Annual Income", stretch=False, width=50)
    DataView.column("Type", stretch=False, width=40)
    DataView.column("LRN", stretch=False, width=40)
    DataView.column("Last Attended", stretch=False, width=50)
    DataView.column("GWA", stretch=False, width=50)
    DataView.column("College", stretch=False, width=50)
    DataView.column("Course", stretch=False, width=50)
    DataView.column("Other", stretch=False, width=50)

    DataView.heading("Name", text="Name")
    DataView.heading("Birthdate", text="Birthdate" )
    DataView.heading("Place of Birth", text="Place of Birth" )
    DataView.heading("Sex", text="Sex")
    DataView.heading("Status", text="Status")
    DataView.heading("Region", text="Region")
    DataView.heading("Province", text="Province")
    DataView.heading("Municipality", text="Municipality" )
    DataView.heading("Barangay", text="Barangay")
    DataView.heading("Code", text="Code")
    DataView.heading("Number", text="Number")
    DataView.heading("Email", text="Email")
    DataView.heading("Facebook Name", text="Facebook Name")
    DataView.heading("Father", text="Father")
    DataView.heading("Occupation1", text="Occupation1")
    DataView.heading("Mother",  text="Mother")
    DataView.heading("Occupation2", text="Occupation2")
    DataView.heading("Siblings", text="Siblings")
    DataView.heading("Annual Income", text="Annual Income")
    DataView.heading("Type",  text="Type")
    DataView.heading("LRN", text="LRN")
    DataView.heading("Last Attended", text="Last Attended")
    DataView.heading("GWA", text="GWA")
    DataView.heading("College", text="College")
    DataView.heading("Course", text="Course")
    DataView.heading("Other", text="Other")
    DataView.place(x=0, y=0)
    
    # Submit Button
    submitButton = Button(perso6Frame,  text="Submit Application",font=("Arial", 11), padx=20, bd=0, cursor="hand2", bg="#007AD6", fg="white", command=lambda: submitApplicationData())
    submitButton.place(x=510, y=130)

    # Cancel Button
    cancelButton = Button(perso6Frame,  text="Cancel",font=("Arial", 11), bd=0, cursor="hand2", bg="#D0CECE", fg="black")
    cancelButton.place(x=417, y=129)

    searchEntry = Entry(tab2, font=("Cambria", 11), bd=0, width=35, fg='gray')
    searchEntry.place(x=1070, y=160, height=25)

    # Event used in search the json file for the information typed on the search entry input.
    def keyRelease(event):
      searchTerm = searchEntry.get()
      update_treeview(searchTerm)

    # Event handling for when a user types something into the entry and releases the keyboard
    searchEntry.bind("<KeyRelease>", keyRelease)
    searchIcon = PhotoImage(file="images/searchIcon.png")

    # Search Button
    searchButton = Button(tab2, image=searchIcon, bg="white", borderwidth=0, activebackground="white",cursor="hand2", command=lambda: update_treeview(searchEntry.get()))
    searchButton.image = searchIcon
    searchButton.place(x=1035, y=157)

    buttons = PhotoImage(file="images/buttons.png")
    buttons_label = Label(tab2, image=buttons, bg="black")
    buttons_label.image = buttons
    buttons_label.place(x=540, y=662)

    # Edit Button
    editButton = Button(tab2, text="Edit", font=("Arial", 12, "bold"), padx=40, pady=8, bd=0, bg="black", fg="white",activebackground="black", activeforeground="white", cursor="hand2", command=lambda: editData())
    editButton.place(x=580, y=705)

    # Update Button
    updateButton = Button(tab2, text="Update", font=("Arial", 12, "bold"), bd=0, padx=30, pady=8, bg="black", fg="white",activebackground="black", activeforeground="white", cursor="hand2", command=lambda: updateData())
    updateButton.place(x=742, y=705)

    # Delete Button
    deleteButton = Button(tab2, text="Delete", font=("Arial", 12, "bold"), bd=0, padx=30, pady=8,bg="black", fg="white",activebackground="black", activeforeground="white", cursor="hand2", command=lambda: deleteData())
    deleteButton.place(x=905, y=705)

    # Print Button
    printButton = Button(tab2, text="Export to CSV", font=("Arial", 12, "bold"),pady=8, bd=0, bg="black", fg="white",activebackground="black", activeforeground="white", cursor="hand2", command=lambda: printData())
    printButton.place(x=1070, y=705)

    # Pdf Button
    pdfButton = Button(tab2, text="Export to PDF", font=("Arial", 12, "bold"), pady=8, bd=0, bg="black", fg="white",activebackground="black", activeforeground="white", cursor="hand2", command=lambda: pdfData())
    pdfButton.place(x=1232, y=705)

    # Another Labels and Images 
    fishingTouch = PhotoImage(file="images/fishingTouch.png")
    fishingTouch_label = Label(tab2, image=fishingTouch, bg="black")
    fishingTouch_label.image = fishingTouch  
    fishingTouch_label.place(x=45, y=660)

    fishingFrame = Frame(tab2, width=380, height=100, bg="black")
    fishingFrame.place(x=95, y=677)
    
    fishingLabel = Label(fishingFrame, text="2024 MABEL UNDERGRADUATE SCHOLARSHIPS", font=("Lucida Handwriting", 10, 'italic', 'bold'), bg="black",fg="white")
    fishing2Label = Label(fishingFrame, text="W I L L   B E   R E L E A S E D   O N", font=("Arial", 9, 'bold'), bg="black",fg="#FFC000")
    fishing3Label = Label(fishingFrame, text="07.15.24", font=("Cambria", 19, 'bold'), bg="black",fg="white")

    fishingLabel.place(x=0, y=10)
    fishing2Label.place(x=90, y=37)
    fishing3Label.place(x=130, y=60)

    # Fetch the data from widgets and set a variable 
    def submitApplicationData():
        name = nameEntry.get()
        birthdate = birthdateEntry.get()
        birthplace = birthplaceEntry.get()
        sex = sexCombobox.get()
        status = statusCombobox.get()
        region = regionCombo.get()
        province = provinceCombo.get()
        city = cityCombo.get()
        brgy = brgyCombo.get()
        code = codeSpinbox.get()
        number = numberEntry.get()
        email = emailEntry.get()
        fb = fbEntry.get()
        father = fatherEntry.get()
        occupation1 = occupationEntry.get()
        mother = motherEntry.get()
        occupation2 = occupation2Entry.get()
        siblings = siblingsEntry.get()
        income = incomeEntry.get()
        application = typeCombobox.get()
        lrn = lrnEntry.get()
        school = schoolEntry.get()
        gwa = gwaEntry.get()
        college = collegeEntry.get()
        degree = degreeEntry.get()
        yesno = yesnoVar.get()

        picture_label.config(image=picture)
        certificate_label.config(image=certificate)
        card_label.config(image=card)
        reset_income() 
        picture_label.unbind("<Button-1>")
        certificate_label.unbind("<Button-1>")
        card_label.unbind("<Button-1>")
        income_label.unbind("<Button-1>")
        
        studentInfo = {
            "name": name,
            "birthdate": birthdate,
            "birthplace": birthplace,
            "sex": sex,
            "status": status,
            "region": region,
            "province": province,
            "city": city,
            "brgy": brgy,
            "code": code,
            "number": number,
            "email": email,
            "fb": fb,
            "father": father,
            "occupation1": occupation1,
            "mother": mother,
            "occupation2": occupation2,
            "siblings": siblings,
            "income": income,
            "application": application,
            "lrn": lrn,
            "school": school,
            "gwa": gwa,
            "college": college,
            "degree": degree,
            "yesno": yesno
        }

        filename = "student_record.json"
        if os.path.exists(filename):
             with open(filename,'r') as readFile:
              data = json.load(readFile)
        else:
            data = {"student_record":[]}
            with open(filename,'w') as createFile:
                json.dump(data, createFile,indent=4)
        
        data["student_record"].append(studentInfo)

        with open(filename, 'w') as updateFile:
            json.dump(data, updateFile, indent=4)

        messagebox.showinfo("RECORD", "DATA SAVED SUCCESSFULLY")
        updateTreeview()
        clearWidgets()

    def updateTreeview():
        for item in DataView.get_children():
            DataView.delete(item)

        with open("student_record.json") as openFile:
            info = json.load(openFile)

        for each_info in info["student_record"]:
            DataView.insert("","end", values=((each_info["name"],each_info["birthdate"],each_info["birthplace"],each_info["sex"],each_info["status"], each_info["region"],each_info["province"],each_info["city"],each_info["brgy"],each_info["code"],each_info["number"],each_info["email"],each_info["fb"],each_info["father"],each_info["occupation1"],each_info["mother"],each_info["occupation2"],each_info["siblings"],each_info["income"],each_info["application"],each_info["lrn"],each_info["school"],each_info["gwa"],each_info["college"],each_info["degree"],each_info["yesno"])))

    # Function for clearing the input widgets 
    def clearWidgets():
        nameEntry.delete(0, END)
        birthdateEntry.delete(0, END)
        birthplaceEntry.delete(0, END)
        sexCombobox.set("")
        statusCombobox.set("")
        regionCombo.set("")
        provinceCombo.set("")
        cityCombo.set("")
        brgyCombo.set("")
        codeSpinbox.delete(0, END)
        numberEntry.delete(0, END)
        emailEntry.delete(0, END)
        fbEntry.delete(0, END)
        fatherEntry.delete(0, END)
        occupationEntry.delete(0, END)
        motherEntry.delete(0, END)
        occupation2Entry.delete(0, END)
        siblingsEntry.delete(0, END)
        incomeEntry.delete(0, END)
        typeCombobox.set("")
        lrnEntry.delete(0, END)
        schoolEntry.delete(0, END)
        gwaEntry.delete(0, END)
        collegeEntry.delete(0, END)
        degreeEntry.delete(0, END)
        yesnoVar.set("")
    
    def update_treeview(searchTerm = ""):
        # Clear the treeview
        for item in DataView.get_children():
            DataView.delete(item)

        # Filter the data based on the search term
        with open("student_record.json", "r") as readFile:
            datas = json.load(readFile)
        
        filteredData = [] 
        for info in datas["student_record"]:
            if searchTerm.lower() in info["name"] or info["name"].lower().startswith(searchTerm.lower()):
                filteredData.append(info)

        # Isert the filtered data into the treeview
        for each_info in filteredData:
            DataView.insert("","end", values=((each_info["name"],each_info["birthdate"],each_info["birthplace"],each_info["sex"],each_info["status"], each_info["region"],each_info["province"],each_info["city"],each_info["brgy"],each_info["code"],each_info["number"],each_info["email"],each_info["fb"],each_info["father"],each_info["occupation1"],each_info["mother"],each_info["occupation2"],each_info["siblings"],each_info["income"],each_info["application"],each_info["lrn"],each_info["school"],each_info["gwa"],each_info["college"],each_info["degree"],each_info["yesno"])))

    def printData():
        with open("student_record.json", "r") as read_file:
            data = json.load(read_file)

        exportCSV(data)
        messagebox.showinfo("REPORTS", "REPORT GENERATED")

    def pdfData():
        with open("student_record.json", "r") as read_file:
            student = json.load(read_file)
        pdf_file = "student_record.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=(50*inch, 10*inch))

        elements = []
        styles = getSampleStyleSheet()

        # Table data
        table_data = []
        headers = ["Name", "Birthdate", "Place of Birth", "Sex", "Status", "Region", "Province", "Municipality", "Barangay", "Code", "Number", "Email", "Facebook Name", "Father", "Occupation1", "Mother", "Occupation2", "Siblings", "Annual Income", "Type", "LRN", "Last Attended", "GWA", "College", "Course", "Other"]
        table_data.append(headers)

        for item in student["student_record"]:
            row = [
                item["name"],
                item["birthdate"],
                item["birthplace"],
                item["sex"],
                item["status"],
                item["region"],
                item["province"],
                item["city"],
                item["brgy"],
                item["code"],
                item["number"],
                item["email"],
                item["fb"],
                item["father"],
                item["occupation1"],
                item["mother"],
                item["occupation2"],
                item["siblings"],
                item["income"],
                item["application"],
                item["lrn"],
                item["school"],
                item["gwa"],
                item["college"],
                item["degree"],
                item["yesno"]
            ]
            table_data.append(row)

        # Create a Table
        table = Table(table_data)

        # Add style 
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 6),  
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6), 
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black)  
        ])
        table.setStyle(style)

        elements.append(table)
        doc.build(elements)

        print(f"PDF created successfully at {pdf_file}.")
    
    def deleteData():
      data_delete = DataView.selection()
      print(data_delete)

      item = DataView.item(data_delete)
      values = item["values"]
      DataView.delete(data_delete)
      print(values)
    
      # Fetch the old json file
      with open("student_record.json", "r") as openFile:
        information = json.load(openFile)
      
      newRecord = []
      for everyInfo in information["student_record"]:
        #values[1] refers to the name of the fetched row 
        if values[1] != everyInfo["name"]: 
           newRecord.append(everyInfo)

      # Send back the data to the json file
      newData = {"student_record": newRecord}
      with open("student_record.json", "w") as updateFile:
        json.dump(newData, updateFile, indent=4)
    
    def editData():
        updateButton.config(state="normal")
        editButton.config(state="disabled")
        submitButton.config(state="disabled")

        data_delete = DataView.selection()
        print(data_delete)

        item = DataView.item(data_delete)
        values = item["values"]
        DataView.delete(data_delete)
        print(values)

        clearWidgets()

        nameEntry.insert(0, values[0])
        birthdateEntry.insert(0, values[1])
        birthplaceEntry.insert(0, values[2])
        sexCombobox.set(values[3])
        statusCombobox.set(values[4])
        regionCombo.set(values[5])
        provinceCombo.set(values[6])
        cityCombo.set(values[7])
        brgyCombo.set(values[8])
        codeSpinbox.insert(0, values[9])
        numberEntry.insert(0, values[10])
        emailEntry.insert(0, values[11])
        fbEntry.insert(0, values[12])
        fatherEntry.insert(0, values[13])
        occupationEntry.insert(0, values[14])
        motherEntry.insert(0, values[15])
        occupation2Entry.insert(0, values[16])
        siblingsEntry.insert(0, values[17])
        incomeEntry.insert(0, values[18])
        typeCombobox.set(values[19])
        lrnEntry.insert(0, values[20])
        schoolEntry.insert(0, values[21])
        gwaEntry.insert(0, values[22])
        collegeEntry.insert(0, values[23])
        degreeEntry.insert(0,values[24])
        yesnoVar.set(values[25])
        
    def updateData():
        with open("student_record.json", "w") as openFile2:
            student_record = json.load(openFile2)
        
        for each_info2 in student_record["student_record"]:

            if each_info2["name"] == nameEntry.get():
                each_info2["name"] = nameEntry.get()
                each_info2["birthdate"] = birthdateEntry.get()
                each_info2["birthplace"] = birthplaceEntry.get()
                each_info2["sex"] = sexCombobox.get()
                each_info2["status"] = statusCombobox.get()
                each_info2["region"] = regionCombo.get()
                each_info2["province"] = provinceCombo.get()
                each_info2["city"] = cityCombo.get()
                each_info2["brgy"] = brgyCombo.get()
                each_info2["code"] = codeSpinbox.get()
                each_info2["number"] = numberEntry.get()
                each_info2["email"] = emailEntry.get()
                each_info2["fb"] = fbEntry.get()
                each_info2["father"] = fatherEntry.get()
                each_info2["occupation1"] = occupationEntry.get()
                each_info2["mother"] = motherEntry.get()
                each_info2["occupation2"] = occupation2Entry.get()
                each_info2["siblings"] = siblingsEntry.get()
                each_info2["income"] = incomeEntry.get()
                each_info2["application"] = typeCombobox.get()
                each_info2["lrn"] = lrnEntry.get()
                each_info2["school"] = schoolEntry.get()
                each_info2["gwa"] = gwaEntry.get()
                each_info2["college"] = collegeEntry.get()
                each_info2["degree"] = degreeEntry.get()
                each_info2["yesno"] = yesnoVar.get()
                break
        filename = "student_record.json"
        with open(filename, 'w') as updateFile2:
            json.dump(student_record, updateFile2, indent=4)
            
        updateButton.config(state="disabled")
        editButton.config(state="normal")
        submitButton.config(state="normal")

        updateTreeview()
        clearWidgets()
    updateTreeview()

root.mainloop()