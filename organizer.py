import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize(target_path):
    extensions = {
        'jpg': 'Images', 'png': 'Images', 'pdf': 'Documents',
        'txt': 'Documents', 'mp4': 'Videos', 'zip': 'Archives'
    }
    
    moved_count = 0
    if not target_path:
        return
        
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        if os.path.isfile(file_path) and '.' in filename:
            ext = filename.split('.')[-1].lower()
            if ext in extensions:
                subfolder = os.path.join(target_path, extensions[ext])
                os.makedirs(subfolder, exist_ok=True)
                shutil.move(file_path, os.path.join(subfolder, filename))
                moved_count += 1
    
    messagebox.showinfo("Готово", f"Порядок наведен! Перемещено файлов: {moved_count}")

# Создаем графический интерфейс
def start_gui():
    window = tk.Tk()
    window.title("Smart Organizer v1.0")
    window.geometry("300x200")

    label = tk.Label(window, text="Нажми кнопку, чтобы выбрать папку", pady=20)
    label.pack()

    def select_folder():
        folder = filedialog.askdirectory()
        if folder:
            organize(folder)

    btn = tk.Button(window, text="Выбрать папку и очистить", command=select_folder, 
                    bg="green", fg="white", padx=10, pady=5)
    btn.pack()

    window.mainloop()

if __name__ == "__main__":
    start_gui()