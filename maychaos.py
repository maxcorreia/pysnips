def maychaos(r, x0, num):
    for i in range(num):
        print(x0)
        x0 = r * x0 * (1 - x0)

inp1 = float(input("Enter r value: "))
inp2 = float(input("Enter x0 value: "))
inp3 = int(input("Enter number of iterations: "))
maychaos(inp1, inp2, inp3)
