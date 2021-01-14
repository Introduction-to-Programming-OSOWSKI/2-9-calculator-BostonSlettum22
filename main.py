def calculate(z,x,y):
    if z == "add":
        return x + y
    elif z == "subtract":
        return x - y
    elif z == "multiply":
        return x * y
    elif z == "divide":
        return x / y
    else:
        return 0
        

print(calculate("divide", 20, 5))
