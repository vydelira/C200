#Listing 1: NLP

# Verb Endings
ar = ["o", "as", "a", "amos", "ais", "an"]
er = ["o", "es", "e", "emos", "eis", "en"]
ir = ["o", "es", "e", "imos", "is", "en"]

#Dictionary that allows easy access to verb endings
endings = {"ar": ar, "er": er, "ir": ir}

#Pairs of verbs (English, Spanish)
word = [["to buy", "comprar"], ["to speak", "hablar"], ["to learn", "aprender"], ["to receive", "recibir"]]

#A function that takes the english verb and return the spanish verb if available

def getVerb(v):
    for i in range(0, len(word)):
       if v == word[i][0]:
           return word[i][1]
    return []


def getEnding(v):
    return v[-2:]

def conjugate(v):
    if getEnding(v) == ar:
        return word[i][1] + endings["ar"]
    elif getEnding(v) == er:
        return word[i][1] + endings["er"]
    else:
        if getEnding(v) == ir:
            return word[i][1] + endings["er"]


print(getVerb("to buy"))
print(getVerb("to see"))
print(getEnding("comprar"))
print(getEnding("aprender"))
print()
print(conjugate("to buy"))
print(conjugate("to learn"))
print(conjugate("to see"))