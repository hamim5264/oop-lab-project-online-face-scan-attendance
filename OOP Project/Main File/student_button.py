from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import cv2   


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Enrollment Management")



        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar() 
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
      

        # Heading Background
        img_path = r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Student Management Background.jpg"
        img = Image.open(img_path)
        img = img.resize((1530,130), Image.LANCZOS)     
        self.photoimg = ImageTk.PhotoImage(img)       

        
        f_lb1 = Label(self.root, image=self.photoimg, border=0)  
        f_lb1.place(x=0, y=0, width=1530, height=130)


         # Background
        img3 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Heading 02.jpeg")
        img3 = img3.resize((1530,790), Image.LANCZOS)         
        self.photoimg3 = ImageTk.PhotoImage(img3)            

        
        bg_img = Label(self.root, image=self.photoimg3, border=0)       
        bg_img.place(x=0, y=130, width=1530, height=790)

        title_lbl= Label(bg_img,text="Student Enrollment",font=("Helvetica", 20),bg="white",fg="orange", border= 0)
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        # Label Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1530,height=790)

        # Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Helvetica",14, "bold"),fg="green",)
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Heading 01.jpeg")
        img_left = img_left.resize((730,130), Image.LANCZOS)         
        self.photoimg_left = ImageTk.PhotoImage(img_left)            

        
        f_lbl = Label(Left_frame, image=self.photoimg_left)      
        f_lbl.place(x=5, y=0, width=730, height=130)      

        # Course  Information
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("Helvetica",12, "bold"),fg= "orange",)
        current_course_frame.place(x=15,y=160,width=730,height=120)

        # Department Information
        dep_label= Label(current_course_frame,text="Department",font=("Helvetica",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Helvetica",10),state="read only",width=16)
        dep_combo["values"]=("Select Department","ICE","CSE","EEE","SWE","TE","MCT","JMC","NFE","CE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course Code Information
        course_label= Label(current_course_frame,text="Course Code",font=("Helvetica",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Helvetica",10,),state="read only",width=16)
        course_combo["values"]=("Select Course","CSE221","CSE222","CSE223","CSE224", "CSE315","CSE316","CSE321","CSE334", "ACT322")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year Information
        year_label= Label(current_course_frame,text="Year",font=("Helvetica",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Helvetica",10),state="read only",width=16)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester Information
        semester_label= Label(current_course_frame,text="Semester",font=("Helvetica",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("Helvetica",10),state="read only",width=16)
        semester_combo["values"]=("Select Semester","1st-Semester","2nd-Semester","3rd-Semester","4th-Semester", "5th-Semester", "6th-Semester","7th-Semester","8th-Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Student Enrollment
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Addition Information",font=("Helvetica",12,"bold"), fg="orange")
        class_student_frame.place(x=15,y=290,width=730,height=300)

        # Student ID
        student_id_label= Label(class_student_frame,text="Student ID",font=("Helvetica",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("Helvetica",10))
        student_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        # Student Name
        studentName_label= Label(class_student_frame,text="Student Name",font=("Helvetica",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("Helvetica",10))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # Division
        class_div_label= Label(class_student_frame,text="Division",font=("Helvetica",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Helvetica",10),state="read only",width=20)
        div_combo["values"]=("Dhaka","Rajshahi","Rangpur","Dhaka","Khulna","Chittagong","Barishal")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=15,sticky=W)

        # Gender
        Gander_label= Label(class_student_frame,text="Gender",font=("Helvetica",12,"bold"),bg="white")
        Gander_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Helvetica",10),state="read only",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Date of Birth
        dob_label= Label(class_student_frame,text="Date of Birth",font=("Helvetica",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Helvetica",10))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Email
        email_label= Label(class_student_frame,text="Email",font=("Helvetica",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Helvetica",10))
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Phone Po
        phone_label= Label(class_student_frame,text="Phone No",font=("Helvetica",12,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Helvetica",10))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Address
        address_label= Label(class_student_frame,text="Address",font=("Helvetica",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Helvetica",10))
        address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Advisor Name
        teacher_label= Label(class_student_frame,text="Advisor Name",font=("Helvetica",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Helvetica",10))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Photo Taking Decision
        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="white")
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes", style= "Custom.TRadiobutton")
        radio_btn1.grid(row=4,column=2)

        
        radio_btn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No", style= "Custom.TRadiobutton")
        radio_btn2.grid(row=4,column=3) 

        # Status Button
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white", border= 0)
        btn_frame.place(x=5,y=223,width=720,height=28)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("Helvetica",10,"bold"),bg="green",fg="white", border= 0)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update", command=self.update_data,width=20,font=("Helvetica",10,"bold"),bg="orange",fg="white", border= 0)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=20,command=self.delete_data,font=("Helvetica",10,"bold"),bg="red",fg="white", border= 0)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("Helvetica",10,"bold"),bg="black",fg="white", border= 0)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white", border=0)
        btn_frame1.place(x=5,y=251,width=720,height=40)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=40,font=("Helvetica",10,"bold"),bg="teal",fg="white", border= 1, foreground= "white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=("Helvetica",10,"bold"),bg="teal",fg="white", border= 1, foreground= "white")
        update_photo_btn.grid(row=0,column=1)


        # Right Frame 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Enrolled Student",font=("Helvetica",12,"bold"), fg= "green")
        Right_frame.place(x=760,y=10,width=740,height=580)

        img_right = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Student Details.jpg")
        img_right = img_right.resize((730,130), Image.LANCZOS)         
        self.photoimg_right= ImageTk.PhotoImage(img_right)            
        
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=730, height=130)


        # Search Frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Helvetica",12))
        search_frame.place(x=5,y=135,width=730,height=70)

        search_label= Label(search_frame,text="Search By:",font=("Helvetica",12,),bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("Helvetica",12,),state="read only",width=15)
        search_combo["values"]=("Select","Student ID","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("Helvetica",12,))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=14,font=("Helvetica",12,),bg="orange",fg="white", border=0)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=14,font=("Helvetica",12,),bg="orange",fg="white", border=0)
        showAll_btn.grid(row=0,column=4,padx=4)


        # Table Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=730, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "gender",  "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course Code")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Advisor Name")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("gender", width=100)
        
        self.student_table.column("dob", width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # Function Declearetion

    def add_data(self):
        
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="hamim@Sql24",database="oophamim")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_dep.get(),
                                                                                             self.var_course.get(),
                                                                                             self.var_year.get(),
                                                                                             self.var_sem.get(),
                                                                                             self.var_id.get(),
                                                                                             self.var_name.get(),
                                                                                             self.var_div.get(),
                                                                                             self.var_gender.get(),
                                                                                             self.var_dob.get(),                        
                                                                                             self.var_email.get(),
                                                                                             self.var_phone.get(),
                                                                                             self.var_address.get(),
                                                                                             self.var_teacher.get(),
                                                                                             self.var_radio1.get()
                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details added successfully",parent=self.root)
         except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root) 
    
    

    # Data Fetching
    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="hamim@Sql24",database="oophamim")
       my_cursor=conn.cursor()
       my_cursor.execute("Select * from student")
       data=my_cursor.fetchall()

       if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
             self.student_table.insert("",END,values=i)
          conn.commit()
       conn.close()  

    # Get Cursor
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0]),
       self.var_course.set(data[1]),
       self.var_year.set(data[2]),
       self.var_sem.set(data[3]),
       self.var_id.set(data[4]),
       self.var_name.set(data[5]),
       self.var_div.set(data[6]),
       self.var_gender.set(data[7]),
       self.var_dob.set(data[8]),
       self.var_email.set(data[9]),
       self.var_phone.set(data[10]),
       self.var_address.set(data[11]),
       self.var_teacher.set(data[12]),
       self.var_radio1.set(data[13]),


    # Update Function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
          try:
             Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
             if Update > 0:
                 conn = mysql.connector.connect(host="localhost", username="root", password="hamim@Sql24", database="oophamim")
                 my_cursor = conn.cursor()
                 my_cursor.execute("UPDATE student SET Department=%s, Course Code=%s, Year=%s, Semester=%s, `Student ID`=%s, Student Name=%s, Division=%s, Gender=%s,  Date of Birth=%s, Email=%s, Phone No=%s, Address=%s, Advisor Name=%s, `Photo Sample Status`=%s where `Student ID`=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    #self.var_id.get()
                     ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
          except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  


    # Delete Function
    def delete_data(self):
     if self.var_id.get() == "":
         messagebox.showerror("Error", "Student ID must be required", parent=self.root)
     else:
         try:
             delete = messagebox.askyesno("Student delete Page", "Do you want to delete this page", parent=self.root)
             if delete > 0:
                 conn = mysql.connector.connect(host="localhost", username="root", password="hamim@Sql24", database="oophamim")
                 my_cursor = conn.cursor()
                 sql = "delete from student where `Student ID`=%s"
                 val = (self.var_id.get(),)
                 my_cursor.execute(sql, val)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
         except Exception as es:
             messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)  


    # Reset Data
    def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_course.set("Select Course")
       self.var_year.set("Select Year")
       self.var_sem.set("Select Semester")
       self.var_id.set("")
       self.var_name.set("")
       self.var_div.set("Division")
       self.var_gender.set("Male")
       self.var_dob.set("")
       self.var_email.set("")
       self.var_phone.set("")
       self.var_address.set("")
       self.var_teacher.set("")
       self.var_radio1.set("")


    # Generate Photo Sample
    def generate_dataset(self):
       if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
       else:
          try:
            conn = mysql.connector.connect(host="localhost", username="root", password="hamim@Sql24", database="oophamim")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
               id+=1
            my_cursor.execute("UPDATE student SET Department=%s, Course Code=%s, Year=%s, Semester=%s, `Student ID`=%s, Student Name=%s, Division=%s, Gender=%s,  Date of Birth=%s, Email=%s, Phone No=%s, Address=%s, Advisor Name=%s, `Photo Sample Status`=%s WHERE `Student ID`=%s", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_id.get(),
                self.var_name.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                #self.var_id.get()
                   ))

            conn.commit()
            self.fetch_data()
            self.reset_data() 
            conn.close()

            # Load Pre-Define Data on Face Frontals From Opencv

            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
               gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
               faces=face_classifier.detectMultiScale(gray,1.3,5)
               for(x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w]
                  return face_cropped
               
            cap=cv2.VideoCapture(0) 
            img_id=0
            while True:
               ret,my_frame=cap.read()
               if face_cropped(my_frame) is not None: 
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(450,450)) 
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="img data/user"+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                  cv2.imshow("Crooped Face",face)

               if cv2.waitKey(1)==13 or int(img_id)==20:
                  break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets compled!!!!",parent=self.root) 
          except Exception as es:
             messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)
              

if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()
