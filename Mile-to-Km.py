from tkinter import *

window = Tk()
window.title("Miles to Km Converter")

label0 = Label(text="is equal to")
label0.grid(column=0, row=1)

entry = Entry()
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="0")
label2.grid(column=1, row=1)

label3 = Label(text="km")
label3.grid(column=2, row=1)

# defining click function
def click():
  result = int(entry.get())*1.609 # 1mile = 1.609km
  label2.config(text=result)

button = Button(text="Calculate", command=click)
button.grid(column="1", row="2")

window.mainloop()
