import customtkinter as tk
import sys
import os
import tempfile
from PIL import Image, ImageOps, ImageEnhance
from PIL import Image
from tkinter import filedialog
import pypdfium2 as pdfium
def invert(filepath):
    with tempfile.TemporaryDirectory() as path:
        pdf = pdfium.PdfDocument(filepath)
        n_pages = len(pdf)
        black_and_white_images = []

        for im in range(n_pages):
            pil_image = pdf.get_page(im).render_topil( scale=3,rotation=0,greyscale=False,optimise_mode=pdfium.OptimiseMode.PRINTING,)
            baw = pil_image.convert('RGB').convert('L')
            im_invert = ImageOps.invert(baw)
            enhancer = ImageEnhance.Contrast(im_invert)
            final_image = enhancer.enhance(7.0)
            black_and_white_images.append(final_image)
            
    black_and_white_images[0].save("out_pdf.pdf", save_all=True, append_images=black_and_white_images[1:])

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
root = tk.CTk()
root.geometry("500x350")
root.title("PDF INVERTER")



def upload():
    filepath = filedialog.askopenfilename()
    invert(filepath)   

def submit():
    print("hi")

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)




my_image = tk.CTkImage(light_image=Image.open("pngwing.com (1).png"),dark_image=Image.open("pngwing.com (1).png"),size=(150, 200))
button = tk.CTkButton(master=frame,image=my_image, text="",fg_color="transparent", command=upload )
button.pack(pady=1, padx=1,fill="both",expand=True)

button1=tk.CTkButton(master=frame,text="Submit",command=submit)
button1.pack(pady=25,padx=40,expand=True)


root.mainloop()
