from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #================variabless=================
        self.var_deep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
   

        #image1
        img=Image.open(r"D:\mini\images\img1.png")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)

        #image2
        img2=Image.open(r"D:\mini\images\img2.png")
        img2=img2.resize((300,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=400,y=0,width=500,height=130)
        
         #image3
        img3=Image.open(r"D:\mini\images\img3.png")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=850,y=0,width=500,height=130) 

        #bg image
        img4=Image.open(r"D:\mini\images\bg.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1350,height=650)

        #label
        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",25,"bold"),bg="lime green",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1300,height=540)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=650,height=530)

        #left image
        img_left=Image.open(r"D:\mini\images\img3.png")
        img_left=img_left.resize((550,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=640,height=130) 

        #left(Current course) frame
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=3,y=135,width=640,height=150)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"italic"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_deep,font=("times new roman",10,"bold"),state="read only",width=20)
        dep_combo["value"]=("Select Department","COMPUTER SCIENCE","MECHANICAL","IS","AIML")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        dep_label=Label(current_course_frame,text="Course",font=("times new roman",13,"italic"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Course","FE","SE","TE","BE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"italic"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="read only",width=20)
        year_combo["values"]=("Select session","2018","2019","2020","2021")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"italic"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        
        #class student Information -frame
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=3,y=290,width=640,height=300)
        
        #studentID
        studentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13))
        studentId_entry.grid(row=0,column=1,padx=1,sticky=W)

        #student Name
        studentId_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=0,column=2,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13))
        studentId_entry.grid(row=0,column=3,padx=2,sticky=W)

        #class Division
        studentId_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=1,column=0,padx=1,pady=1,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13))
        studentId_entry.grid(row=1,column=1,padx=1,pady=1,sticky=W)

        #Roll no
        studentId_label=Label(class_student_frame,text="Roll no:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=1,column=2,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13))
        studentId_entry.grid(row=1,column=3,padx=2,pady=1,sticky=W)
        
        #Phone No
        studentId_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=2,column=0,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13))
        studentId_entry.grid(row=2,column=1,padx=2,pady=1,sticky=W)

        #DOB
        studentId_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=2,column=2,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,self.var_dob,width=20,font=("times new roman",13))
        studentId_entry.grid(row=2,column=3,padx=2,pady=1,sticky=W)

        #Email
        studentId_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"italic"),bg="white")
        studentId_label.grid(row=3,column=0,padx=10,pady=1,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,self.var_email,width=20,font=("times new roman",13))
        studentId_entry.grid(row=3,column=1,padx=2,pady=1,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"italic"),bg="white")
        gender_label.grid(row=3,column=2,padx=10,pady=1,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="read only",width=23)
        gender_combo["values"]=("Select Gender","M","F","NOT SPECIFIED")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=3,padx=3,pady=1,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

        #bbuttons -frame 0
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=3,y=130,width=630,height=30)

        #save button
        save_btn=Button(btn_frame,text="Save",font=("times new roman",10,"bold"),bg="blue",fg="white",width=21)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",10,"bold"),bg="blue",fg="white",width=21)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",10,"bold"),bg="blue",fg="white",width=21)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",font=("times new roman",10,"bold"),bg="blue",fg="white",width=21)
        reset_btn.grid(row=0,column=3)

        #button -frame-1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=3,y=160,width=630,height=30)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",font=("times new roman",10,"bold"),bg="red",fg="white",width=43)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman",10,"bold"),bg="red",fg="white",width=44)
        update_photo_btn.grid(row=0,column=1)




        #right label -frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"))
        right_frame.place(x=670,y=10,width=650,height=530)


        img_right=Image.open(r"D:\mini\images\img3.png")
        img_right=img_right.resize((550,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=619,height=130) 


        #==========SEARCH SYSTEM============
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=3,y=135,width=620,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"italic"),bg="violet")
        search_label.grid(row=0,column=0,padx=1,pady=0,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",11,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Roll_No","Name","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=0,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13))
        search_entry.grid(row=0,column=2,padx=2,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",10,"bold"),bg="red",fg="white",width=14)
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(search_frame,text="Show All",font=("times new roman",10,"bold"),bg="red",fg="white",width=14)
        showAll_btn.grid(row=0,column=4,padx=3)

        #===========Table -frame==============
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=210,width=620,height=280)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("deep","course","year","sem","id","name","div","gender","dob","phone","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("deep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings" #shows tables

        self.student_table.column("deep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)

    def add_data(self):
        if self.var_deep.get()


if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()