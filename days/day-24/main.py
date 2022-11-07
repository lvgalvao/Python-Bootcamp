#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("project 24 mail merge project/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("project 24 mail merge project/Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_text = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"project 24 mail merge project/Output/ReadyToSend/Pode_enviar_{stripped_name}", "w") as new_letter:
            new_letter.write(new_text)



# read names

# for names write in letter


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp