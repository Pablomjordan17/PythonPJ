def badFun(n):
    return 1/n
try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("The End.")
    
