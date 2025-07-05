from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # left side icon image
        img=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\left image.jpg")
        img=img.resize((510,150),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=150)



          # middle side icon image
        img1=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\middle image.jpg")
        img1=img1.resize((510,150),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=150)



        # right side icon image
        img2=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\right image.jpg")
        img2=img2.resize((510,150),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=510, height=150)


        # background image
        img3=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\bg image.jpg")
        img3=img3.resize((1530,640),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=640)


        # title label
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)


        #==================time==============
        def time():
            string =strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        


        # student button
        img4=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\student.details.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


        # face detector button
        img5=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\facedetector.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        b2_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # attendance button
        img6=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\attendence.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800, y=100, width=220, height=220)

        b3_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # help button
        img7=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1=Button(bg_img,text="HELP",cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # train button
        img8=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\traindata.jpg")
        img8=img8.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200, y=370, width=220, height=200)

        b5_1=Button(bg_img,text="TRAIN",cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=570, width=220, height=40)

        # photos button
        img9=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\photo.jpg")
        img9=img9.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500, y=370, width=220, height=200)

        b6_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=570, width=220, height=40)


        # developer button
        img10=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\develop.jpg")
        img10=img10.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b8=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b8.place(x=800, y=370, width=220, height=200)
        
        b8_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=800, y=570, width=220, height=40)

        # exit button
        img11=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\exit.jpg")  
        img11=img11.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b7.place(x=1100, y=370, width=220, height=200)

        b7_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=1100, y=570, width=220, height=40)


    def open_img(self):
          os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project.",parent=self.root)
        if self.iExit>0:
           self.root.destroy()
        else:
             return
        
        

            #=======================Functionality Buttons========================
    
    def student_details(self):
                self.new_window = Toplevel(self.root)
                self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

        # Uncomment the following line to call the train_classifier method from Train class
        # self.app.train_classifier()


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()       