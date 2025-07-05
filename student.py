from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from itertools import count


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #====================Variables Declaration========================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_class_div = StringVar()
        self.var_roll_no = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

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
        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="DARKGREEN")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)


        # left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg="white", text="Student Details", font=("times new roman", 12, "bold"), fg="red")
        left_frame.place(x=10, y=10, width=750, height=550)

        img_left=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\right image.jpg")
        img_left=img_left.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=110)

        #current course
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, bg="white", text="Current Course", font=("times new roman", 12, "bold"), fg="red")
        current_course_frame.place(x=5, y=115, width=730, height=100)


        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"),width=20, state="readonly")
        dep_combo['values'] = ("Select Department", "Computer Science", "Information Technology", "Electronics", "Mechanical")
        dep_combo.current(0)
        # dep_combo.bind("<<ComboboxSelected>>", self.fetch_course_data)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width=20, state="readonly")
        course_combo['values'] = ("Select Course", "B.Tech", "M.Tech", "MBA", "PhD")
        course_combo.current(0)
        # course_combo.bind("<<ComboboxSelected>>", self.fetch_course_data)
        course_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width=20, state="readonly")
        year_combo['values'] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        # year_combo.bind("<<ComboboxSelected>>", self.fetch_course_data)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=20, state="readonly")
        sem_combo['values'] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8")
        sem_combo.current(0)
        # sem_combo.bind("<<ComboboxSelected>>", self.fetch_course_data)
        sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        #Class Student Information
        class_Student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, bg="white", text="Class Student Information", font=("times new roman", 12, "bold"), fg="red")
        class_Student_frame.place(x=5, y=215, width=730, height=310)


        # Student ID
        studentId_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry =ttk.Entry(class_Student_frame,textvariable=self.va_student_id,width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_student_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        #class_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_class_div, width=20, font=("times new roman", 13, "bold"))
        #lass_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_class_div,width=20,font=("times new roman", 12, "bold"), state="readonly")
        class_div_combo['values'] = ("Select Class Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll_no, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman", 12, "bold"), state="readonly")
        gender_combo['values'] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)        

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Button Frame
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        # Button Frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=720, height=35)

        #save button
        save_btn = Button(btn_frame, text="Save",command=self.add_data,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        #update button
        update_btn = Button(btn_frame, text="Update",command=self.update_data,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        #delete button
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        #reset button
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=245, width=720, height=35)


        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample",width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)


        update_photo_btn = Button(btn_frame1, text="Update Photo Sample",width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)




        # right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg="white", text="Student Details", font=("times new roman", 12, "bold"), fg="red")
        right_frame.place(x=780, y=10, width=710, height=550)


        img_right=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\right image.jpg")
        img_right=img_right.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=730, height=110)


        # Search System
        Search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, bg="white", text="Search System", font=("times new roman", 12, "bold"), fg="red")
        Search_frame.place(x=5, y=115, width=700, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo['values'] = ("Select", "Roll No", "Phone No", "StudentID")
        search_combo.current(0)
        search_combo.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        search_btn = Button(Search_frame, text="Search", width=13, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=4, padx=5, pady=5)

        show_all_btn = Button(Search_frame, text="Show All", width=13, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        show_all_btn.grid(row=0, column=5, padx=5, pady=5)


        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=190, width=700, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)


        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "class_div", "roll_no","gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("class_div", text="Class Division")
        self.student_table.heading("roll_no", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No:")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table['show'] = 'headings'

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("class_div", width=100)
        self.student_table.column("roll_no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



        #===================Function Declarations========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.va_student_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Anisagu@2328",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.va_student_id.get(),
                                                                                        self.var_student_name.get(),
                                                                                        self.var_class_div.get(),
                                                                                        self.var_roll_no.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get()
                                                                                  ))
                

                conn.commit()
                self.fetch_data()  # Refresh the table after adding data
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


      #=======================Fetch Course Data========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Anisagu@2328",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()


    #=======================get cursor data========================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']

        if data and len(data) >= 15:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.va_student_id.set(data[4])
            self.var_student_name.set(data[5])
            self.var_class_div.set(data[6])
            self.var_roll_no.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])


    #=======================Update data========================
    def update_data(self):  
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.va_student_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root) 

        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Anisagu@2328", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s,Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_iD=%s",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                                                                        self.var_semester.get(),
                                                                                                                                        self.var_student_name.get(),
                                                                                                                                        self.var_class_div.get(),
                                                                                                                                        self.var_roll_no.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_teacher.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.va_student_id.get()
                                                                                                                                 ))
                                                                                                                                        
                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()  # Refresh the table after updating data
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)



#=======================Delete data========================
    def delete_data(self):
        if self.va_student_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Anisagu@2328", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_iD=%s"
                    value = (self.va_student_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()  # Refresh the table after deleting data
                conn.close()
                messagebox.showinfo("Delete", "Student details deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


#=======================Reset data========================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_student_id.set("")
        self.var_student_name.set("")
        self.var_class_div.set("Select Class Division")
        self.var_roll_no.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("Select Teacher")
        self.var_radio1.set("")


#=====================Generate Data Set========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.va_student_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root) 
            

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Anisagu@2328", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id =2
                
                
                for x in myresult:
                    id += 0
                id = str(id)
                id = int(id) + 1  # Increment ID for new student
                my_cursor.execute("Update student set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s,Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_iD=%s",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                                                                        self.var_semester.get(),
                                                                                                                                        self.var_student_name.get(),
                                                                                                                                        self.var_class_div.get(),
                                                                                                                                        self.var_roll_no.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_teacher.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.va_student_id.get() == id + 1
                                                                                                                                 ))
                                                                                                                                      
                conn.commit()
                self.fetch_data()  # Refresh the table after generating dataset
                self.reset_data()
                messagebox.showinfo("Success", f"ID: {id} - Student details added successfully", parent=self.root)
                # Close the connection
                conn.close()

                    
            

            #=======================Load Predefined Data========================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor of 1.3 and minimum neighbors of 5
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y+h, x:x+w]
                            return face_cropped
                        
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                        ret,my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error occurred: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()       