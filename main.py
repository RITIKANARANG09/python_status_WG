# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]
max_len=0
for player in players:
    if len(player["numbers"].intersection(lottery_numbers))>max_len:
         max_len=len(player["numbers"].intersection(lottery_numbers))
print(100**max_len)
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
