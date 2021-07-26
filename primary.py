# author: layla
# date:7/23/2021

from random import randint

# --------------- # Section 1 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 1 -----'.center(25))
print('--- Part 1 ---'.center(25))

# Conditions & Conditionals

# 1 - Conditions
print('\n' + 'Task 1' + '\n')
# Part 1 is focused on getting input from the user and comparing that input in various ways.
#
# Instructions:
#   a. Prompt input in the form of a float from the user and save to four variables: a, b, c, and d.
#       --> a has been done for you already. Feel free to change the prompt if you wish.
#   b. Print the results of the following comparisons. Number 1 has been done for you.
#       1. a == b
#       2. a == b == c
#       3. a > b > c
#       4. a < b < c < d
#       5. a != b == c != d
#       6. a >= b >= c == d
#       7. a <= b > c <= d
#
# WRITE CODE BELOW #
a = float(input('a = '))
b = 4
c = 6
d = 10

print('a == b |', a == b)
print('a == b == c',a == b == c)
print('a > b > c', a > b > c)
print(' a < b < c < d',  a < b < c < d)
print('a != b == c != d',a != b == c != d)
print(' a >= b >= c == d',  a >= b >= c == d)
print('a <= b > c <= d', a <= b > c <= d)
# 2 - if Statements (ONLY USE if STATEMENTS)
print('\n' + 'Task 2' + '\n')
# Instructions:
#   a. Prompt input from the user in the form of a word, and save to a variable. Do this twice. It has been done
#       for the first word, you must do the second one yourself.
#
#   b. Write the following conditionals using ONLY if Statements:
#       1. Compare the words to see if they are the same. If so, print that they are the same.
#
#       2. Compare the words to see if they aren't the same. If so, print that they are not the same.
#
#       3. Compare the words to see if word1 is alphabetically lower (less than) than word2. If so, print that
#           the first word appears before the second word.
#
#       4. Compare the words to see if word1 is alphabetically higher (greater than) than word2. If so, print that
#           the first word appears after the second word.
#
# WRITE CODE BELOW #
word1 = input('enter a word: ')
word2 = 'mom'

if word1 == word2:
    print(word1, 'and', word2, 'are the same!')
elif word1:
    print(word1, 'and', word2, 'they are not the same')
elif word1:
    print(word1, 'and', word2, 'the first word appears before the second word')
else:
    print(word1, 'and', word2, 'the first word appears after the second word')


# 3 - if-elif-else Statements
print('\n' + 'Task 3' + '\n')
# Instructions:
#   a. Using the randint function, roll two six sided dice. One dice has been rolled for you already.
#
#   b. Write the following using if-elif-else Statements:
#       1. If both dice are the same value, print 'Doubles!' followed by the two numbers. However, if the numbers
#           are both ones, print 'Snake Eyes!' instead.
#
#       2. If both dice are even, print 'Evens!' followed by the two numbers.
#
#       3. If both dice are odd, print 'Odds!' followed by the two numbers.
#
#       4. If the sum of the values of the dice are greater than 6, print 'Win!'
#
#       5. Otherwise, print 'Lose!'
#
# WRITE CODE BELOW #
dice1 = randint(1, 6)
dice2 = randint(1, 6)
print(dice1)
print(dice2)

if dice1==dice2:
    print('Doubles!', dice1,'and', dice2)
elif dice1==dice2==1:
    print('Snake Eyes!')
if dice1%2==dice2%2==0:
    print('Evens!', dice1,'and', dice2)
else:
    print('Odds!', dice1, 'and', dice2)





