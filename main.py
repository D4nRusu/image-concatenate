import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, filedialog
import os

TEMPLATE_PATH = "template.jpeg"
slotx = 790
sloty = 1054
pos = 811

IMAGE_SIZE = (slotx, sloty)

class ImageConcat:
    def __init__(self, root):
        self.root = root
        self.root.title("Before/After Image Generator")

        self.before_path = None
        self.after_path = None

        # UI Elements
        self.btn_before = tk.Button(root, text="Selecteaza INAINTE", command=self.select_before)
        self.btn_before.pack(pady=5)

        self.btn_after = tk.Button(root, text="Selecteaza DUPA", command=self.select_after)
        self.btn_after.pack(pady=5)

        self.output_label = tk.Label(root, text="Numele pozei:")
        self.output_label.pack(pady=(15, 0))

        self.output_entry = tk.Entry(root, width=40)
        self.output_entry.pack(pady=5, padx=40)

        self.generate_btn = tk.Button(root, text="Genereaza", command=self.generate)
        self.generate_btn.pack(pady=10)

        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack()

    def select_before(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            self.before_path = path
            self.btn_before.config(text="✅")

    def select_after(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            self.after_path = path
            self.btn_after.config(text="✅")

    def generate(self):
        if not self.before_path or not self.after_path:
            messagebox.showerror("Lipsesc imagini", "Mai selecteaza inca o data")
            return

        output_name = self.output_entry.get().strip()
        if not output_name:
            messagebox.showerror("Lipseste numele imaginii finale", "Introdu un nume pentru imaginea finala")
            return

        try:
            template = Image.open(TEMPLATE_PATH)
            before_img = Image.open(self.before_path).resize(IMAGE_SIZE)
            after_img = Image.open(self.after_path).resize(IMAGE_SIZE)

            template.paste(before_img, (0, 0))
            template.paste(after_img, (pos, 0))

            output_filename = f"{output_name}.jpeg"
            template.save(output_filename)
            self.status_label.config(text=f"Imaginea finala: {output_filename}", fg="green")

            self.btn_before.config(text="Selecteaza INAINTE")
            self.btn_after.config(text="Selecteaza DUPA")
        except Exception as e:
            self.status_label.config(text="Error: " + str(e), fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConcat(root)
    root.mainloop()