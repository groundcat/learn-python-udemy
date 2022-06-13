from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to KM Calculator")
window.minsize(width=300, height=200)

# Add some padding (spaces around all widgets)
window.config(padx=50, pady=50)

# Labels
label = Label(text="Mile to KM Calculator")

# Text
text_miles = Entry(width=10)
text_miles.focus()
text_miles.insert(END, "0")
text_miles.grid(column=2, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=3, row=1)

label_isequalto = Label(text="is equal to")
label_isequalto.grid(column=1, row=2)

label_answer = Label(text="0")
label_answer.grid(column=2, row=2)

label_km = Label(text="Km")
label_km.grid(column=3, row=2)

# Button
def button_clicked():

    # Get the user input
    miles = float(text_miles.get())

    km = miles * 1.609344
    km = round(km, 2)

    # Populate the label using user input
    label_answer.config(text=km)


# Call the function when button clicked
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


# Keep the window open
window.mainloop()
