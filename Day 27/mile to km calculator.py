from tkinter import *

window = Tk()
window.title("Mile to Km Convereter")
window.minsize(width=400,height=300)

def calculate():
    NEW_TEXT = float(input.get())
    km = NEW_TEXT*1.60934
    my_label_result.config(text=km)


input = Entry(width=30)
input.grid(row=0,column=1)


my_label = Label(text="Miles",font=("Arial",16))
my_label.grid(row=0,column=2)

my_label_equal = Label(text="is equal to",font=("Arial",16))
my_label_equal.grid(row=1,column=0)

my_label_result= Label(text="result",font=("Arial",16))
my_label_result.grid(row=1,column=1)

my_label_km = Label(text="Km",font=("Arial",16))
my_label_km.grid(row=1,column=2)

button = Button(text="calculate", command=calculate)
button.grid(row=2,column=1)



window.mainloop()
