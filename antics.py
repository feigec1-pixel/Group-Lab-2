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