import sys

def fibonacci(n):
    if n < 0:
        return False
        
    a,b = 0,1
    while a < n:
        a,b = b,a+b
    
    return a == n

if __name__ == '__main__':
    number = int(sys.argv[1])
    
    if fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} NÃO pertence à sequência de Fibonacci.")



