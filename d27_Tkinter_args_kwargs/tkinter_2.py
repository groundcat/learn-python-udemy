from tkinter import *

# Create a window
window = Tk()

# Create a title for the window
window.title("My Window")

# Change the size of the window
window.minsize(width=500, height=300)

# Add some padding (spaces around all widgets)
window.config(padx=20, pady=20)

# Create a label
my_label = Label(text="Hello World!", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)  # Pack the label to the window

# Update the label that we created
my_label["text"] = "Hello World twice!"
my_label.config(text="Hello World again!")  # another way

# Add padding for a widget
my_label.config(pady=20)

# Button
def button_clicked():

    # Get the user input
    user_answer = input.get()

    # Populate the label using user input
    my_label.config(text=user_answer)


# Call the function when button clicked
button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=0)


# Entry to get user input
input = Entry(width=10)
input.grid(column=3, row=2)


# Keep the window open
window.mainloop()

