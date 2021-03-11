from tkinter import*
import mysql.connector#for connecting mysql with python
import webbrowser#for interacting with web browser
import requests
from bs4 import BeautifulSoup#for webscraping in python
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk#for appying themes in tkinter
win=themed_tk.ThemedTk(theme="Clearlooks")
win.title("Covid-19-App")
win.geometry("800x600")
win.maxsize(800,600)
win.minsize(800,600)
win.iconbitmap("./pictures/vicon.ico")
#adding images globally 
img=Image.open("./pictures/main_bg.jpg")
resized=img.resize((800,600), Image.ANTIALIAS)
new_pic1=ImageTk.PhotoImage(resized)
img2=Image.open("./pictures/corona.jpg")
resized2=img2.resize((800,600), Image.ANTIALIAS)
new_pic2=ImageTk.PhotoImage(resized2)
img3=Image.open("./pictures/pmthanks.png")
resized3=img3.resize((400,400), Image.ANTIALIAS)
new_pic3=ImageTk.PhotoImage(resized3)
img4=Image.open("./pictures/coronawarr.jpg")
resized4=img4.resize((400,400), Image.ANTIALIAS)
new_pic4=ImageTk.PhotoImage(resized4)
#live data web scraping 
page=requests.get(r"https://www.worldometers.info/coronavirus/")
soup=BeautifulSoup(page.content,'html.parser')
page2=requests.get(r"https://www.worldometers.info/coronavirus/country/india/")
soup2=BeautifulSoup(page2.content,'html.parser')
def callback(link):
    webbrowser.open(link)
def frame4():
    frame4=Frame(win,bg="white")
def frame3():
    global new_pic3
    #creating last page
    frame3=Frame(win,bg="black")
    frame3.place(x=0,y=0,width="800",height="600")
    #adding images inside frame3
    pmphotoframe=Label(frame3,image=new_pic3,bg="black")
    pmphotoframe.place(x=450,y=10,width="300",height="300")
    warriorsphotoframe=Label(frame3,image=new_pic4,bg="black")
    warriorsphotoframe.place(x=450,y=320,width="300",height="270")
    #linkframe inside frame3
    linkframe=Frame(frame3,bg="black")
    linkframe.place(x=10,y=10,width="450",height="600")
    #online sources inside linkframe
    lb2=Label(linkframe,text='''Stay updated by reading these online sources: ''',bg="black",
        fg="#9432c9",borderwidth=5,font=("Sans serif",15,"bold"))
    lb2.place(x=0,y=50)
    lb3=Label(linkframe,text='''Click to visit the websites below: ''',fg="#9432c9",bg="black",
        borderwidth=5,font=("Sans serif",15,"bold"))
    lb3.place(x=0,y=100)
    lb4=Label(linkframe,text="-->World Health Organisation(WHO)", fg="#00c2d2", bg="black",
        borderwidth=5,font=("Sans serif",14,"bold"),cursor="hand2")
    lb4.place(x=30,y=200)
    lb4.bind("<Button-1>", lambda e: callback(r"https://www.who.int/health-topics/coronavirus#tab=tab_1"))
    lb5=Label(linkframe,text="-->Indian Council of Medical Research", bg="black",fg="#00c2d2",
        borderwidth=5,font=("Sans serif",14,"bold"),cursor="hand2")
    lb5.place(x=30,y=250)
    lb5.bind("<Button-1>", lambda e: callback(r"https://www.icmr.gov.in/"))
    lb6=Label(linkframe,text="-->Indian Journal of Medical Research",bg="black", fg="#00c2d2",
        borderwidth=5 ,font=("Sans serif",14,"bold"),cursor="hand2")
    lb6.place(x=30,y=300)
    lb6.bind("<Button-1>", lambda e: callback(r"https://www.ijmr.org.in/"))
    lb7=Label(linkframe,text="-->Worldometers",bg="black", fg="#00c2d2",borderwidth=5,
        font=("Sans serif",14,"bold"),cursor="hand2")
    lb7.place(x=30,y=350)
    lb7.bind("<Button-1>", lambda e: callback(r"https://www.worldometers.info/coronavirus/"))
    lb8=Label(linkframe,text="--STAY SAFE, STAY UPDATED--", bg="black",fg="#00ff1d",
        borderwidth=5,font=("Sans serif",20,"bold"))
    lb8.place(x=10,y=400)
    #buttons
    button_pre=Button(frame3,text="PREVIOUS",command=frame2,height="1", width="8",
     borderwidth=5,font=("arial",12,"bold"), fg="Black")
    button_pre.place(x=10,y=500)
    button3=Button(frame3,text="EXIT",command=quit,height="1", width="5",
        borderwidth=5,font=("arial",12,"bold"), fg="RED")
    button3.place(x=350,y=500)
def frame2(): 
    global new_pic2
    #creating second page
    frame2=Frame(win,bg="black")
    frame2.place(x=0,y=0,width="800",height="600")
    #intracting with database
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="newrootpassword")
    cur=mydb.cursor()
    cur.execute('create database if not exists covid_19')
    cur.execute('use covid_19')
    cur.execute('''create table if not exists Active_patients(Fullname varchar(20),Age int,
        gender varchar(20),health_status varchar(40),State varchar(20),PhoneNumber int)''')
    cur.execute('''create table if not exists Staff_Members(Staff_ID int,name varchar(20),
        Age int, gender varchar(20),post varchar(40),salary int)''')
    cur.execute('''create table if not exists deceased_patients(Fullname varchar(20), Age int,
        health_status varchar(40),gender varchar(20),State varchar(20),PhoneNumber int)''')
    cur.execute('''create table if not exists Recovered_patients(Fullname varchar(20), Age int,
        gender varchar(20),State varchar(20), PhoneNumber int,health_status varchar(40))''')
    cur.execute('''create table if not exists unavailstaff(Staff_ID int,name varchar(20),Age int,
        gender varchar(20),post varchar(40),salary int)''')
    mydb.commit()
    def patientdata_enter():
        name=patient_entry.get()
        age=patientage_entry.get()
        gender=patientgender_entry.get()
        state=patientstate_entry.get()
        phoneno=patientnum_entry.get()
        health=patienthealth_entry.get()
        insert='Insert into Active_patients values(%s,%s,%s,%s,%s,%s)'
        info_tuple=(name,age,gender,state,phoneno,health)
        cur.execute(insert,info_tuple)
        mydb.commit()
    def act_count():
        count='select count(*) from Active_Patients'
        displaycount=count
        return displaycount
    def deceased_patients():
        name=patient_entry.get()
        age=patientage_entry.get()
        health=patienthealth_entry.get()
        gender=patientgender_entry.get()
        state=patientstate_entry.get()
        phoneno=patientnum_entry.get()
        insert='Insert into deceased_patients values(%s,%s,%s,%s,%s,%s)'
        info_tuple=(name,age,health,gender,state,phoneno)
        cur.execute(insert,info_tuple)
        mydb.commit()
    def patientdata_delete():
        name=patient_entry.get()
        age=patientage_entry.get()
        gender=patientgender_entry.get()
        state=patientstate_entry.get()
        phoneno=patientnum_entry.get()
        health=patienthealth_entry.get()
        delete='Delete from Active_patients where PhoneNumber=(%s)'
        delete_tuple=(phoneno,)
        cur.execute(delete,delete_tuple)
        mydb.commit()

    def patient_recovered():
        name=patient_entry.get()
        age=patientage_entry.get()
        gender=patientgender_entry.get()
        state=patientstate_entry.get()
        phoneno=patientnum_entry.get()
        health=patienthealth_entry.get()
        insert='Insert into Recovered_patients values(%s,%s,%s,%s,%s,%s)'# inserting data into recovered patients table
        info_tuple=(name,age,gender,state,phoneno,health)
        cur.execute(insert,info_tuple)
        delete='Delete from Active_patients where PhoneNumber=(%s)'
        delete_tuple=(phoneno,)
        cur.execute(delete,delete_tuple)
        mydb.commit()
    def patientdata_win():
        patientwin=themed_tk.ThemedTk(theme="Clearlooks")
        patientwin.title("Patient database")
        patientwin.geometry("800x600")
        patientwin.minsize(800,600)
        patientwin.maxsize(800,600)
        def update1(rows):
            for i in rows:
                tree.insert(parent="",index='end',values=i)

        #Active patients section
        activepatientlabel=Label(patientwin,text="ACTIVE CORONA PATIENTS",fg="#00c2d2",
                                borderwidth=5,bg="black",font=('comicsansms',15,'bold'))
        activepatientlabel.place(x=300,y=0)
        add_frame=Frame(patientwin,bg="white")
        add_frame.place(x=0,y=30,width="800",height="190")
        #scroll bar for add_frame
        add_scroll=Scrollbar(add_frame)
        add_scroll.pack(side=RIGHT,fill=Y)
        #treeview
        tree=ttk.Treeview(add_frame, yscrollcommand=add_scroll.set,columns=(1,2,3,4,5,6),
                         show="headings",height="2")
        tree.place(x=0,y=0,width="780",height="160")
        add_scroll.config(command=tree.yview)

        tree.column("1", width = 90, minwidth=50, anchor ='c') 
        tree.column("2", width = 90, minwidth=50,anchor ='c') 
        tree.column("3", width = 90,minwidth=50, anchor ='c')
        tree.column("4", width = 90,minwidth=50, anchor ='c') 
        tree.column("5", width = 90,minwidth=50, anchor ='c') 
        tree.column("6", width = 90, minwidth=50,anchor ='c')
        tree.heading(1,text="Patient name", anchor="c")
        tree.heading(2,text="Age",anchor="c")
        tree.heading(3,text="Gender",anchor="c")
        tree.heading(4,text="State",anchor="c")
        tree.heading(5,text="Phone number",anchor="c")
        tree.heading(6,text="Health status",anchor="c")
        query="Select Fullname,Age, Gender, state, PhoneNumber, Health_status from Active_Patients"
        cur.execute(query)
        rows=cur.fetchall()
        update1(rows)
        def update2(rows2):
            for i in rows2:
                tree2.insert(parent="",index='end',values=i)
        #Recovered Patients section
        recoveredpatientlabel=Label(patientwin,text="RECOVERED CORONA PATIENTS",borderwidth=5,
                                    fg="#00c2d2",bg="black",font=('comicsansms',15,'bold'))
        recoveredpatientlabel.place(x=300,y=210)
        recovered_frame=Frame(patientwin,bg="white")
        recovered_frame.place(x=0,y=240,width="800",height="160")
        #scroll bar for recovered_frame
        recovered_scroll=Scrollbar(recovered_frame)
        recovered_scroll.pack(side=RIGHT,fill=Y)
        #treeview 
        tree2=ttk.Treeview(recovered_frame,yscrollcommand=add_scroll.set,columns=(1,2,3,4,5,6),
                           show="headings",height="2")
        tree2.place(x=0,y=0,width="780",height="160")
        recovered_scroll.config(command=tree2.yview)
        tree2.column("1", width = 90, minwidth=50, anchor ='c') 
        tree2.column("2", width = 90, minwidth=50,anchor ='c') 
        tree2.column("3", width = 90,minwidth=50, anchor ='c')
        tree2.column("4", width = 90,minwidth=50, anchor ='c') 
        tree2.column("5", width = 90,minwidth=50, anchor ='c') 
        tree2.column("6", width = 90, minwidth=50,anchor ='c')
        tree2.heading(1,text="Patient name", anchor="c")
        tree2.heading(2,text="Age",anchor="c")
        tree2.heading(3,text="Gender",anchor="c")
        tree2.heading(4,text="State",anchor="c")
        tree2.heading(5,text="Phone number",anchor="c")
        tree2.heading(6,text="Health status",anchor="c")
        query2="Select Fullname,Age, Gender, state, PhoneNumber, Health_status from Recovered_Patients"
        cur.execute(query2)
        rows2=cur.fetchall()
        update2(rows2)
        def update3(rows3):
            for i in rows3:
                tree3.insert(parent="",index='end',values=i)
        #Deceased patients section
        deceasedpatientlabel=Label(patientwin,text="DECEASED CORONA PATIENTS",borderwidth=5,
                                   fg="#00c2d2",bg="black",font=('comicsansms',15,'bold'))
        deceasedpatientlabel.place(x=300,y=420)
        deceased_frame=Frame(patientwin,bg="white")
        deceased_frame.place(x=0,y=470,width="800",height="200")
        #scroll bar for deceased_frame
        deceased_scroll=Scrollbar(deceased_frame)
        deceased_scroll.pack(side=RIGHT,fill=Y)
        #treeview
        tree3=ttk.Treeview(deceased_frame,yscrollcommand=deceased_scroll.set,columns=(1,2,3,4,5,6),
                           show="headings",height="2")
        tree3.place(x=0,y=0,width="780",height="190")
        deceased_scroll.config(command=tree3.yview)

        tree3.column("1", width = 90, minwidth=50, anchor ='c') 
        tree3.column("2", width = 90, minwidth=50,anchor ='c') 
        tree3.column("3", width = 90,minwidth=50, anchor ='c')
        tree3.column("4", width = 90,minwidth=50, anchor ='c') 
        tree3.column("5", width = 90,minwidth=50, anchor ='c') 
        tree3.column("6", width = 90, minwidth=50,anchor ='c')
        tree3.heading(1,text="Patient name", anchor="c")
        tree3.heading(2,text="Age",anchor="c")
        tree3.heading(3,text="Gender",anchor="c")
        tree3.heading(4,text="State",anchor="c")
        tree3.heading(5,text="Phone number",anchor="c")
        tree3.heading(6,text="Health status",anchor="c")
        query3="Select Fullname,Age, Gender, state, PhoneNumber, Health_status from Deceased_Patients"
        cur.execute(query3)
        rows3=cur.fetchall()
        update3(rows3)
        patientwin.mainloop()
    #events on patient's frame buttons
    def submittedbox():
        messagebox.showinfo("","Patient data submitted, click on show data to check the table.")
    def bindfn1():# for binding 2 commands
        patientdata_enter()
        submittedbox()
    def removedbox():
        messagebox.showinfo("","Patient Removed from active patient table, Click on show data to check the table.")
    def bindfn2():# for binding 2 commands
        patientdata_delete()
        removedbox()
    def recoveredbox():
        messagebox.showinfo("","Patient added to recovered table, Click on show data to check the table.")
    def bindfn3():
        patient_recovered()
        recoveredbox()
    def deceasedbox():
        messagebox.showinfo("","Patient added to deceased table, Click on show data to check the table.")
    def bindfn4():
        deceased_patients()
        deceasedbox()
    #creating patient_frame
    patient_frame=Frame(frame2,bg="black")
    patient_frame.place(x=0,y=0,width="800",height="300")
    bglabel=Label(patient_frame,image=new_pic2)#bglabel==2nd page size(for bgimage)
    bglabel.place(x=0,y=0,width="800",height="300")
    #creating labels inside patients's frame
    patientheading_label=Label(patient_frame,text="PATIENTS", fg="#9432c9", 
                               bg="white",borderwidth=5,font=(" MS Sans Serif",20,"bold"))
    patientheading_label.grid(row=1,column=2,pady=5,sticky=W,padx=10)
    patientname_label=Label( patient_frame,text="Fullname:",fg="black",
                            font=(" MS Sans Serif",12,"bold"),borderwidth=5)
    patientname_label.grid(row=2,column=0,pady=5,sticky=W,padx=10)
    patient_entry=Entry( patient_frame,font=(" MS Sans Serif",12,"bold"),
                       bg="White",borderwidth=5,fg="#8b8be9",relief=RAISED)
    patient_entry.grid(row=2, column=1,pady=5,padx=10)
    patienthealth_label=Label(patient_frame,text="Health Status",fg="black", 
                       borderwidth=5,font=(" MS Sans Serif",12,"bold"))
    patienthealth_label.grid(row=2,column=2,pady=5,padx=10)
    patienthealth_entry=Entry(patient_frame,font=(" MS Sans Serif",12,"bold"),
                              borderwidth=5,bg="white",fg="#8b8be9",relief=RAISED)
    patienthealth_entry.grid(row=2,column=3,pady=5,padx=10)
    patientage_label=Label( patient_frame,text="Age: ",fg="black",borderwidth=5,
                           font=(" MS Sans Serif",12,"bold"))
    patientage_label.grid(row=3,column=0,pady=5,sticky=W,padx=10)
    patientage_entry=Entry( patient_frame,font=(" MS Sans Serif",12,"bold"),
                           borderwidth=5,bg="white",fg="#8b8be9",relief=RAISED)
    patientage_entry.grid(row=3, column=1,pady=5,padx=10)
    patientgender_label=Label( patient_frame,text="Gender: ",borderwidth=5,
                              fg="black",font=(" MS Sans Serif",12,"bold"))
    patientgender_label.grid(row=3,column=2,pady=5,sticky=W,padx=10)
    patientgender_entry=Entry( patient_frame,font=(" MS Sans Serif",12,"bold"),borderwidth=5,
                             bg="white",fg="#8b8be9",relief=RAISED)
    patientgender_entry.grid(row=3, column=3,pady=5,padx=10)
    patientstate_label=Label( patient_frame,text="State: ",borderwidth=5,fg="black",
                            font=(" MS Sans Serif",12,"bold"))
    patientstate_label.grid(row=4,column=0,pady=5,sticky=W,padx=10)
    patientstate_entry=Entry( patient_frame,font=(" MS Sans Serif",12,"bold"),borderwidth=5,
                            bg="white",fg="#8b8be9",relief=RAISED)
    patientstate_entry.grid(row=4, column=1,pady=5,padx=10)
    patientnum_label=Label( patient_frame,text="Phone number: ",fg="black",borderwidth=5,
                          font=(" MS Sans Serif",12,"bold"))
    patientnum_label.grid(row=4,column=2,pady=5,sticky=W,padx=10)
    patientnum_entry=Entry( patient_frame,font=(" MS Sans Serif",12,"bold"),borderwidth=5,
                          bg="white",fg="#8b8be9",relief=RAISED)
    patientnum_entry.grid(row=4, column=3,pady=5,padx=10)
    #patient_frame buttons
    show_patientsdata_button=Button(patient_frame,text="Show data",borderwidth=5,height="1", 
                             width="8", font=("comicsansms",12,"bold"), fg="#9432c9",command=patientdata_win)
    show_patientsdata_button.grid(row=5, column=0,pady=5,padx=10)
    submit_button=Button(patient_frame,text="ADD",height="1",borderwidth=5, width="6",
                         font=("comicsansms",12,"bold"), fg="#9432c9",command=bindfn1)
    submit_button.grid(row=5, column=1,pady=5,padx=10)
    deceased_button=Button(patient_frame,text="DECEASED",borderwidth=5,height="1",
                          width="10", font=("comicsansms",12,"bold"), fg="#9432c9",command=bindfn4)
    deceased_button.grid(row=5, column=2,pady=5,padx=10)
    removepatient_button=Button(patient_frame,text="REMOVE",borderwidth=5,height="1", width="7",
                               font=("comicsansms",12,"bold"), fg="#9432c9",command=bindfn2)
    removepatient_button.grid(row=6, column=0,pady=5,padx=10)
    recovered_button=Button(patient_frame,text="RECOVERED",borderwidth=5,height="1",width="12",
                            font=("comicsansms",12,"bold"),fg="#9432c9",command=bindfn3)
    recovered_button.grid(row=6, column=1,pady=5,padx=10)

    def staffdata_enter():
        Staff_ID=staffID_entry.get()
        name=staffname_entry.get()
        age=staffage_entry.get()
        gender=staffgender_entry.get()
        post=staffpost_entry.get()
        salary=staffsalary_entry.get()
        insert='Insert into staff_members values(%s,%s,%s,%s,%s,%s)'
        info_tuple=(Staff_ID,name,age,gender,post,salary)
        cur.execute(insert,info_tuple)
        mydb.commit()
    def staffdata_delete():
        Staff_ID=staffID_entry.get()
        name=staffname_entry.get()
        age=staffage_entry.get()
        gender=staffgender_entry.get()
        post=staffpost_entry.get()
        salary=staffsalary_entry.get()
        delete='Delete from staff_members where Staff_ID=(%s)'
        delete_tuple=(Staff_ID,)
        cur.execute(delete,delete_tuple)
        mydb.commit()
    def unavailstaff():
        Staff_ID=staffID_entry.get()
        name=staffname_entry.get()
        age=staffage_entry.get()
        gender=staffgender_entry.get()
        post=staffpost_entry.get()
        salary=staffsalary_entry.get()
        insert='Insert into unavailstaff values(%s,%s,%s,%s,%s,%s)'
        info_tuple=(Staff_ID,name,age,gender,post,salary)
        cur.execute(insert,info_tuple)
        mydb.commit()
    def staffdata_win():
        staffwin=themed_tk.ThemedTk(theme="Clearlooks")
        staffwin.title("Staff database")
        staffwin.geometry("800x600")
        staffwin.minsize(800,600)
        staffwin.maxsize(800,600)
        def update1(rows):
            for i in rows:
                tree.insert(parent="",index='end',values=i)
        
        #Staff Section
        totalstafflabel=Label(staffwin,text="CORONA STAFF",borderwidth=5,fg="#00c2d2",bg="black",font=('comicsansms',15,'bold'))
        totalstafflabel.place(x=300,y=0)
        addstaff_frame=Frame(staffwin,bg="white")
        addstaff_frame.place(x=0,y=30,width="800",height="300")
        #scroll bar for addstaff_frame
        addstaff_scroll=Scrollbar(addstaff_frame)
        addstaff_scroll.pack(side=RIGHT,fill=Y)
        #treeview
        tree=ttk.Treeview(addstaff_frame,yscrollcommand=addstaff_scroll.set,columns=(1,2,3,4,5,6),show="headings",height="2")
        tree.place(x=0,y=0,width="780",height="300")
        addstaff_scroll.config(command=tree.yview)

        tree.column("1", width = 90, minwidth=50, anchor ='c') 
        tree.column("2", width = 90, minwidth=50,anchor ='c') 
        tree.column("3", width = 90,minwidth=50, anchor ='c')
        tree.column("4", width = 90,minwidth=50, anchor ='c') 
        tree.column("5", width = 90,minwidth=50, anchor ='c') 
        tree.column("6", width = 90, minwidth=50,anchor ='c')
        tree.heading(1,text="Staff-ID", anchor="c")
        tree.heading(2,text="Full name", anchor="c")
        tree.heading(3,text="Age",anchor="c")
        tree.heading(4,text="Gender",anchor="c")
        tree.heading(5,text="Post",anchor="c")
        tree.heading(6,text="Salary",anchor="c")
        query="Select Staff_ID, name, Age, Gender, Post, Salary from Staff_Members"
        cur.execute(query)
        rows=cur.fetchall()
        update1(rows)
        def update2(rows2):
            for i in rows2:
                tree2.insert(parent="",index='end',values=i)
        #Unavailable Staff section
        unavailstafflabel=Label(staffwin,text="STAFF UNAVAILABLE",borderwidth=5,fg="#00c2d2",
                               bg="black",font=('comicsansms',15,'bold'))
        unavailstafflabel.place(x=300,y=320)
        unavail_frame=Frame(staffwin,bg="white")
        unavail_frame.place(x=0,y=360,width="800",height="300")
        #scroll bar for unavail_frame
        unavail_scroll=Scrollbar(unavail_frame)
        unavail_scroll.pack(side=RIGHT,fill=Y)
        #treeview
        tree2=ttk.Treeview(unavail_frame,yscrollcommand=unavail_scroll.set,columns=(1,2,3,4,5,6),show="headings",height="2")
        tree2.place(x=0,y=0,width="780",height="300")
        unavail_scroll.config(command=tree2.yview)

        tree2.column("1", width = 90, minwidth=50, anchor ='c') 
        tree2.column("2", width = 90, minwidth=50,anchor ='c') 
        tree2.column("3", width = 90,minwidth=50, anchor ='c')
        tree2.column("4", width = 90,minwidth=50, anchor ='c') 
        tree2.column("5", width = 90,minwidth=50, anchor ='c') 
        tree2.column("6", width = 90, minwidth=50,anchor ='c')
        tree2.heading(1,text="Staff-ID", anchor="c")
        tree2.heading(2,text="Full name", anchor="c")
        tree2.heading(3,text="Age",anchor="c")
        tree2.heading(4,text="Gender",anchor="c")
        tree2.heading(5,text="Post",anchor="c")
        tree2.heading(6,text="Salary",anchor="c")
        query2="Select Staff_ID, name, Age, Gender, Post, Salary from unavailstaff"
        cur.execute(query2)
        rows2=cur.fetchall()
        update2(rows2)
        staffwin.mainloop()
    #events on staff's frame buttons
    def submitstaffbox():
        messagebox.showinfo("","Staff added,check the show data button to view staff data.")
    def removestaffbox():
        messagebox.showinfo("","Staff Removed,check the show data button to view staff data.")
    def unavailstaffbox():
        messagebox.showinfo("","Staff added to Unavailable list,check the show data button to view staff data.")
    def bindfn4():
        staffdata_enter()
        submitstaffbox()
    def bindfn5():
        staffdata_delete()
        removestaffbox()
    def bindfn6():
        staffdata_delete()
        unavailstaff()
        unavailstaffbox()
    #creating staff_frame
    staff_frame=Frame(frame2,bg="black")
    staff_frame.place(x=0,y=300,width="800",height="300")
    bglabel=Label(staff_frame,image=new_pic2)#bglabel==2nd page size(for bgimage)
    bglabel.place(x=0,y=0,width="800",height="300")
    #creating labels inside staff_frame
    staffheading_label=Label(staff_frame,text="STAFF", fg="#9432c9", borderwidth=5,bg="white",font=("comicsansms",20,"bold"))
    staffheading_label.grid(row=1,column=2,pady=5,padx=10,sticky=W)
    staffID_label=Label(staff_frame,text="Staff-ID: ",fg="black",borderwidth=5,font=("comicsansms",12,"bold"))
    staffID_label.grid(row=2,column=0,pady=5,sticky=W,padx=10)
    staffID_entry=Entry(staff_frame,font=("comicsansms",12,"bold"),borderwidth=5,bg="White",fg="#8b8be9",relief=RAISED)
    staffID_entry.grid(row=2, column=1,pady=5,padx=10)
    staffname_label=Label(staff_frame,text="Name: ",fg="black",borderwidth=5,font=("comicsansms",12,"bold"))
    staffname_label.grid(row=2,column=2,pady=5,sticky=W,padx=10)
    staffname_entry=Entry(staff_frame,font=("comicsansms",12,"bold"),borderwidth=5,bg="white",fg="#8b8be9",relief=RAISED)
    staffname_entry.grid(row=2, column=3,pady=5,padx=10)
    staffage_label=Label(staff_frame,text="Age: ",fg="black",borderwidth=5,font=("comicsansms",12,"bold"))
    staffage_label.grid(row=3,column=0,pady=5,sticky=W,padx=10)
    staffage_entry=Entry(staff_frame,font=("comicsansms",12,"bold"),borderwidth=5,bg="white",fg="#8b8be9",relief=RAISED)
    staffage_entry.grid(row=3, column=1,pady=5,padx=10)
    staffgender_label=Label(staff_frame,text="Gender: ",fg="black",borderwidth=5,font=("comicsansms",12,"bold"))
    staffgender_label.grid(row=3,column=2,pady=5,sticky=W,padx=10)
    staffgender_entry=Entry(staff_frame,font=("comicsansms",12,"bold"),borderwidth=5,bg="white",fg="#8b8be9",relief=RAISED)
    staffgender_entry.grid(row=3, column=3,pady=5,padx=10)
    staffpost_label=Label(staff_frame,text="Post: ",fg="black",borderwidth=5,font=("comicsansms",12,"bold"))
    staffpost_label.grid(row=4,column=0,pady=5,sticky=W,padx=10)
    staffpost_entry=Entry(staff_frame,font=("comicsansms",12,"bold"),borderwidth=5,bg="White",fg="#8b8be9",relief=RAISED)
    staffpost_entry.grid(row=4, column=1,pady=5,padx=10)
    staffsalary_label=Label(staff_frame,text="Salary: ",fg="black",borderwidth=5,font=("comicsansms",12,"bold"))
    staffsalary_label.grid(row=4,column=2,pady=5,sticky=W,padx=10)
    staffsalary_entry=Entry(staff_frame,font=("comicsansms",12,"bold"),borderwidth=5,bg="White",fg="#8b8be9",relief=RAISED)
    staffsalary_entry.grid(row=4, column=3,pady=5,padx=10)
    submitstaff_button=Button(staff_frame,text="ADD", height="1",width="7",borderwidth=5,
                              font=("arial",12,"bold"),fg="#9432c9",command=bindfn4)
    submitstaff_button.grid(row=5, column=0,pady=5,padx=10)
    removestaff_button=Button(staff_frame,text="REMOVE",height="1", width="7",borderwidth=5,
                              font=("arial",12,"bold"), fg="#9432c9",command=bindfn5)
    removestaff_button.grid(row=5, column=1,pady=5,padx=10)
    showstaffdata_button=Button(staff_frame,text="Show data",height="1", width="8",borderwidth=5,
                                font=("arial",12,"bold"), fg="#9432c9",command=staffdata_win)
    showstaffdata_button.grid(row=5, column=2,pady=5,padx=10)
    unavailstaff_button=Button(staff_frame,text="UNAVAILABLE",height="1",width="15",borderwidth=5,
                               font=("arial",12,"bold"),fg="#9432c9",command=bindfn6)
    unavailstaff_button.grid(row=6,column=1,pady=5,padx=10)
    #2nd page buttons
    next_button=Button(frame2,text="NEXT",borderwidth=5,command=frame3,height="1", width="5",
                    font=("arial",12,"bold"),fg="Black")
    next_button.place(x=700,y=450)
    previous_button=Button(frame2,text="PREVIOUS",borderwidth=5,command=frame1,height="1",
                           width="8", font=("arial",12,"bold"), fg="Black")
    previous_button.place(x=700,y=300)
def inframe():
    #creating instructions frame
    frame=Frame(win,bg="black")
    frame.place(x=0,y=0,width="800",height="600")
    #labels 
    l1=Label(frame,text="WHY THIS APP!??",fg="#00c2d2",bg="black",font=('Times',30,'bold'))
    l1.place(x=240,y=0)
    l2=Label(frame,text='''
This app was created during lockdown when the world 
was shut due to the globally spreading SARS COVID-19 virus.
This is a small tribute for those coronavirus warriors
who followed their duties risking their own lives.
It's goal is to show the live details of the world and of
India related to Coronavirus and to manage local pandemic related data.''',
fg="#9432c9",bg="black",font=("Times New Roman ",16,"bold"))
    l2.place(x=5,y=60)
    l3=Label(frame,text="----INSTRUCTIONS----",fg="#00c2d2",bg="black",font=('Times',30,'bold'))
    l3.place(x=200,y=250)
    l4=Label(frame,text=
'''* Add patients into active patient list by filling all the given entries.
* To remove the patients from active patient list, fill their phone numbers.
* To add the patients into Recovered patients list,fill all the enteries.
* To add the deceased patients into Deceased patients list, fill all the enteries.
* Similarly in the staff section, to add staff into staff list, fill all the enteries.
* To remove staff from staff list, fill all the enteries.
* To add staff into Unavailable list, fill all the enteries.
* Click on the show data to review the lists.
* Stay updated by reading online resources given on last page''',fg="#9432c9",bg="black",font=("Times New Roman ",16,"bold"))
    l4.place(x=5,y=310)
    #buttons
    button1=Button(frame,text="NEXT",command=frame2,height="1", width="5",borderwidth=5, font=("arial",12,"bold"), fg="Black")
    button1.place(x=700,y=530)
    button2=Button(frame,text="MAIN WINDOW",command=frame1,height="1",width="13",borderwidth=5,font=("arial",12,"bold"),fg="Black")
    button2.place(x=20,y=530)
def frame1():
    global new_pic1
    global page
    global page2
    #creating first page
    frame1=Frame(win,bg="#81d0f4")
    frame1.place(x=0,y=0,width="800",height="600")
    #adding bg image
    lb1=Label(frame1,image=new_pic1)
    lb1.place(x=0,y=0,width="800",height="600")
    #top heading text
    lb2=Label(lb1,text="LIVE CORONA DETAILS:",fg="#22fb15",bg="black",font=("comicsansms",20,"bold"))
    lb2.place(x=0,y=0)
    #web scraping live cases: World
    wdata=[]
    world_totalcases=soup.find_all('div',class_="maincounter-number")
    for i in world_totalcases:
        a=i.text.replace("\n", "")
        wdata.append(a)
    print(wdata)
    #web scraping live cases: India
    idata=[]
    ind_totalcases=soup2.find_all('div',class_="maincounter-number")
    for i in ind_totalcases:
        b=i.text.replace("\n","")
        idata.append(b)
    print(idata)
    #WORLD Frame
    wframe=Frame(lb1,bg="#c0dfbe")
    wframe.place(x=10,y=50,width=300,height=150)
    lb3=Label(wframe,text="WORLD:", fg="#a2be14",bg="black",font=("comicsansms",15,"bold"))
    lb3.grid(row=0,column=0,padx=2,pady=2)
    lb4=Label(wframe,text="Total cases:", fg="#00c2d2",bg="black",font=("comicsansms",15,"bold"))
    lb4.grid(row=1,column=0,padx=2,pady=2)
    lb5=Label(wframe,text=wdata[0],fg="#8b8be9",bg="black",font=("comicsansms",15,"bold"))
    lb5.grid(row=1,column=1,padx=2,pady=2)
    lb6=Label(wframe,text="Deaths:", fg="#00c2d2",bg="black",font=("comicsansms",15,"bold"))
    lb6.grid(row=3,column=0,padx=2,pady=2)
    lb7=Label(wframe,text=wdata[1], fg="#8b8be9",bg="black",font=("comicsansms",15,"bold"))
    lb7.grid(row=3,column=1,padx=2,pady=2)
    lb8=Label(wframe,text="Recovered:", fg="#00c2d2",bg="black",font=("comicsansms",15,"bold"))
    lb8.grid(row=2,column=0,padx=2,pady=2)
    lb9=Label(wframe,text=wdata[2], fg="#8b8be9",bg="black",font=("comicsansms",15,"bold"))
    lb9.grid(row=2,column=1,padx=2,pady=2)
    #INDIA Frame
    iframe=Frame(lb1,bg="#c0dfbe")
    iframe.place(x=400,y=50,width=300,height=150)
    lb10=Label(iframe,text="INDIA:", fg="#a2be14",bg="black",font=("comicsansms",15,"bold"))
    lb10.grid(row=0,column=0,padx=2,pady=2)
    lb11=Label(iframe,text="Total cases:",fg="#00c2d2",bg="black",font=("comicsansms",15,"bold"))
    lb11.grid(row=1,column=0,padx=2,pady=2)
    lb12=Label(iframe,text=idata[0],fg="#8b8be9",bg="black",font=("comicsansms",15,"bold"))
    lb12.grid(row=1,column=1,padx=2,pady=2)
    lb13=Label(iframe,text="Deaths:",fg="#00c2d2",bg="black",font=("comicsansms",15,"bold"))
    lb13.grid(row=2,column=0,padx=2,pady=2)
    lb14=Label(iframe,text=idata[1],fg="#8b8be9",bg="black",font=("comicsansms",15,"bold"))
    lb14.grid(row=2,column=1,padx=2,pady=2)
    lb15=Label(iframe,text="Recovered:",fg="#00c2d2",bg="black",font=("comicsansms",15,"bold"))
    lb15.grid(row=3,column=0,padx=2,pady=2)
    lb16=Label(iframe,text=idata[2],fg="#8b8be9",bg="black",font=("comicsansms",15,"bold"))
    lb16.grid(row=3,column=1,padx=2,pady=2)
    #quit command to quit the app
    def quit_app():
        quit()
    #buttons
    button_inst=Button(frame1,text="Instructions",command=inframe,height="1",width="12", borderwidth=5,
                       font=("arial",12,"bold"),fg="Black")
    button_inst.place(x=100,y=450)
    button_next=Button(frame1,text="NEXT",command=frame2,height="1", width="5", borderwidth=5, 
                      font=("arial",12,"bold"), fg="Black")
    button_next.place(x=700,y=450)
    button_exit=Button(frame1,text="EXIT",command=quit_app,height="1", width="5", borderwidth=5,
                       font=("arial",12,"bold"), fg="RED")
    button_exit.place(x=350,y=500)
    #creator's name
    myname=Label(text="Created By: Riya Bisht(XII-A)", fg="#00ff1d",bg="black",font=("comicsansms",20,"bold"))
    myname.place(x=200,y=550)
frame1()
win.mainloop()

