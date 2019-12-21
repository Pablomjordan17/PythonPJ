
def readint(x,a,b):
    y=list(range(a,b,1))  

    for i in range(0,len(y)):
         r=y[i]
         if r==x: 
             a=1;
             break
         else:
             a=0;
    return a         

try:
    x=int(input("Ingrese el numero a buscar: "))
    a=int(input("Ingrese el limite inferior: "))
    b=int(input("Ingrese el limite superior: "))
    f=readint(x,a,b)
    if f==1:
        print("the value is: ",x)
    else:
        print("the value is not within permitted range ")
except ValueError:
    print("wrong input ")
    
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
