from tkinter import *

# Create a window
window = Tk()

# Create a title for the window
window.title("My Window")

# Change the size of the window
window.minsize(width=500, height=300)

# Create a label
my_label = Label(text="Hello World!", font=("Arial", 20, "bold"))
my_label.pack(side="top")  # Pack the label to the window

# Update the label that we created
my_label["text"] = "Hello World twice!"
my_label.config(text="Hello World again!")  # another way


# Button
def button_clicked():

    # Get the user input
    user_answer = input.get()

    # Populate the label using user input
    my_label.config(text=user_answer)


# Call the function when button clicked
button = Button(text="Click me", command=button_clicked)
button.pack()


# Entry to get user input
input = Entry(width=10)
input.pack()


# Keep the window open
window.mainloop()

