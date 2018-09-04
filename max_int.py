#Algorithm
#1. Receive a number from te user
#2. Check if the number is neative
#    2.1 if the number is negative
        # print the highest number from the user
#    2.2 if the number is positive
#        if the largest number is 0
#            store the users number as the largest
#        compare it to the previous number
#            if it is larger than the previous number
#                store it as the largest number
#            if it is smaller than the previous number
#                go back to step 1

max_int = 0
num_int = int(input("Input a number: "))    # Do not change this line
while num_int >= 0:
    num_int = int(input("Input a number: ")) 
    if max_int == 0:
        max_int = num_int
    else:
        if num_int > max_int:
            max_int = num_int

    
print("The maximum is", max_int)    # Do not change this line
    
