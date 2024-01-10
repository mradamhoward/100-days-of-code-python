with open("./Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()
    print(starting_letter)

    with open("./Input/Names/invited_names.txt", "r") as file_names:
        for name in file_names:
            print("Name: " + name)
            name = name.replace("\n", "")
            letter_modified = starting_letter.replace("[name]", name)
            with open("./Output/ReadyToSend/"+name+".txt", "w") as write_file:
                write_file.write(letter_modified)