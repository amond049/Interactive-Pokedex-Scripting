import requests
import string
from bs4 import BeautifulSoup

def processing(string):
    firstClosingBracket = string.index(">")
    secondOpeningBracket = string[firstClosingBracket + 1:].index("<")

    return string[firstClosingBracket + 1:firstClosingBracket + secondOpeningBracket + 1]

while True:
    pokemon = input("Please enter the name of the pokemon you would like to get the pokedex entry of: \n")

    # Need to do some pre-processing to account for the weird punctuation in the pokemon name
    formattedPokemonName = ""
    for letter in pokemon:
        if letter == "-":
            formattedPokemonName += "-"
        elif letter not in string.punctuation and letter != " ":
            formattedPokemonName += letter
        elif letter == " ":
            formattedPokemonName += "-"

    # CHECKLIST OF ITEMS TO RETRIEVE
    # Pokedex Number -> Done
    # Typing -> Done
    # Height -> Done
    # Weight
    # Abilities
    # Base stats 

    URL = "https://pokemondb.net/pokedex/" + formattedPokemonName.lower()
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Getting the pokedex number of the pokemon in question
    pokedexNumber = str(soup.find("strong"))
    allTypes = list(soup.findAll("a", class_="type-icon"))

    # Getting the typing of the pokemon
    typing = []
    for i in range(2):
        if "title" not in str(allTypes[i]):
            typing.append(str(allTypes[i]))

    # Getting the height of the pokemon
    height = soup.find("th", string="Height")
    # Getting the height value and then formatting it
    heightValue = str(height.next_sibling.next_sibling)

    # Getting the weight of the pokemon
    weight = soup.find("th", string="Weight")
    # Getting the weight value and then formatting it 
    weightValue = str(weight.next_sibling.next_sibling)
    
    # Printing the information that was retrieved 
    # Printing the pokedex number 
    print ("Pokedex Number: " + processing(pokedexNumber))

    # Printing the typing
    print ("Typing: ", end="")
    for element in typing:
        # Should probably put this into a function
        formattedType = processing(element)
        print(formattedType, end=" ")

    print()
    print ("Height: " + processing(heightValue))
    print ("Weight: " + processing(weightValue))
