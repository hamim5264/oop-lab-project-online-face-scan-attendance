from tkinter import*
from tkinter import Label,Button
from PIL import Image, ImageTk
import tkinter as tk
from student_button import Student
import os 
from train import Train
from face_recognition import Face_Recognition


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Online Face Recognition Attendance System")
    

        # Heading Background Image Taking
        img1 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Main Background.jpg")
        img1 = img1.resize((1530,790), Image.LANCZOS)        
        self.photoimg3 = ImageTk.PhotoImage(img1)            

        
        bg_img = Label(self.root, image=self.photoimg3)    
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl= Label(bg_img,text="Online Face Recognition Attendance System",font=("Helvetica",30),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1530,height=65)


        # Student Enrollment Button
        img2 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Student Details.png")
        img2 = img2.resize((220,220), Image.LANCZOS)         
        self.photoimg4 = ImageTk.PhotoImage(img2) 

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2", border= 0)
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Enrollment",command=self.student_details,cursor="hand2",font=("Helvetica", 15),bg="white",fg="black", border= 0)
        b1_1.place(x=200,y=300,width=220,height=40)


        # Face Detector Button
        img3 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Face Detector.png")
        img3 = img3.resize((220,220), Image.LANCZOS) 
        self.photoimg5 = ImageTk.PhotoImage(img3) 

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data, border=0)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Helvetica",15),bg="white",fg="black", border=0,)
        b1_1.place(x=500,y=300,width=220,height=40)



        # Face Scan Attendance Button
        img4 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Attendance.png")
        img4 = img4.resize((220,220), Image.LANCZOS)       
        self.photoimg6 = ImageTk.PhotoImage(img4) 

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2", border=0, command=self.scan_attendance)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Scan Attendance",cursor="hand2",font=("Helvetica", 15),bg="white",fg="black", border= 0, command=self.scan_attendance)
        b1_1.place(x=800,y=300,width=220,height=40)



        # Help & Tips Button
        img5 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Help Center.png")
        img5 = img5.resize((220,220), Image.LANCZOS)         
        self.photoimg7 = ImageTk.PhotoImage(img5) 

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2", border=0,command=self.open_help)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help & Tips",cursor="hand2",font=("Helvetica", 15),bg="white",fg="black", border= 0,command=self.open_help)
        b1_1.place(x=1100,y=300,width=220,height=40)



        # Model Train With Face Button
        img6 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Train Data.png")
        img6 = img6.resize((220,220), Image.LANCZOS)         
        self.photoimg8 = ImageTk.PhotoImage(img6) 

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data, border=0)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Model Train With Face",cursor="hand2",command=self.train_data,font=("Helvetica", 15),bg="white",fg="black", border= 0)
        b1_1.place(x=200,y=580,width=220,height=40)



        # Gallery Button
        img7 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Gallery.png")
        img7 = img7.resize((220,220), Image.LANCZOS)         
        self.photoimg9 = ImageTk.PhotoImage(img7) 

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img, border=0)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Gallery",cursor="hand2",command=self.open_img,font=("Helvetica", 15),bg="white",fg="black", border= 0)
        b1_1.place(x=500,y=580,width=220,height=40)



        # Exit Button
        img8 = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Exit.jpg")
        img8 = img8.resize((220,220), Image.LANCZOS)        
        self.photoimg11 = ImageTk.PhotoImage(img8) 

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2", border=0, command=self.exit_application)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("Helvetica", 15),bg="white",fg="black", border= 0, command=self.exit_application)
        b1_1.place(x=800,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("img data")    



    # Functional Student Enrollment Button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    # Funtional Train Data Button
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

     
    # Funtional Face Recognication Button
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    # Funtional Face Scan Attendance Button
    def scan_attendance(self):
        scan_window = Toplevel(self.root)
        scan_window.title("Face Scan Attendance")
        scan_window.geometry("720x300")
        Message(scan_window, text="Hello Users!", font=("Helvetica", 12, "bold"),fg="green",width=720).pack(pady=0)
        Message(scan_window, text="This feature is under development.", font=("Helvetica", 11,),fg="red",width=720).pack(pady=0)
        Message(scan_window, text="Stay Tuned!", font=("Helvetica", 10),fg="black",width=720).pack(pady=0)


    # Funtional Help & Tips Button
    def open_help(self):
        help_window = Toplevel(self.root)
        help_window.title("Help & Tips")
        help_window.geometry("720x300")
        Message(help_window, text="We Are Trying Our Best to Provide The Best Solution For Online Attendance System.", font=("Helvetica", 12, "bold"),fg="green",width=720).pack(pady=20)
        Message(help_window, text="Developers & Contributors:", font=("Helvetica", 12, "bold"),fg="maroon",width=720).pack(pady=0)
        Message(help_window, text="MD. ABDUL HAMIM LEON", font=("Helvetica", 10),fg="black",width=720).pack(pady=0)
        Message(help_window, text="MUSFIQUR RAHMAN ZIHAD", font=("Helvetica", 10,),fg="black",width=720).pack(pady=0)
        Message(help_window, text="MD. RUBEL MIAN", font=("Helvetica", 10,),fg="black",width=720).pack(pady=0)
        Message(help_window, text="FAHARIA AKTER", font=("Helvetica", 10,),fg="black",width=720).pack(pady=0)
        Message(help_window, text="Developed By:", font=("Helvetica", 12, "bold"),fg="maroon",width=720).pack(pady=0)
        Message(help_window, text="Team Masterminds", font=("Helvetica", 12,),fg="black",width=720).pack(pady=0)
        Message(help_window, text="Email: hamim15-5264@diu.bd", font=("Helvetica", 10,),fg="black",width=720).pack(pady=0)
    

    # Funtional Exit Button
    def exit_application(self):
        self.root.quit()

        

if __name__ == "__main__":
    root = tk.Tk()
    obj = FaceRecognitionSystem(root)
    app = FaceRecognitionSystem(root)
    root.mainloop()
