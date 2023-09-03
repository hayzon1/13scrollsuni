#A program to know the sum and product of some set of integers

#declare value "number"
number = input('Enter an integer:')

number_length = len(number)

digit_sum = 0

digit_product =1

for i in range(number_length):

    digit_sum +=int(number[i])

    digit_product *=int(number[i])
#Final command for the operation
print("\n',number,"digit sum is",digit_sum, "and digit product is",digit_product")