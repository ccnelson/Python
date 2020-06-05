#list_move = [["#" for i in range(CN_play_area_x)]for i in range(CN_play_area_y)]
import random

options = ['00', '01', '10', '11']

list1 = [random.choice(options) for i in range(16)]

print(list1)

text = ""

for i in range(16):
    text = text + list1[i]

print(text)

