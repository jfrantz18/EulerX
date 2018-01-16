X = 2520 #set X initial value at 2520 to conserve time
i = 2 #set divisor (i) initial value at 2 because all numbers are divisible by 1

while i <= 20: #when i is less than or equal to 20
    if X % i != 0: #if X is divided by i (initial value 2) and the remainder is not equal to zero...
        X = X + 1 #then, add 1 to X, repeat process, and...
        i = 2 #divisor (i) will remain or be reset at 2
    elif X % i == 0: #if X is divided by i (initial value 2) and the remainder IS equal to zero...
        i = i + 1 #add 1 to i and repreat process until contraints are met

print X
