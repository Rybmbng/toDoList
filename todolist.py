import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

def tambah_tugas():
    task = task_entry.get()
    task_time = time_entry.get()
    task_date = date_entry.get()
    
    if task and task_time and task_date:
        listbox.insert(tk.END, f"{task} - {task_date} {task_time}")
        task_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Input task and time.")

def hapus_tugas():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Error Hapus", "Mark task to delete.")

def tandai_selesai():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task} [SELESAI]")
    except IndexError:
        messagebox.showwarning("Error Selesai", "Mark task to complete.")

root = tk.Tk()
root.title("ToDo List")

root.configure(bg="lightblue")

task_label  = tk.Label(root, height=1, text="My Activity:")
task_label.pack()
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

time_label = tk.Label(root, text="ToDo Clock (HH:MM):")
time_label.pack()
time_entry = tk.Entry(root, width=10)
time_entry.pack(pady=5)

date_label = tk.Label(root, text="ToDo Date :")
date_label.pack()
date_entry = DateEntry(root, width=12, background='lightblue',
                       foreground='white', borderwidth=2)
date_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=tambah_tugas)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10, background="lightblue")
listbox.pack(pady=10)

done_button = tk.Button(root, text="Mark Done", command=tandai_selesai)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=hapus_tugas)
delete_button.pack(pady=5)

root.mainloop()
