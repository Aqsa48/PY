# check if alphabet is vowel or consonant


letter = input("Enter a letter: ")

if(letter.isalpha() and (letter.upper() == 'A')or
   letter.upper() == 'E' or letter.upper() == 'I' or letter.upper() == 'O' or letter.upper() == 'U'):
    print("Is a vowel.")
else:
    print("Is a consonant.")