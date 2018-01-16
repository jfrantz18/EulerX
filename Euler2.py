#Prompt: considering the terms in the Fibonacci sequence whose values do not exceed four million
#find the sum of the even-valued terms

first_number = 1 #first term
second_number = 2 #second term
i = 0 #base sum going to be added to by X if constraints are met
X = 0

#Fibonacci Sequence = (n) + (n - 1)

while X <= 4000000: #while loop to set limits on program
    X = second_number
    if X % 2 == 0: #if the remainder of X divided by 2 is equal to zero
        i += X # i, which is initiailly equal to zero, is added to by X every time the constraints are made
    X = first_number + second_number #executing the Fibonacci Sequence
    first_number = second_number #replacing the first term with the second in order to continue the Fibonacci Sequence
    second_number = X #term_B is equal to X (the 1st term added to the second term AKA term_A + term_B)

print i
