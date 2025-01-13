#Coursewise Student Query
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#
def close_window():
    master.destroy()
#
def do_query():     #User defined function
    conn=sqlite3.connect("c:/anirud/mcet.db")
    cursor1=conn.cursor()
    vcompany_code = e1.get()
    vyear = e2.get()
    vqualification1=""
    vqualification2=""
    vqualification3=""
    vmark_tenth=""
    vmark_plus2=""
    vmark_diploma=""
    vcgpa=""
    
    otxt=""
    #Recruiter Table
    s ="select * from recruiters where company_code = " + "'" + vcompany_code + "'"
    s = s + " and year_of_study = " + vyear
    cursor1.execute(s)
    rs1=cursor1.fetchall()
    for row in rs1:
        otxt+="\n"+"Placement for   :" + row[5]
        otxt+="\n"+"No. of Positions :" + str(row[6])
        vqualification1 = row[7]
        vqualification2 = row[8]
        vqualification3 = row[9]
        otxt+="\n"+"Qualification 1 :"+ vqualification1
        otxt+="\n"+"Qualification 2 :"+vqualification2
        otxt+="\n"+"Qualification 3 :"+vqualification3
        otxt+="\n"+"Eligibility Criteria:"
        vmark_tenth=row[10]
        vmark_plus2=row[11]
        vmark_diploma=row[12]
        vcgpa=row[13]
        otxt+="\n"+"10th Mark:"+ str(vmark_tenth)
        otxt+="\n"+"12th Mark:"+ str(vmark_plus2)
        otxt+="\n"+"Diploma Mark:"+ str(vmark_diploma)
        otxt+="\n"+"CGPA :"+ str(vcgpa)
        otxt+="\n"+"Arrear History  :"+ str(row[20])
        otxt+="\n"+"Arrear Current :"+ str(row[21])
   #    
    cursor1.close()

    #Student Eligiblity List
    i=0
    otxt+="\n"+"\nELIGIBLE STUDENT LIST:" 
    otxt+="\n"+"-"*100 
    otxt+="\n"+"Roll Number\t\tStudent Name\t\tCourse\t10th \t+2 \tDiploma\tCGPA"
    otxt+="\n"+"-"*100

    s ="select * from students where current_year = " + vyear
    s = s+ " and (coursecode = " + "'" + vqualification1 + "'"
    s = s+ " or coursecode = " + "'" + vqualification2 + "'"
    s = s+ " or coursecode = " + "'" + vqualification3 + "'" + ")"
    s= s + " and mark_tenth >= " + str(vmark_tenth)
    s= s + " and (mark_plus2 >= " + str(vmark_plus2)
    s= s + " or mark_diploma >= " + str(vmark_diploma) + ")"
    s= s + " and cgpa >= " + str(vcgpa)
    cursor2=conn.cursor()
    cursor2.execute(s)
    rs2=cursor2.fetchall()
    for row in rs2:
        otxt+="\n"+str(row[0])+"\t\t"+str(row[1])+"\t\t"+str(row[2])+"\t"+str(row[6])+"\t"+str(row[7])+"\t"+str(row[8])+"\t"+str(row[12])
        i=i+1
    #
    otxt+="\n"+"-"*100 
    cursor2.close()

    otxt+="\n"+ "-"*100 
    if i==0:
        messagebox.showinfo("Note","Details NOT found for this Company...")
    conn.close()
    t1.insert(tk.END,otxt)
    #messagebox.showinfo("Note",otxt)
#
#sticky to control alignment : W - West - Left / E-East - Right  / N-North - Top / S-South - Bottom
#Label
#bg-background
#fg-foreground
#bd=border
#relief=SUNKEN/RAISED/GROOVE/RIDGE

master = Tk()
master.title("Recruiter Eligibility List")
master.geometry("1280x768")
master.config(background='light blue')

#Label
l1=tk.Label(master,text="Select Company Code:", font=("Arial",16,"bold"), bg="black", fg="white")
l1.pack()

#Entry for Company Code
e1=tk.Entry(master,width=10,font=("Arial",16,"bold"))
e1.pack()

#Label
l2=tk.Label(master,text="Enter Year of Study:", font=("Arial",16,"bold"), bg="black", fg="white")
l2.pack()

#Entry for Year of Study
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
#


