#A program to read in 20 numbers and print each number once it is read but won't print a duplicate number

#create an empty list for numbers
numbers =[]

#set Loop for number of times to be iterated
for i in range (1,21)

num = int(input("enter a number:"))

#initiate if command( To give a condition of if numbers is not duplicated add to the list of numbers to be printed 
if num not in numbers:

#initiate else command to print number if it passes the previous command 
else:
    print(num)

#if number not in list of previous numbers print it
    numbers.append(num)
    print(num)
