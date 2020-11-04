from difflib import get_close_matches
import json

data = json.load(open("./data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
        f"Did you mean {get_close_matches(word, data.keys())[0]} instead?. Enter Y if yes or N  if No: "
        )
        if yn == "y" or yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n" or yn == "N":
            return "The Word does'nt exist please double check it."
        else:
            return "We did'nt understand your entry"

    else:
        print("The Word does'nt exist please double check it.")

word = input("Enter a Word: ")

output = translate(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)