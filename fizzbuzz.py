def fizzbuzz(num):
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        else:
            print(i)
inp = input("Enter number of iterations: ")
inp = int(inp)
fizzbuzz(inp)
