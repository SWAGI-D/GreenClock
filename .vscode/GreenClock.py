from ctypes.wintypes import PHANDLE
from dataclasses import field
import tkinter as tk
from datetime import date, datetime
   

panel = tk.Tk()
panel.geometry("500x400")
panel.configure(bg='old lace')

now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

if month == "01":
        month = "January"
elif month == "02":
        month = "February"
elif month == "03":
        month = "March"
elif month == "04":
        month = "April"
elif month == "05":
        month = "May"
elif month == "06":
        month = "June"
elif month == "07":
        month = "July"
elif month == "08":
        month = "August"
elif month == "09":
        month = "September"
elif month == "10":
        month = "October"
elif month == "11":
        month = "November"
elif month == "12":
        month = "December"

#time = now.strftime("%H:%M:%S")
#print("time:", time)

label = tk.Label(panel, text=year, font=("Cambria",20), bg="old lace", fg="#013220")
label.pack()

label = tk.Label(panel, text=month + " " + day, font=("Cambria",20), bg="old lace", fg="#013220")
label.pack()

label = tk.Label(panel, text="SET ALARM", font=("Cambria",20), bg="old lace", fg="#013220")
label.place(x = 250, y = 120, anchor = 'center')

timeVar=tk.StringVar()
name=timeVar.get()
timeVar.set("")

fieldEntry = tk.Entry(panel,textvariable = timeVar, font=('Arial',10))
fieldEntry.place(x = 250, y = 200, anchor = 'center')

setButton=tk.Button(panel,text = 'SET')
setButton.place(x = 250, y = 250, anchor = 'center')

panel.mainloop()
