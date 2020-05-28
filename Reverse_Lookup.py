#defining reverseLookup function
def reverseLookup(dictionary, value):
    keys = []
    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)
    return keys

#test dictionary
calories_per_nutrient = {"carbohydrates" : "four", "protein" : "four", "fat" : "nine"}

#check for cases with multiple keys
print("What nutrients have four calories per gram?")
print(reverseLookup(calories_per_nutrient, "four"))
print()

#check for cases with one key
print("What nutrient has nine calories per gram?")
print(reverseLookup(calories_per_nutrient, "nine"))
print()

#check for cases with no keys
print("What nutrients have seventy-two calories per gram?")
print(reverseLookup(calories_per_nutrient, "seventy-two"))
print()