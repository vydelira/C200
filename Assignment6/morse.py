code = {'A':'=.===',
'B':'===.=.=.=',
'C':'===.=.===.',
'D':'===.=.=',
'E':'=',
'F':'=.=.===.=',
'G':'===.===.=',
'H':'=.=.=.=',
'I':'=.=',
'J':'=.===.===.===',
'K':'===.=.===',
'L':'=.===.=.=',
'M':'===.===',
'N':'===.=',
'O':'===.===.===',
'P':'=.===.===.=',
'Q':'===.===.=.===',
'R':'=.===.=',
'S':'=.=.=',
'T':'===',
'U':'=.=.===',
'V':'=.=.=.===',
'W':'=.===.===',
'X':'===.=.=.===',
'Y':'===.=.===.===',
'Z':'===.===.=.='}

def letter_to_code(letter):
    return code[letter]

space_between_letters = "..." 
space_between_words = "......."

def word_to_code(word):
    encoded_word=""
    for i in range(0,len(word)-1):
       encoded_word += code[word[i]] + space_between_letters
    encoded_word += code[word[len(word)-1]]
    return encoded_word

def sentence_to_code(s):
    encoded_sentence=""
    s = s.split(" ")
    for i in range(0, len(s)-1):
        encoded_sentence += word_to_code(s[i]) + space_between_words
    encoded_sentence += code[s[len(s)-1]]
    return encoded_sentence


def code_to_letters(s):
    morse_code=""
    letters = s.split("...")
    for i in range(0, len(s)):
        morse_code += code[word[0][i]]
    return morse_code


def code_to_sentence(s):
    decode_sentence = ""
    sentences = (".......")
    for i in range(0, len(s)):
        decode_sentence += code_to_letters(sentences[i]) + " "
    return decode_sentence


d = {}
for k,v in code.items():
    d[v] = k

#Testing
def testing(s,c):
    if sentence_to_code(s) == c:
        print("S->C for {0} passed.".format(s))
    else:
        print("S->c for {0} failed.".format(s))
    if code_to_sentence(c) == s:
        print("C->S for {0} passed.".format(s))
    else:
        print("C->S for {0} failed.".format(s))

test_strings = ["MORSE CODE", "I NEED MONEY", "ORDER PIZZA"]
test_code = ['===.===...===.===.===...=.===.=...=.=.=...=.......===.=.===.=...===.===.===...===.=.=...=',
'=.=.......===.=...=...=...===.=.=.......===.===...===.===.===...===.=...=...===.=.===.===',
'===.===.===...=.===.=...===.=.=...=...=.===.=.......=.===.===.=...=.=...===.===.=.=...===.===.=.=...=.===']



f = open("c.txt", "r")


for s,c in zip(test_strings, test_code):
    testing(s,c)

#TO DO 5

#Read codes in \url{c.txt} and translate them and display them.

print(letter_to_code())
print(word_to_code())
print(sentence_to_code())
print(code_to_letters())
print(code_to_sentence())