# defining pig_latin function
def pig_latin(input_word):
    
    #checking if word starts with a consonant
    if input_word[0] != "a" and input_word[0] != "e" and input_word[0] != "i" and input_word[0] != "o" and input_word[0] != "u":
        
        #finding all consonants until first vowel and translating word to pig latin through concantenation
        for i in range(1, len(input_word)):
            if input_word[i] == "a" or input_word[i] == "e" or input_word[i] == "i" or input_word[i] == "o" or input_word[i] == "u":
                translation = input_word[i:len(input_word)] + input_word[:i]+ "ay"
                break
    
    #cases for when word starts with vowel
    else:
        translation = input_word + "way"
    return translation

#receiving input from user
input_word = str(input("Please enter a word to be translated to pig latin: "))

#final result
print(pig_latin(input_word))