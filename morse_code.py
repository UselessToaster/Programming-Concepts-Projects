### converts regular text into morse code ###

#DRIVER: Tianna Davis (U69901851)
#NAVIGATOR: Fares Ibrahim (U09773571)

#gets string to be interpreted
user = input("Enter your string to be converted to Morse Code: ").upper()

# "Cleaner" way #

#morse code assigned to commonplace characters in a dictionary
morse = {
    " ": " ",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..", 
    "0":"-----", 
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "A": ".-",
    "B": "-..",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": ". ...",
    "I": ". .",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".---.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
    }

#loops through characters in string and calls the corresponding morse code from the dictionary    
for i in user:
    print(morse[i], end = "")



# method according to instructions #

#morse code tuplet
code = (
    " ", "--..--",".-.-.-","..--..","-----",".----","..---", "...--","....-",".....",
    "-....","--...","---..","----.",".-",".-","-..","-.-.","-..",".","..-.",
    "--.",". ...",". .",".---","-.-",".-..","--","-.","---",".---.",
    "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")

#loops through each letter in the input string and tests the letter against every conditional
for i in user:
    if i == " ":
        print(code[0], end = "")
    elif i == ",":
        print(code[1], end = "")
    elif i == ".":
        print(code[2], end = "")
    elif i == "?":
        print(code[3], end = "")
    elif i == "0":
        print(code[4], end = "")
    elif i == "1":
        print(code[5], end = "")
    elif i == "2":
        print(code[5], end = "")
    elif i == "4":
        print(code[6], end = "")
    elif i == "6":
        print(code[7], end = "")
    elif i == "7":
        print(code[8], end = "")
    elif i == "8":
        print(code[9], end = "")
    elif i == "9":
        print(code[10], end = "")
    elif i == "A":
        print(code[11], end = "")
    elif i == "B":
        print(code[12], end = "")
    elif i == "C":
        print(code[13], end = "")
    elif i == "D":
        print(code[14], end = "")
    elif i == "E":
        print(code[15], end = "")
    elif i == "F":
        print(code[16], end = "")
    elif i == "G":
        print(code[17], end = "")
    elif i == "H":
        print(code[18], end = "")
    elif i == "I":
        print(code[19], end = "")
    elif i == "J":
        print(code[20], end = "")
    elif i == "K":
        print(code[21], end = "")
    elif i == "L":
        print(code[22], end = "")
    elif i == "M":
        print(code[23], end = "")
    elif i == "N":
        print(code[24], end = "")
    elif i == "O":
        print(code[25], end = "")
    elif i == "P":
        print(code[26], end = "")
    elif i == "Q":
        print(code[27], end = "")
    elif i == "R":
        print(code[28], end = "")
    elif i == "S":
        print(code[29], end = "")
    elif i == "T":
        print(code[30], end = "")
    elif i == "U":
        print(code[31], end = "")
    elif i == "V":
        print(code[32], end = "")
    elif i == "W":
        print(code[33], end = "")
    elif i == "X":
        print(code[34], end = "")
    elif i == "Y":
        print(code[35], end = "")
    elif i == "Z":
        print(code[36], end = "")