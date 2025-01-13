#Roundwise Student Performance Query
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk

otxt=""
def close_window():
    master.destroy()
#
def do_query():     #User defined function
    vcompany_code = e1.get()
    vround=int(e2.get())
    
    conn=sqlite3.connect("c:/anirud/mcet.db")
    cursor=conn.cursor()
    s="select * from stu_perform where company_code ="+"'"+vcompany_code + "'"
    cursor.execute(s)
    rs=cursor.fetchall()
    i=0
    otxt=""
    otxt+="\n STUDENT PERFORMANCE FOR COMPANY ::" + vcompany_code
    otxt+="\n"+"-"*100
    if vround==1:
        otxt+="\n"+"Roll Number\t\tAptitude"
    elif vround==2:
        otxt+="\n"+"Roll Number\t\tTechnical"
    elif vround==3:
        otxt+="\n"+"Roll Number\t\tFinal"

    otxt+="\n"+"-"*100
    for row in rs:
        if vround==1:
            otxt+="\n"+row[1]+"\t\t"+row[3]
        elif vround==2:
            otxt+="\n"+row[1]+"\t\t"+row[4]
        elif vround==3:
            otxt+="\n"+row[1]+"\t\t"+row[5]
        i=i+1
#
    otxt+="\n"+"-"*100
    if i==0:
        messagebox.showinfo("Note","Details NOT Found")
    cursor.close()
    conn.close()
    t1.insert(tk.END,otxt)
    #messagebox.showinfo("Note",otxt)
#
    
master = Tk()
master.title("Roundwise Performance")
master.geometry("1280x768")
master.config(background='light blue')

#sticky to control alignment : W - West - Left / E-East - Right  / N-North - Top / S-South - Bottom
#Label
#bg-background
#fg-foreground
#bd=border
#relief=SUNKEN/RAISED/GROOVE/RIDGE

#Label
l1=tk.Label(master,text="Select Company Code:", font=("Arial",16,"bold"), bg="black", fg="white")
l1.pack()

#Entry for Company code
e1=tk.Entry(master,width=10,font=("Arial",16,"bold"))
e1.pack()

#Label
l2=tk.Label(master,text="Enter Round:", font=("Arial",16,"bold"), bg="black", fg="white")
l2.pack()

#Entry for Round
e2=tk.Entry(master,width=10,font=("Arial",16,"bold"))
e2.pack()

#Button
b1=tk.Button(master,text="Proceed", font=("Arial",12,"bold"),command=do_query)
b1.pack()

b2=tk.Button(master,text="Quit",font=("Arial",12,"bold"),command=close_window)
b2.pack()

#Text-Output
t1=tk.Text(master, height=30, width=120,font=("Lucida Console",14,"bold")) #Text
t1.pack()

tk.mainloop()
