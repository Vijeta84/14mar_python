'''Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7 
Hint : first 7 numbers in the series
Expected output : 
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13'''

# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(13))

