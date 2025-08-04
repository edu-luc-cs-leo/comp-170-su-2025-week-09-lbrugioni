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
    #Base case. If n is a single digit then return it immediately  
    if n<10:
        result=n
    #Add the last digit to the sum of digits from the rest of the number recursivley 
    else:
        result=n%10+sum_of_digits(n//10)
    return result

def count_occurrences(data_list, target):
    """Counts how many times the target value appears in the list using recursion."""
    #Check if list is empty 
    if len(data_list)==0:
        result=0
    else:
        #Check if the first item in the list is equal to the target  
        if data_list[0]==target:
            #Add 1 for the current matching element and recursivley count occurances in the remaining list 
            result=1+count_occurrences(data_list[1:],target)
        else: 
            #If first item is not a match, skip it and check rest of the itmes in the list  
            result=count_occurrences(data_list[1:],target)
    return result 

def factorial_iterative(n):
    """This function calculates the factorial of a postive integer n using a loop"""
    #Set result to 1 so it won't affect the products when multiplying numbers in the loop 
    result=1
    #Loop through all numbers from 1 to n to multiply them together 
    for i in range(1,n+1):
        #update result by multiplying it by i 
        result *=i
    return result

def fibonacci_iterative(n):
    """Calcualte the nth Fibonacci number using a loop iteration."""
    #Check if n is 1 or 2 because the first 2 fibonacci numbers are 1 and 2 so we return them immediately
    if n==1 or n==2:
        result=n
    else: 
        #Starting values: first two numbers in the Fibonacci sequence 
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

