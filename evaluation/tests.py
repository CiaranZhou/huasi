from django.test import TestCase

# Create your tests here.
from itertools import permutations

result = {'C': 3, 'R': 5, 'I': 5, 'E': 4, 'S': 3, 'A': 2}
s = sorted(result, key=result.__getitem__, reverse=True)
if result[s[2]] == result[s[3]]:
    print('本次测试不准确')
else:
    if result[s[0]] == result[s[1]] == result[s[2]]:
        for i in permutations(s[:3]):
            print(i)
    elif result[s[0]] == result[s[1]]:
        for i in permutations(s[:2]):
            i = i + (s[2], )
            print(i)
    elif result[s[1]] == result[s[2]]:
        for i in permutations(s[:2]):
            i = (s[0], ) + i
            print(i)
