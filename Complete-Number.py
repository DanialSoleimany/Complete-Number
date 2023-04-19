# Complete Number
x = int(input("Enter a number:\n"))
sum = 0

for i in range(1, x):
    if(x%i == 0):
        sum += i

if(x == sum):
    print("Complete Number")
else:
    print("Not a Complete Number")