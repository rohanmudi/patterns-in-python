n = int(input())
spaces = n - 1
stars = 1

i = 0

for i in range(n):
    print(" " * spaces + "*" * stars)
    spaces -= 1
    stars += 2
