import tkinter as tk
from PIL import Image, ImageTk
import cv2
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 25, "bold"), bg="white", fg="orange")
        title_lbl.place(x=0, y=-15, width=1530, height=80)

        # Cover Image
        img_top = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Face Recognitaion.jpg")
        img_top = img_top.resize((1530, 750), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=750)


        # Button For Face Recognition
        b1_1 = tk.Button(self.root, text="Face Recognition", cursor="hand2", font=("Helvetica", 15,), bg="orange", fg="white", command=self.start_face_recog, border=0)
        b1_1.place(x=670, y=626, width=200, height=40)

        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("classifier.xml")

        self.video_cap = None
        self.running = False

    def start_face_recog(self):
        if not self.running:
            self.video_cap = cv2.VideoCapture(0)
            self.running = True
            self.update()

    def update(self):
        if self.running:
            ret, img = self.video_cap.read()
            if ret:
                img = self.recognize(img)
                cv2.putText(img, "Press ESC to Exit From Camera", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == 27: 
                self.stop_face_recog()
            else:
                self.root.after(10, self.update)

    def stop_face_recog(self):
        if self.running:
            self.running = False
            self.video_cap.release()
            cv2.destroyAllWindows()

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y+h, x:x+w])
            confidence = int((100*(1-predict/300)))

            if confidence > 77:
                cv2.putText(img, f"Confidence: {confidence}%", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            else:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 3)
                cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

    def recognize(self, img):
        self.draw_boundary(img, self.faceCascade, 1.1, 10, (255, 25, 255), "Face", self.clf)
        return img

if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition(root)
    root.mainloop()
