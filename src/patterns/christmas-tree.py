def tree_part(spaces, stars):
    for i in range(3):
        print(" " * spaces + "*" * stars)
        spaces -= 1
        stars += 2

def tree_stem(space, width, length):
    for i in range(length):
        print(" " * space + "*" * width)

n = int(input())

space = n + 1
stars = 1
for i in range(n):
    tree_part(space, stars)
    space -= 1
    stars += 2

space += 1
stars -= 2
tree_stem(space, stars, n)


