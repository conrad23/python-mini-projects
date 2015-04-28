__author__ = 'conrad23'

# recursively determines the fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# prints out the fibonacci sequence up to the input index
def fibonacci_seq(n):
    sequence = ""
    if n == 0:
        sequence += "0"
    else:
        array = [0] * 100
        array[1] = 1
        for i in range(2, n+1):
            array[i] = array[i-1] + array[i-2]
        for i in range(0, n+1):
            sequence += (str(array[i]) + ", ")
    return sequence

print ("Which fibonacci number would you like to see?")
prompt = '> '
numStr = raw_input(prompt)
num = int(numStr)
print ("%r ---> %r") % (num, fibonacci(num))
print ("Fibonacci sequence to %r: %r") % (num, fibonacci_seq(num))
