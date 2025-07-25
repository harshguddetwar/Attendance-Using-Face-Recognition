from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from itertools import count
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=======================variables==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        img=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\left image.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)



          # middle side icon image
        img1=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\middle image.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)


        # background image
        img3=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\bg image.jpg")
        img3=img3.resize((1530,640),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=640)

        title_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="DARKGREEN")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg="white", text="Student Attendance Details", font=("times new roman", 12, "bold"), fg="red")
        left_frame.place(x=10, y=10, width=750, height=550)

        img_left=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\right image.jpg")
        img_left=img_left.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=110)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=125,width=720,height=370)

        #========label and entry
        attendanceId_label = Label(left_inside_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        #name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        name_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman", 13, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        roll_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman", 13, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        dep_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep, font=("times new roman", 13, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
         
         #time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time, font=("times new roman", 13, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date, font=("times new roman", 13, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=720, height=35)

        #save button
        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv,width=18,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        #update button
        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        #delete button
        delete_btn = Button(btn_frame, text="Update",width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        #reset button
        reset_btn = Button(btn_frame, text="Reset",width=15,command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        




        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg="white", text="Attendance Details", font=("times new roman", 12, "bold"), fg="red")
        right_frame.place(x=780, y=10, width=715, height=550)

        table_frame = Frame(right_frame , bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=445)

        #=====================scroll bar===========

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance ")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #========================fetch data=================


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 



    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to " +os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)




    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


       










if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()  