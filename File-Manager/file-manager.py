from tkinter import filedialog, messagebox, Button, Tk, Label
import shutil
import os
import easygui


def file_open_box():
    path = easygui.fileopenbox()
    return path


def directory_open_box():
    path = filedialog.askdirectory()
    return path


def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except TypeError:
        messagebox.showinfo("!با خطا مواجعه شدم", "!فایل مورد نظر یافت نشد")


def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo("کپی موفق", "!فایل با موفقیت کپی شد")
    except:
        messagebox.showinfo("!خطا", "!کپی با شکست مواجعه شد")








