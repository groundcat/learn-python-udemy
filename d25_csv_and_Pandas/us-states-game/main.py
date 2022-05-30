import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US States Game")

# Load the background image
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# Read the CSV file
csv_file = "50_states.csv"
df = pd.read_csv(csv_file)
states = df.state
states_list = states.tolist()

answered_states = []

while len(answered_states) < 50:

    # Ask the user for the name of the state
    answer_state = screen.textinput(f"Guess the State {len(answered_states)}/50 correct!", "What is the name of the state? (Type 'quit' to quit)")
    answer_state = answer_state.title()  # Make the first letter capital

    print(answer_state)

    # If the users asks to quit, end the game
    if answer_state == "Quit":
        break

    # If the answer is found in the list, print the message
    if answer_state in states_list and answer_state not in answered_states:
        print("You guessed correctly!")

        # Create a turtle object
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        my_state = df[states == answer_state]
        print(my_state)
        x = int(my_state.x)
        y = int(my_state.y)
        print(f"The coordinates of {answer_state} are {x} and {y}")
        t.goto(x, y)
        t.write(answer_state)

        # Add the state to the list of answered states
        answered_states.append(answer_state)

# Make a list of the states that the user did not answer
unanswered_states = [state for state in states_list if state not in answered_states]

# Save the list of states that the user did not answer to a CSV file
unanswered_states_file = "unanswered_states.csv"
df = pd.DataFrame(unanswered_states, columns=["state"])
df.to_csv(unanswered_states_file, index=False)

# Keep the window open
turtle.mainloop()
