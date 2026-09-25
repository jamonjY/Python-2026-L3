# Ex1:
radius = int(input("Enter circle radius: "))

area = 3.14 * (radius**2)

print(f"Circle area = {float(area)}" )

# Ex2:
n = int(input("Enter the temperature in celsius? "))

result = (1.8 * n) + 32

print(f"{n} (C) = {result} (F)")

# Ex3:
def isPrime(n: int):
    if n = 1:
        return true

    int i = 2
    while(i * i <= n):
        if (n % i == 0):
            return false
            i++       
    return true 


n = int(input("Enter a number? "))
if (isPrime(n) == true):
    print(f"{n} is a prime number") 
else:
    print(f"{n} is a NOT prime number")  

# Ex4:
def isPerfect(n):
    total = 0

    for i in range(1,n):
        if (n % i == 0):
            total += i

    return i = n 


n = int(input("Enter a number? "))
if (isPerfect()):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT a perfect number")

# Ex5:
color = ("Yellow", "White", "Purple", "Red", "Blue")

favcolor = input("What is your favourite color? ")

if favcolor in color:
    index = color.index(favcolor)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

# Ex6:
range1 = list(range(0,7))
range2 = list(range(1,11,3))
range3 = list(range(5,0,-1))
range4 = list(range(6,-3,-2))


print(range1)
print(range2)
print(range3)
print(range4)

# Ex7:
def remove_dollar_sign(s: string):
    return s.replace("$", "")

str = "very$do$llar$0$sign"
print(remove_dollar_sign(str))

# Ex8:
def extract_even(l):
    even_list = [] 
    for i in l:
        if (i % 2 == 0):
            even_list.append(i)

    return even_list

l = [1,4,5,-1,10]
print(extract_even(l))

# Ex9: 
def factorial(n: int):
    if n < 0:
        print("Invalid input! ")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

n = 5 
print(factorial(n))

# Ex10:
import math

def get_divisors(n: int) -> list[int]:
    divisors = []
    
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
                
    return divisors


n = 100
result = get_divisors(n)
print(f"Divisors of {n}: {result}")

# Ex11:
import math

def distance(point1, point2):
    return math.sqrt(((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))

point1 = [1, 0]
point2 = [0, 1]
print(distance(point1, point2))

# Ex12:
def thePattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                print("*", end ="")
            else:
                print(" ", end="")
        print()    



m = int(input("Please enter value for m: "))
n = int(input("Please enter value for n: "))
thePattern(m, n)

