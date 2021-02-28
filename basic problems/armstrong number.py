num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")  # e.g. 153
else:
    print(num, "is not an Armstrong number")
