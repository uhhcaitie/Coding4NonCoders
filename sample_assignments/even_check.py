#want all the numbers from 0 to user input
#if even number and below half print my name, otherwise if even print the number
#if odd number is between half and three quarters of range, print not my name, otherwise print nothing
new_range = input("Hey man, enter a number: ")
new_range = int(new_range)
for x in range(0,new_range):
    if x%2 == 0:
        if x <= new_range/2:
            print ("My Name")
        else:
            print(x)
    elif x >= new_range/2 and x <= new_range/2 + new_range/4:
        print ("Not My Name")