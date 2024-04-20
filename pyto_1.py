import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def remove_prefix_from_pdfs(folder_path):
    files = os.listdir(folder_path)
    pdf_files_found = False
    for file_name in files:
        if file_name.lower().endswith('.html'):
            pdf_files_found = True
            old_path = os.path.join(folder_path, file_name)
            new_file_name = file_name.replace('prefix_sprefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_prefix_', '', 1)
            new_path = os.path.join(folder_path, new_file_name)
            os.rename(old_path, new_path)
    if pdf_files_found:
        messagebox.showinfo("Success", "Prefix removed from PDFs in selected folder.")
    else:
        messagebox.showwarning("Warning", "No PDF files found in the selected folder.")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        remove_prefix_from_pdfs(folder_path)

def resize_bg(event):
    # Resize the background image to match the window size
    new_width = event.width
    new_height = event.height
    resized_bg = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(resized_bg)
    bg_label.config(image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection

root = tk.Tk()
root.title("Remove Prefix from PDFs")

# Load the background image
bg_image = Image.open("bkround.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Set background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

instruction_label = tk.Label(root, text="Select a folder containing PDF files with 'prefix-' in their names:", bg='white')
instruction_label.pack(pady=10)

select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=5)

# Bind the resizing event of the window to the resize_bg function
root.bind("<Configure>", resize_bg)

root.mainloop()
