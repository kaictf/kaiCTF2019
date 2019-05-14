import os
import pandas as pd


all_possible_passwords_raw = open('passwords').read()[:-1].split()


all_passwords = pd.DataFrame(all_possible_passwords_raw)


easy_passwords = all_passwords[all_passwords[0].map(lambda x:len(x)).isin([5])]

medium_passwords = all_passwords[all_passwords[0].map(lambda x:len(x)).isin([6])]

hard_passwords = all_passwords[all_passwords[0].map(lambda x:len(x)).isin([8])]


# create easy password list
with open('easy.txt', 'w') as file:
    count = 0
    for index, row in easy_passwords.iterrows():
        password = row[0]



        print(password)

        file.write(password+'\n')
        count +=1

        if count % 7 ==0:
            file.write('\n')


# create medium_passwords password list
with open('medium.txt', 'w') as file:
    count = 0
    for index, row in medium_passwords.iterrows():
        password = row[0]

        file.write(password+'\n')

        count += 1

        if count % 8 ==0:
            file.write('\n')


# create hard password list
with open('hard.txt', 'w') as file:
    count = 0
    for index, row in hard_passwords.iterrows():
        password = row[0]

        file.write(password+'\n')
        count += 1

        if count % 12 ==0:
            file.write('\n')
