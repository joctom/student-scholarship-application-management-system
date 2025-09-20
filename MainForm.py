from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from Location import region
from Location import province_select
from Location import municipality_select
from Location import brgy_select
import os 
import json
# from Location import get_province

root = Tk()
root.geometry("1580x780")
root.title("Tabbed Container Example")
tab_control = ttk.Notebook(root)


style = ttk.Style()
# Configure the style of the notebook tabs
style.configure('TNotebook.Tab', font=('Helvetica', 12))  # Change the font size as desired
# Create tabs
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)

# Add tabs to the notebook
tab_control.add(tab1, text='Tab 1')
tab_control.add(tab2, text='Tab 2')
tab_control.add(tab3, text='Tab 3')
tab_control.pack(expand=1, fill="both")
tab1.configure(bg="#466D1D")

Tab1Frame = Frame(tab1, bd=2, relief=SOLID, width=400, height=700)
Tab1Frame.place(x=10,y=10)

Tab2Frame = Frame(tab1, bd=2, relief=SOLID, width=1000, height=620)
Tab2Frame.place(x=500,y=90)
Tab2Frame.pack_propagate(False)

#FRAME CONTAINING THE SEARCH 
SearchContainer = Frame(tab1, bd=2, relief=SOLID, width=1000, height=70)
SearchContainer.pack_propagate(False)
SearchContainer.place(x=500,y=10)

search_entry = Entry(SearchContainer, width=80, font=("Consolas",13))
search_entry.pack(side=LEFT, padx=15)

search_button = Button(SearchContainer, width=12, height=6, bg="LightSalmon", fg="White",text="SEARCH")
search_button.pack(side=RIGHT, padx=14)

stud_ID = Label(Tab1Frame, text="STUDENT ID", font=("Consolas", 9))
stud_ID.place(x=10,y=10)

stud_ID_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
stud_ID_entry.place(x=40,y=30)
#student Name
stud_Name = Label(Tab1Frame, text="FULL NAME", font=("Consolas", 9))
stud_Name.place(x=10,y=50)

stud_Name_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
stud_Name_entry.place(x=40, y=70)
#Data of Birth
stud_DOB = Label(Tab1Frame, text="BIRTH DATE", font=("Consolas", 9))
stud_DOB.place(x=10,y=90)

stud_DOB_entry = DateEntry(Tab1Frame, width=20, font=("Consolas", 13))
stud_DOB_entry.place(x=40, y=110)
#sex 

stud_SEX = Label(Tab1Frame, text="SEX", font=("Consolas", 9))
stud_SEX.place(x=10,y=130)

SexVar = StringVar()
MaleBtn = Radiobutton(Tab1Frame, text="MALE", font=("Consolas",10), variable=SexVar, value="Male")
MaleBtn.place(x=60,y=140)
FemaleBtn = Radiobutton(Tab1Frame, text="FEMALE", font=("Consolas",10), variable=SexVar, value="Female")
FemaleBtn.place(x=60,y=160)

#email
stud_Email = Label(Tab1Frame, text="EMAIL", font=("Consolas", 9))
stud_Email.place(x=10,y=170)

stud_Email_entry = Entry(Tab1Frame, width=30, font=("Consolas",12))
stud_Email_entry.place(x=40,y=190)
    
#phone number 
def validate_numeric(input):
    # Check if the input consists only of numeric characters
    if input.isdigit():
        return True
    else:
        messagebox.showerror("Error", "Please enter only numeric values")
        return False
    
validate_numeric_format = Tab1Frame.register(validate_numeric)

stud_CPNO = Label(Tab1Frame, text="CONTACT NUMBER", font=("Consolas", 9))
stud_CPNO.place(x=10,y=210)

stud_CPNO_entry = Entry(Tab1Frame, width=30, font=("Consolas",12), validate="key", validatecommand=(validate_numeric_format, '%P'))
stud_CPNO_entry.place(x=40,y=230)

stud_ADDRESS  = Label(Tab1Frame, text="ADDRESS", font=("Consolas", 9))
stud_ADDRESS.place(x=10,y=250)

#COMBOBOXES

region_lbl  = Label(Tab1Frame, text="REGION", font=("Consolas", 12))
region_lbl.place(x=10,y=270)

regionCombo = ttk.Combobox(Tab1Frame, values = region,  font=("Consolas", 12))
regionCombo.place(x=40,y=290)


province = list()
municipality = list()
brgy = list()

def region_selector(event):
    selected_region = regionCombo.get()
    province = province_select(selected_region)
    provinceCombo.configure(values=province)
  
regionCombo.bind("<<ComboboxSelected>>",region_selector)
#PROVINCE 

def province_selector(event):
    selected_region = regionCombo.get()
    selected_province = provinceCombo.get()
    municipality = municipality_select(selected_region, selected_province)
    cityCombo.configure(values=municipality)


province_lbl  = Label(Tab1Frame, text="PROVINCE", font=("Consolas", 12))
province_lbl.place(x=10,y=315)

provinceCombo = ttk.Combobox(Tab1Frame, values=province,  font=("Consolas", 12))
provinceCombo.place(x=40,y=335)
provinceCombo.bind("<<ComboboxSelected>>", province_selector)


def city_selector(event):
    selected_region = regionCombo.get()
    selected_province = provinceCombo.get()
    selected_city = cityCombo.get()

    brgy = brgy_select(selected_region, selected_province, selected_city)
    brgyCombo.configure(values=brgy)

city_lbl  = Label(Tab1Frame, text="MUNICIPALITY", font=("Consolas", 12))
city_lbl.place(x=10,y=360)

cityCombo = ttk.Combobox(Tab1Frame, font=("Consolas", 12))
cityCombo.place(x=40,y=380)
cityCombo.bind("<<ComboboxSelected>>", city_selector)

brgy_lbl  = Label(Tab1Frame, text="BARANGAY", font=("Consolas", 12))
brgy_lbl.place(x=10,y=410)

brgyCombo = ttk.Combobox(Tab1Frame, font=("Consolas", 12))
brgyCombo.place(x=40,y=430)


Submit = Button(Tab1Frame, text="Submit", font=("Consolas",10),width=20,height=5,bg="Black",fg="White", command=lambda:save_data())
Submit.place(x=40,y=500)

Cancel = Button(Tab1Frame, text="Cancel", font=("Consolas",10),width=20,height=5,bg="Lightsalmon",fg="White")
Cancel.place(x=200,y=500)


myColumns = ("ID", "NAME", "BIRTH DATE", "SEX","EMAIL", "PHONE NUM","REGION","PROVINCE","CITY","BRGY")
DataView = ttk.Treeview(Tab2Frame,columns=myColumns,show="headings",)
#OPTINAL CODE IF YOU WISH TO CUSTOMIZE THE SIZE OF THE COLUMNS
DataView.column("ID", stretch=False, width=30)
DataView.column("NAME",stretch=False, width=100)
DataView.column("BIRTH DATE",stretch=False, width=100)
DataView.column("SEX",stretch=False, width=80)
DataView.column("EMAIL",stretch=False, width=150)
DataView.column("PHONE NUM",stretch=False, width=80)
DataView.column("REGION",stretch=False, width=100)
DataView.column("PROVINCE",stretch=False, width=100)
DataView.column("CITY",stretch=False, width=80)
DataView.column("BRGY",stretch=False, width=80)

DataView.heading("ID",text="ID")
DataView.heading("NAME",text="FULLNAME")
DataView.heading("BIRTH DATE",text="BIRTH DATE")
DataView.heading("SEX",text="SEX")
DataView.heading("EMAIL",text="EMAIL")
DataView.heading("PHONE NUM",text="PHONE NUMBER")
DataView.heading("REGION",text="REGION")
DataView.heading("PROVINCE",text="PROVINCE")
DataView.heading("CITY",text="CITY")
DataView.heading("BRGY",text="BRGY")
# DataView.geometry("300x300")
DataView.pack()

#Scroballs are added to a program just in case the contents or data has exceed the frame size
#and the presentation of the data is not accessible due to size dimension limit

# Create a vertical scrollbar - VERTICAL
vsb = ttk.Scrollbar(Tab2Frame, orient=VERTICAL, command=DataView.yview)
vsb.pack(side=RIGHT,fill=Y)

# Create a horizontal scrollbar - HORIZONTAL
hsb = ttk.Scrollbar(Tab2Frame, orient=HORIZONTAL, command=DataView.xview)
hsb.pack(side=BOTTOM,fill=X)

DataView.configure(yscroll=vsb.set, xscroll=hsb.set) 

def save_data():
    #fetch the data from Widgets and set a variable 
    id = stud_ID_entry.get()
    name = stud_Name_entry.get()
    dob= stud_DOB_entry.get()
    sex= SexVar.get()
    email= stud_Email_entry.get()
    cpno= stud_CPNO_entry.get()
    region= regionCombo.get()
    province= provinceCombo.get()
    city= cityCombo.get()
    brgy= brgyCombo.get()

    new_data = {
        "id":id,
        "name":name,
        "birthdate":dob,
        "sex":sex,
        "emai":email,
        "cpno":cpno,
        "region":region,
        "province":province,
        "city":city,
        "brgy":brgy
    }

    filename = "student_record.json"
    if os.path.exists(filename):
        with open(filename,'r') as read_file:
            student_info = json.load(read_file)
    else:
        student_info = {"student_record":[]}
        with open(filename,'w') as create_file:
            json.dump(student_info, create_file,indent=4)
    
    student_info["student_record"].append(new_data)

    with open(filename, 'w') as update_file:
        json.dump(student_info, update_file, indent=4)

    messagebox.showinfo("RECORD", "DATA SAVED SUCCESSFULLY")
    UpdateTree()
    clearWidgets()


def UpdateTree():
    for item in DataView.get_children():
        DataView.delete(item)
    with open("student_record.json") as read_file:
        student_record = json.load(read_file)

    for each_info in student_record["student_record"]:
        DataView.insert("","end", values=(each_info["id"],each_info["name"],each_info["birthdate"],each_info["sex"],each_info["emai"],each_info["cpno"],each_info["region"],each_info["province"],each_info["city"],each_info["brgy"] ))
UpdateTree()

#function for clearing the input widgets 
def clearWidgets():
    stud_ID_entry.delete(0,END)
    stud_Name_entry.delete(0,END)
    stud_DOB_entry.delete(0,END)
    SexVar.set('')
    stud_Email_entry.delete(0,END)
    stud_CPNO_entry.insert(0,0)
    regionCombo.set('')
    provinceCombo.set('')
    cityCombo.set('')
    brgyCombo.set('')

def update_treeview(search_term=""):
    # Clear the Treeview
    for item in DataView.get_children():
        DataView.delete(item)

    # Filter data based on the search term
    with open('student_record.json','r') as read_file:
        data = json.load(read_file)

    filtered_data = []
    for row in data["student_record"]:
        if search_term.lower() in row["name"]:
            filtered_data.append(row)

   
    # Insert the filtered data into the Treeview
    for row in filtered_data:
        DataView.insert("", "end", values=((row["id"],row["name"],row["birthdate"],row["sex"],row["emai"],row["cpno"],row["region"],row["province"],row["city"],row["brgy"] )))

update_treeview("asdf")

root.mainloop()

