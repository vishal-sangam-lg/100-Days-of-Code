# Label Button Entry Text Spinbox Scale Radiobutton Checkbox Listbox
from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

# my_label.pack(side="bottom")
# my_label.pack(expand=True)
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# my_label["text"] = "New text"
# my_label.config(text="New Text")

# Button


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# button.pack()
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
