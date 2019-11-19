import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()]


def add_app():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfile(initialdir="/", title="Select File",
                                      filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=add_app)
openFile.pack()

run_app = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg="#263D42", command=run_apps)
run_app.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
