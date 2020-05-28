# defining pig_latin function
def pig_latin(input_phrase):
    #separating into separate words
    input_phrase = input_phrase.split()
    
    #defining vowels
    vowels = ["a", "e", "i", "o", "u"]

    #translating to pig latin word by word
    for k in range(len(input_phrase)):
        i = input_phrase[k]
        
        #cases starting with consonants
        if i[0] not in vowels:
            for p in range(1, len(i)):
                if i[p] in vowels:
                    input_phrase[k] = i[p:len(i)] + i[:p]+ "ay"
                    break
        
        #cases starting with vowels
        else:
            input_phrase[k] = i + "way"

    #concatenation        
    return " ".join(input_phrase)

#receiving input from user
input_phrase = str(input("Please enter a phrase to be translated to pig latin: "))

#final result
print(pig_latin(input_phrase))