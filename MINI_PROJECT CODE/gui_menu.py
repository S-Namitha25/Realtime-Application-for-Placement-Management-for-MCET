# MENU
import os
from tkinter import messagebox
from tkinter import *

def do_help():
    s="REAL TIME APPLICATION FOR PLACEMENT MANAGEMENT FOR MCET"
    s+="\n\n"+"Project Description."
    s+="\n\n"+"This project streamline the job placement process."
    s+="\n\n"+"This system enhances the experience for both job seekers and companies."
    s+="\n\n"+"This project aims at optimizing the overall efficiency of the placement cell."
    s+="\n\n"+"It provide valuable insights into job seeker preferences,company requirements,and overall trends in the job market."
    messagebox.showinfo("Note",s)

def do_about():
    s="REAL TIME APPLICATION FOR PLACEMENT MANAGEMENT FOR MCET"
    s+="\n\n"+"Developed by:"
    s+="\n\n"+"MAGESH KUMAR. M.R"
    s+="\n\n"+"NAMITHA.S "
    s+="\n\n"+"ANIRUD JAGDHISH. M"
    messagebox.showinfo(" ",s)

def do_quit():
    ch= messagebox.askquestion("Confirm Quit","Are you sure?")
    if ch=="yes":
        root.destroy()

def do_menu1():
    os.system('GUI_query_coursewise-ok.py')
#
def do_menu2():
    os.system('gui_query_recruiteligible_ok.py')
#
def do_menu3():
    os.system('GUI_query_roundwise_perform-ok.py')
#
def do_menu4():
    os.system('GUI_query_roundwise_selection-ok.py')
#

root = Tk()
root.title("REAL TIME APPLICATION FOR PLACEMENT MANAGEMENT FOR MCET")
root.geometry("1280x768")
root.config(background='pink')

menubar = Menu(root)

#
querymenu = Menu(menubar, tearoff=0)
querymenu.add_command(label="Coursewise Student List", command=do_menu1)
querymenu.add_separator()
querymenu.add_command(label="Recruiter Eligibility Report", command=do_menu2)
querymenu.add_separator()
querymenu.add_command(label="Roundwise Performance", command=do_menu3)
querymenu.add_separator()
querymenu.add_command(label="Roundwise Selection", command=do_menu4)
menubar.add_cascade(label="Query", menu=querymenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=do_help)
helpmenu.add_command(label="About...", command=do_about)
menubar.add_cascade(label="Help", menu=helpmenu)

quitmenu = Menu(menubar, tearoff=0)
quitmenu.add_command(label="Close", command=do_quit)
menubar.add_cascade(label="Quit", menu=quitmenu)

root.config(menu=menubar)
root.mainloop()
