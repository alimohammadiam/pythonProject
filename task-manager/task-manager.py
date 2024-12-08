import tkinter as tk
from tkinter import messagebox
import json


# بارگذاری وظایف از فایل
def load_tasks():
    try:
        with open('../tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# ذخیره وظایف در فایل
def save_tasks(tasks):
    with open('../tasks.json', 'w') as file:
        json.dump(tasks, file)


# اضافه کردن وظیفه
def add_task():
    task_name = entry_task.get()
    task_description = entry_description.get()
    if task_name != "":
        tasks.append({"name": task_name, "description": task_description})
        save_tasks(tasks)
        update_task_listbox()
        entry_task.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showwarning("خطای ورودی", "لطفا یک وظیفه وارد کنید.")


# حذف وظیفه
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        save_tasks(tasks)
        update_task_listbox()
        entry_description.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("خطای انتخاب", "لطفاً یک کار را برای حذف انتخاب کنید.")


# ویرایش وظیفه
def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task_name = entry_task.get()
        task_description = entry_description.get()
        if task_name != "":
            tasks[selected_task_index] = {"name": task_name, "description": task_description}
            save_tasks(tasks)
            update_task_listbox()
            entry_task.delete(0, tk.END)
            entry_description.delete(0, tk.END)
        else:
            messagebox.showwarning("خطای ورودی", "لطفاً یک کار وارد کنید.")
    except IndexError:
        messagebox.showwarning("خطای انتخاب", "لطفاً یک کار را برای ویرایش انتخاب کنید.")


# نمایش توضیحات وظیفه انتخاب‌شده
def display_description(event):
    try:
        selected_task_index = listbox.curselection()[0]
        task = tasks[selected_task_index]
        entry_task.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_task.insert(0, task["name"])
        entry_description.insert(0, task["description"])
    except IndexError:
        entry_task.delete(0, tk.END)
        entry_description.delete(0, tk.END)


# به‌روزرسانی لیست وظایف در لیست‌باکس
def update_task_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task["name"])


# جستجو در وظایف
def search_task():
    search_term = entry_search.get().lower()
    filtered_tasks = [task for task in tasks if search_term in task["name"].lower()]

    listbox.delete(0, tk.END)
    for task in filtered_tasks:
        listbox.insert(tk.END, task["name"])


# تنظیمات اولیه
tasks = load_tasks()

# پنجره اصلی
root = tk.Tk()
root.title("لیست وظایف")

# فریم برای ورودی وظیفه و توضیحات
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# ورودی برای نام وظیفه
entry_task = tk.Entry(frame_input, width=40)
entry_task.pack(side=tk.LEFT, padx=10)

# ورودی برای توضیحات وظیفه
entry_description = tk.Entry(frame_input, width=40)
entry_description.pack(side=tk.LEFT, padx=10)

# دکمه اضافه کردن وظیفه
button_add = tk.Button(frame_input, text="افزودن وظیفه", command=add_task)
button_add.pack(side=tk.LEFT)

# دکمه ویرایش وظیفه
button_edit = tk.Button(frame_input, text="ویرایش وظیفه", command=edit_task)
button_edit.pack(side=tk.LEFT, padx=10)

# دکمه حذف وظیفه
button_delete = tk.Button(frame_input, text="حذف وظیفه", command=delete_task)
button_delete.pack(side=tk.LEFT)

# فریم برای جستجوی وظایف
frame_search = tk.Frame(root)
frame_search.pack(pady=10)

# ورودی جستجو
entry_search = tk.Entry(frame_search, width=30)
entry_search.pack(side=tk.LEFT, padx=10)

# دکمه جستجو
button_search = tk.Button(frame_search, text="جستجو", command=search_task)
button_search.pack(side=tk.LEFT)

# لیست‌باکس برای نمایش وظایف
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

# به‌روزرسانی لیست وظایف در لیست‌باکس
update_task_listbox()

# نمایش توضیحات هنگام انتخاب وظیفه
listbox.bind('<<ListboxSelect>>', display_description)

# اجرای پنجره
root.mainloop()
