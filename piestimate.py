# Estimates the value of pi using the Pythagorean theorem
import random
import math
def piestimate(num):
    count = 0
    for i in range(1, num+1):
        x = random.random()
        y = random.random()
        rad = math.sqrt(x ** 2 + y ** 2)
        if rad < 1:
            count+=1
    print(count*4/num)

inp = input("Enter number of iterations: ")
inp = int(inp)
piestimate(inp)
