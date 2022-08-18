alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Import and print the logo from art.py when the program starts.
#import art

#print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

def caesar(message, shift_num):
    if direction == "decode":
        shift_num = -1 * shift_num
    final_text = ""
  #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    for letter in message:
        if letter in alphabet:
            letter_index = alphabet.index(letter) + shift_num
            if (letter_index > 25):
                #letter_index = (letter_index % 25) - 1
                letter_index = (letter_index - 1) % 25 
            elif(letter_index < 0):
                letter_index = (letter_index + 1) % 25 
                final_text += alphabet[letter_index]
            else:
                final_text += letter
    print(f"The {direction}d text is {final_text}\n")
  
    
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
direction = ""
play_again = True

while(play_again):
    input_bad = True
    while (input_bad):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if (direction == "encode" or direction == "decode"):
        input_bad = False
    else: 
        print("INVALID INPUT ENTERED")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(message=text, shift_num=shift)
    answer = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.\n ").lower()
    if (answer == "no"):
        play_again = False
        print("Goodbye")

 



