import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
lis = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i) 
    lis.append(t)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

positive = []
negative = []
for number in lis:
    if 5526 >= number >= 0:
        positive.append(number)
    elif -273 <= number < 0:
        negative.append(number)

unnegative = 0
if len(negative) == 0 and len(positive) == 0:
    print(unnegative)
elif len(negative) == 0 and len(positive) > 0:
    print(min(positive))
elif len(negative) > 0 and len(positive) == 0:
    print(max(negative))
else:
    unnegative -= max(negative)
    if unnegative > min(positive):
        print(min(positive))
    elif unnegative < min(positive):
        print(max(negative))
    elif unnegative == min(positive):
        print(min(positive))