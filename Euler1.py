#Find the sum of all the multiples of 3 or 5 below 1000

X = 0 #numeral sum
i = 0 #divisor up to indicated number

while i < 1000: #when i is less than printed number
    if i % 3 == 0 or i % 5 == 0: #if divisible by number and the remainder is zero
        X += i #add that number to the total sum
    i = i + 1 #if conditions are met or not, add one until conditions fufilled (while loop)

print X #print the numeral sum
