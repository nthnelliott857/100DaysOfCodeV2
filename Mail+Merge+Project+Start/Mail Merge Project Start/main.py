#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



    #C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt
s = open("Input\Letters\starting_letter.txt")
starting_letter = s.read()

f = open(r"Input\Names\invited_names.txt")
invited_names_raw = f.readlines()

# print(invited_names)
print(starting_letter)

letters = []
invited_names = []

for name in invited_names_raw:
    invited_names.append(name.split('\n'))


for name in invited_names:
    letters.append(starting_letter.replace("[name]", name[0]))


for i in range(0, len(letters)):
    file_name = "example"
    file_name += str(i)
    file_name += ".txt"
    with open(rf"Output\ReadyToSend\{file_name}", mode="w") as output:
        output.write(letters[i])





#C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend