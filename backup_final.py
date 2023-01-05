from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from students import student
from students import __init__


class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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
        img4=Image.open(r"D:\mini\images\bg_img5.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1350,height=650)

        #label
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDACE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="lime green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button 1
        img5=Image.open(r"D:\mini\images\button1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.__init__,cursor="hand2",bg="silver")
        b1.place(x=100,y=100,width=200,height=200)

        b1=Button(bg_img,text="Student Details",command=self.__init__,cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=300,width=200,height=40)


        #student button 2 detect face
        img6=Image.open(r"D:\mini\images\button2.jpeg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",bg="silver")
        b1.place(x=400,y=100,width=200,height=200)

        b1=Button(bg_img,text="Face Detector",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=400,y=300,width=200,height=40)
        
        #student button 3 Attendance
        img7=Image.open(r"D:\mini\images\button3.webp")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",bg="silver")
        b1.place(x=700,y=100,width=200,height=200)

        b1=Button(bg_img,text="Attendance",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=700,y=300,width=200,height=40)

        #student button 4 Help 
        img8=Image.open(r"D:\mini\images\button4.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",bg="silver")
        b1.place(x=1000,y=100,width=200,height=200)

        b1=Button(bg_img,text="Help Desk",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1000,y=300,width=200,height=40)

        #student button 5 Train
        img9=Image.open(r"D:\mini\images\button5.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",bg="silver")
        b1.place(x=100,y=350,width=200,height=200)

        b1=Button(bg_img,text="Tain Data",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=100,y=550,width=200,height=40)

        #button 6 Photos
        img10=Image.open(r"D:\mini\images\button6.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",bg="silver")
        b1.place(x=400,y=350,width=200,height=200)

        b1=Button(bg_img,text="Photos",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=400,y=550,width=200,height=40)

        #student button 7 Developer
        img11=Image.open(r"D:\mini\images\button7.png")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",bg="silver")
        b1.place(x=700,y=350,width=200,height=200)

        b1=Button(bg_img,text="Developer",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=700,y=550,width=200,height=40)

        #student button 8 Exit
        img12=Image.open(r"D:\mini\images\button8.png")
        img12=img12.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",bg="silver")
        b1.place(x=1000,y=350,width=200,height=200)

        b1=Button(bg_img,text="Exit",cursor="hand1",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1000,y=550,width=200,height=40)


    def __init__(self,root):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        obj=__init__(self,root)
        self.mainloop()
    


