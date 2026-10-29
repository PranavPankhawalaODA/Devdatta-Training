# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

input_string, size = input().split()
size = int(size)

sorted_string = sorted(input_string)

for i in range(1, size + 1):
    for el in combinations(sorted_string, i):
        print(''.join(el))
