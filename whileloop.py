i = 1
while i <= 20:
    if (1 % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("odd numbers are: ",i)
    i += 1

import random
rand_num = random.randrange(1,51)
y = 1
while y != rand_num:
    y += 1
    print(rand_num)

tree_height = int(input("how tall is the tree: "))
spaces = tree_height- 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
    for m in range(spaces):
        print(" ",end=" ")
    for m in range(hashes):
        print("#",end=" ")
    print()
    spaces -= 1
    