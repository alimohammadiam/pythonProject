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


def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo("حذف موفق", "!فایل با موفقیت حذف شد")
    except:
        messagebox.showinfo("خطا", "!حذف فایل با شکست مواجعه شد")


def rename_file():
    try:
        file = file_open_box()
        path1 = os.path.dirname(file)
        extension = os.path.splitext(file)[1]
        new_name = input('new name: ')
        path2 = os.path.join(path1, new_name + extension)
        os.rename(file, path2)
    except:
        messagebox.showinfo("خطا", "!تغییر نام ناموفق")


def move_file():
    source = file_open_box()
    destination = directory_open_box()
    if source == destination:
        messagebox.showinfo("!خطا", "!مسیر انتقال مشابه مسیر فعلی است")
    else:
        try:
            shutil.move(source, destination)
            messagebox.showinfo("!موفق", "فایل یا موفقیت انتقال یافت")
        except:
            messagebox.showinfo("!خطا", "!انتقال فایل ناموفق بود")


def make_directory():
    path = directory_open_box()
    name = input('name: ')
    path = os.path.join(path, name)
    try:
        os.mkdir(path)
        messagebox.showinfo("!موفق", "دایرکتوری با موفقیت ایجاد شد")
    except:
        messagebox.showinfo("!خطا", "!دایرکتوری ساخته نشد")











