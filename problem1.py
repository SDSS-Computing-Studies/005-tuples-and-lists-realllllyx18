#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
List = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(List)
word1=input("Choose a person from the list to replace:").strip()
number=List.index(word1)
List.pop(int(number))
word2=input("Enter the replacement:").strip()
List.insert(int(number),word2)
print(List)
