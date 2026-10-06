#isogram: a word in which no letter of the alphabet occurs more than once
def isogram(text: str) -> bool:
	letters = [character.lower() for character in text if character.isalpha()]
	return len(letters) == len(set(letters))
    

#abedecerian: a word in which the letters appear in alphabetical order
def abedecerian(text: str) -> bool:
	letters = [character.lower() for character in text if character.isalpha()]
	return all(first <= second for first, second in zip(letters, letters[1:]))

#dobloon: a word in which every letter that appears in the word appears exactly twice
def dobloon(text: str) -> bool:
	letters = [character.lower() for character in text if character.isalpha()]
	return all(letters.count(letter) == 2 for letter in letters)



gram = input("test iso, abe, dob: ")
imp = input("please input what you want to test ").lower()
if gram == "iso":
	#Example: demographics
	print(imp, "is" if isogram(imp) else "is not", "an isogram")
elif gram == "abe":
	#Example: bijoux, biopsy, dimpsy
	print(imp, "is" if abedecerian(imp) else "is not", "an abedecerian")
elif gram == "dob":
	#Example: murmur, noon, reappear, sees
	print(imp, "is" if dobloon(imp) else "is not", "an dobloon")
else:
	print("invalid")




#Author of second half of code is Aarav Roy
#Date:oct 6

word=input("Please provide a word to check if its a palindrome: ").lower()
"""The user gives the computer a word and the computer spells it backwards to check if its a palindrome."""
def palindrome(word):
    if word==word[::-1]:
        print(word, "is a palindrome!!! WOOOWWWWW")
    else:
        print("Sorry,",word,"is not a palindrome")
    return

palindrome(word)

sentence=input("Please provide a sentence to check if it is a panagram: ").lower()
"""The user gives the computer a sentence. The computer runs through every letter of the alphabet using a for loop and the built in find function."""
def pangram(sentence):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if sentence.find(i)<0:
            return False
    return True

if pangram(sentence)==True:
    print("WOWZA!,"+sentence+" is a pangram!!!")
elif pangram(sentence)==False:
    print("OHHHH NOOO!!! "+sentence+" is not a pangram")


sentence2=input("Please provide a sentence to check if it is a tautogram: ")
"""The user gives the computer a sentence. I used indexes to grab the first letters and compare them."""
def tautogram(sentence2):
    #a sentence that all words start with same letter
    words=sentence2.split()
    first_word=words[0]
    first_letter=first_word[0].lower()
    for n in words:
        current_letter=n[0].lower()
        if current_letter!=first_letter:
            return False
    return True
        
if tautogram(sentence2)==True:
    print("WOOOHOOO!!! "+sentence2+" is a tautogram!")
elif tautogram(sentence2)==False:
    print("Unfortunatly, "+sentence2+" is not a tautogram")
