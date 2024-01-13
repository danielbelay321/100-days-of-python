from tkinter import *

window = Tk()
window.title("My First Program")
window.minsize()



my_label = Label(text="label",font=("Arial",24))
my_label.pack(side="left")

# my_label["text"] = "NEW TEXT"
# my_label.config(text="NEW TEXT")

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)

button.pack(side="left")

input = Entry(width=100)
print(input.get())
input.pack(side="left")

# def radio_used():
#     print(radio_state.get())
#
# radio_state = IntVar()
# radioButton = Radiobutton(text="option",value=1, variable=radio_state,command=radio_used)
# radioButton.pack()
# window.mainloop()



