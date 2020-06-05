
from dataclasses import dataclass

listx = [["1", "2", "3", "4"],["2", "3", "2", "1"],
         ["3", "4", "4", "3"],["3", "4", "3", "2"],
         ["3", "4", "5", "2"]]

g_list = []

@dataclass
class Gene:
    chromo: str
    dist: int
    score: int
    pos: int

for i in range(5):
    g_list.append(Gene(listx[i], 0, 0, i))

for j in g_list:
    print(j)

g_list[0].chromo = 'hey'

print(g_list[0].chromo)
