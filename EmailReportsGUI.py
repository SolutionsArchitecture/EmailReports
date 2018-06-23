import tkinter
from tkinter import *
from SupportFiles import email_data_reports
from datetime import datetime

top = tkinter.Tk()

Label(top, text='Company Id').grid(row=0, column=0)
E1 = Entry(top, bd = 5)
E1.grid(row=0, column=1)

Label(top, text='Start Date').grid(row=1, column=0)
E2 = Entry(top)
E2.grid(row=1, column=1)

Label(top, text='End Date').grid(row=2, column=0)
E3 = Entry(top)
E3.grid(row=2, column=1)

def validDate():
    startDate = E2.get()
    endDate = E3.get()
    datetimeStart = datetime.strptime(startDate,"%Y%m%d")
    datetimeEnd = datetime.strptime(endDate,"%Y%m%d")
    delta = datetimeEnd - datetimeStart
    rangeDate = datetime.today() - datetimeStart
    print("Running for " + str(delta.days) + " day period")
    if( delta.days > 32 or delta.days < 0):
        print("Time Range Over 30 Days Or Reversed. Cancelling Query")
        return False
    elif(rangeDate.days > 60):
        print("Can't run report for times greater than 60 days ago")
        return False
    else:
        return True
    
def runDomain():
    try:
        print('Running Domain Report on Company ID ', E1.get())
        if( validDate() ):
            email_data_reports.runReport(E1.get(),E2.get(),E3.get(),'d')
    except ValueError:
        print("Please Enter Values to Run Report")
    
def runSubject():
    try:
        print('Running Subject Report on Company ID ', E1.get())
        if( validDate() ):
            email_data_reports.runReport(E1.get(),E2.get(),E3.get(),"s" + str(checkVal.get()))
    except ValueError:
        print("Please Enter Values to Run Report")

def runPush():
    try:
        print('Running Push Report on Company ID ', E1.get())
        if( validDate() ):
            email_data_reports.runReport(E1.get(),E2.get(),E3.get(),'p')
    except ValueError:
        print("Please Enter Values to Run Report")

def deleteTables():
    email_data_reports.runReport(E1.get(),E2.get(),E3.get(),'delete')
    
Button(top, text='Start Subject Report', command=runSubject).grid(row=3,column=0)           
Button(top, text='Start Domain Report', command=runDomain).grid(row=4,column=0)

checkVal = IntVar()
Checkbutton(top, text="AB ON/OFF", variable=checkVal).grid(row=3,column=1) 

Frame(top,bg="black").grid(row=5,columnspan=2,stick=E+W)

Button(top, text='Start Push Report', command=runPush).grid(row=6,column=0)
Button(top, text='Delete Tables', command=deleteTables).grid(row=6,column=1)

top.mainloop()
