def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

def sum_of_digits(n):
    """Recursivley calculates the sum of the digits in a positive integer"""
    #Base case. Checks if n is a single digit. This provides a stopping point  
    if n<10:
        result=n
    #Add the last digit to the sum of digits from the rest of the number recursivley 
    else:
        result=n%10+sum_of_digits(n//10)
    return result

def count_occurrences(data_list, target):
    """Counts how many times the target value appears in the lsit using recursion."""
    #Base case, stops the recursion when list is empty 
    if len(data_list)==0:
        result=0
    else:
        #Check if the first item in the list and see if it is exactly equal to the target 
        if data_list[0]==target:
            #Add 1 for the current matching element and recursivley count occurances in the remaining list 
            # data_list[1:] means give a new list with all items except the first one 
            result=1+count_occurrences(data_list[1:],target)
        else: 
            #If first item is not a match, skip it and check rest of the itmes in the list  
            result=count_occurrences(data_list[1:],target)
    return result 

def factorial_iterative(n):
    """This function calculates the factorial of a postive integer n using a loop"""
    #Factorials count how many ways things can be arranged or ordered 
    #example: 3! means 3x2x1=6
    #Set result to 1 so it won't affect the prodcuts when multiplying numbers in the loop 
    result=1
    #counts from 1 and ends at n, adds 1 so range actually stops at n 
    #Loop each number from 1 to n to multiply it into the result 
    for i in range(1,n+1):
        #same as result=result*i
        #multiply current number 1 and udate result 
        result *=i
    return result

def fibonacci_iterative(n):
    """Calcualte the nth Fibonacci number using a loop iteration."""
    #Fibonacci sequence is a series of numbers where each number is the sum of the two before it. 
    #Base case, the answers for 1 and 2 are known immediately
    if n==1 or n==2:
        result=n
    else: 
        #Start with the first two fibonacci numbers as a base for calcualtions
        a=1
        b=2 
        #Loop starts at 3 and goes up to n 
        for _ in range(3,n+1):
            #Calcualte the next Fibonacci number by adding the previous two numbers stored in a and b 
            result=a+b
            #Move a to represent the previous Fibonacci number for next loop iteration  
            a=b
            #b now represents the current Fibonacci number to use in the next 
            b=result
    return result 




#Test code 
print(sum_of_digits(4232002)) #using recursion 
print(sum_of_digits_iterative(4232002)) #using iterative 

my_list=[0,4,2,3,2,0,0,2]
target=0
print(count_occurrences(my_list,target))

print(factorial_iterative(4))

print(fibonacci_iterative(6))

