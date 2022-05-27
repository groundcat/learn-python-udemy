
with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names_list = invited_names.readlines()  # Read all the lines in the file as a list

    for name in names_list:
        name = name.strip()  # Remove the spaces at the beginning and end of the string

        with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
            letter = starting_letter.read()  # Read the whole file as a string
            letter = letter.replace("[name]", name)

            with open("./Output/ReadyToSend/" + name + ".txt", "w") as ready_to_send:
                ready_to_send.write(letter)
