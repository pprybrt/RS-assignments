# You’re given a list of tuples, where each tuple contains coordinates (x, y). Write a program to print all coordinates where both x and y are even numbers.
# EXAMPLE: coordinates: [(2, 4), (1, 3), (6, 8), (7, 2), (0, 0)]; 
# OUTPUT: [(2, 4), (6, 8), (0, 0)]


coordinates=[(2, 4), (1, 3), (6, 8), (7, 2), (0, 0)]
for x,y in coordinates:
    if x%2==0 and y%2==0:
        print((x,y))