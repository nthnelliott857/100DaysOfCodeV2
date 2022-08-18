import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

size = nr_letters + nr_symbols + nr_numbers
print(size)
password = ""
#print(password)

#for i in range(0, size):
 #   if (i < size - (nr_symbols + nr_numbers)):
  #      random_index = random.randint(0, 51)
   #     #print(random_index)
    #    password += letters[random_index]
     #   print(password)
    #elif(i >= size - nr_symbols - nr_numbers and i < size - nr_numbers):
     #   random_index1 = random.randint(0, 9)
      #  password += str(numbers[random_index1])
       # print(password)
    #elif(i >= size - nr_numbers and i < size):
     #   random_index2 = random.randint(0, 8)
      #  password += symbols[random_index2]
       # print(password)

let_sum = 0
num_sum = 0
sym_sum = 0
password_ready = False
loops = 0

while(not password_ready):
    which_char = random.randint(0,2)
    if (which_char == 0 and let_sum < nr_letters):
        random_index = random.randint(0, 51)
        password += letters[random_index]
        let_sum += 1
    elif(which_char == 1 and sym_sum < nr_symbols):
        random_index1 = random.randint(0, 8)
        password += symbols[random_index1]
        sym_sum += 1
    elif (which_char == 2 and num_sum < nr_numbers):
        random_index2 = random.randint(0, 9)
        password += numbers[random_index2]
        num_sum += 1
    print(password)
    loops += 1
    
    if (let_sum == nr_letters and num_sum == nr_numbers and sym_sum == nr_symbols):
        password_ready = True

print("Your password is:" + password)
print(f"It was generated in {loops} iterations")
