# Author: Rajendra L Hanagodi
# Date of creation:23/02/2021

import re
input_file = open("input.txt", "r")                                   # reading the input file
count = 0
input_search = input("Enter the Word to be search:\n")                # user input requried word
input_file2 = input_file.read()        # finding all the user input requried word from the input file
input_file1 = input_file2.split()
user_input_search_word = input_search + '.txt'
user_input_file = open(user_input_search_word, "w+")                              # counting the number of times input word is repeating
for i in range(len(input_file1)):
    word = re.match(input_search, input_file1[i], re.M | re.I)         # finding all the user input required word from the input file
    if word:
        count += 1
        user_input_file.write(input_file1[i-1]+' '+input_file1[i]+' '+input_file1[i+1]+'\n'+'\n')


user_input_file.write("Number of times word appered in file:  " + str(count))

