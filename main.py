
with open("Input/Letters/starting_letter.txt") as file:
    lines = file.readlines()
    line_1 = lines[0]

with open("Input/Names/invited_names.txt") as names:
    for name in names:
        stripped_name = name.strip()
        new_line_1 = line_1.replace("[name]", stripped_name)
        lines.remove(lines[0])
        lines.insert(0, new_line_1)
        with open(f"Output/ReadyToSend/letters_for_{stripped_name}.txt", mode="a") as finished:
            letters = "".join(lines)
            finished.write(f"\n{letters}")










#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: strip