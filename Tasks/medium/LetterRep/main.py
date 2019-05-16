import string
import random as rn

alphabet = [i for i in string.ascii_lowercase]
cypherAlph = ([i for i in string.ascii_lowercase])
rn.shuffle(cypherAlph)

with open('plaintext.txt', 'r') as f:
    plaintext = f.read()

cyphertext = ''

for letter in plaintext:
    if letter in string.ascii_letters:
        for index, i in enumerate(alphabet):
            if letter == i:
                cyphertext += cypherAlph[index]
                break
            elif letter == i.upper():
                cyphertext += (cypherAlph[index].upper())
                break
    else:
        cyphertext += letter

with open('cyphertext.txt','w') as f:
    f.write(cyphertext)
