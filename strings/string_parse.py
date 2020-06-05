gene = "01111011"

for i in range(0, 8, 2):
    y = gene[i] + gene[i+1]
    print(y)
