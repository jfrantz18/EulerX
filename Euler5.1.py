X = 2520
i = 2

while i <= 20:
    if X % i != 0:
        X = X + 20 #adding by multiples of 20 in order to cut program time substantially
        i = 2
    elif X % i == 0:
        i = i + 1

print X
