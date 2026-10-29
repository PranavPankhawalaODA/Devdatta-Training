from itertools import groupby

input_string = input()
for key, group in groupby(input_string):
    print((len(list(group)), int(key)), end=' ')