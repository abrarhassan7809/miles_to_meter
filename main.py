from tkinter import *

def button_clicked():
    print("I got clicked the button")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First Frontend Design")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# label
my_label = Label(text="Hello brother", font=("Arial", 15, "normal"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)

# button
button = Button(text="Click me", command=button_clicked)
button.grid(column=3, row=3)

# entry
input = Entry(width=20)
print(input.get())
input.grid(column=2, row=2)



window.mainloop()
