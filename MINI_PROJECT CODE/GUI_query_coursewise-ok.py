#Coursewise Student Query
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk

otxt=""

def close_window():
    master.destroy()
# 
def do_query():     #User defined function
    conn=sqlite3.connect("c:/anirud/mcet.db")
    cursor=conn.cursor()
    vcoursecode = e1.get()
    s="Select * from students where coursecode="+"'"+vcoursecode + "'"
    cursor.execute(s)
    rs=cursor.fetchall()
    i=0
    otxt=""
    otxt = "\n\t\t\tSTUDENT LIST FOR COURSE :" + vcoursecode
    otxt+="\n"+("-"*100)
    otxt+="\n"+"Roll Number\t\tStudent Name\t\tCourse\tCGPA\tPlacement Status"
    otxt+="\n"+("-"*100)
    for row in rs:
        otxt+="\n"+str(row[0])+"\t\t"+str(row[1])+"\t\t"+str(row[2])+"\t"+str(row[13])+"\t"+str(row[21])
        i=i+1
    #
    otxt+="\n"+("-"*100)
    if i==0:
        messagebox.showinfo("Note","Details NOT found for this course...")
    cursor.close()
    conn.close()
    t1.insert(tk.END,otxt)
    #messagebox.showinfo("Note",otxt)
#
    
master = Tk()
master.title("Coursewise Student List")
master.geometry("1280x768")
master.config(background='light blue')

#sticky to control alignment : W - West - Left / E-East - Right  / N-North - Top / S-South - Bottom
#Label
#bg-background
#fg-foreground
#bd=border
#relief=SUNKEN/RAISED/GROOVE/RIDGE

#Label
l1=tk.Label(master,text="Select Course Code:", font=("Arial",16,"bold"), bg="black", fg="white")
l1.pack()

#Entry for coursecode
e1=tk.Entry(master,width=10,font=("Arial",16,"bold"))
e1.pack()

#Button
b1=tk.Button(master,text="Proceed", font=("Arial",12,"bold"),command=do_query)
b1.pack()

b2=tk.Button(master,text="Quit",font=("Arial",12,"bold"),command=close_window)
b2.pack()

#Text-Output
t1=tk.Text(master, height=30, width=120,font=("Lucida Console",14,"bold")) #Text
t1.pack()

tk.mainloop()


