import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = tk.Label(self.root, text="Train Data Set", font=("Helvetica", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"F:\Academic Documents & Recorded Class\6th Semester\CSE222 Object Oriented Programming Lab II\OOP Project\Assets\Model Training.jpg")
        img_top = img_top.resize((1530, 790), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=790)

        # Train Button
        b1_1 = tk.Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("Helvetica", 25), bg="white", fg="red", border=0)
        b1_1.place(x=635, y=670, width=250, height=50)

    def train_classifier(self):
        data_dir = "img data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Directory not found")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        if not path:
            messagebox.showerror("Error", "No images found in the directory")
            return

        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert('L')
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image_path)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Train", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid images found for training")
            return

        ids = np.array(ids)

        # Train Classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!!")

if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()
