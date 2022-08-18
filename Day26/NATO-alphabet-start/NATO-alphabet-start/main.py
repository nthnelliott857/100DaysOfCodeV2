student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
nato_alphabet_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_frame.iterrows()}
# print(nato_alphabet)

students = {}

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # num = row.index
#     # Access row.student or row.score
#     student = row.student
#     #letters = [student[letter] for letter in range(len(student))]
#     matching_letters = [nato_alphabet[letter] for letter in student]
#     print(matching_letters)
#         #[code for (letter, code) in nato_alphabet.items() if letter in letters]
#
# print(students)
#

# print(student_data_frame)
# print(nato_alphabet_frame)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [nato_alphabet[letter] for letter in word]
print(output_list)
# {new_key:new_value for (index, row) in df.iterrows()}
