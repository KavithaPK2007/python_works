a=int(input("enter the first number :"))
b= int(input("enter the second number :"))
c=input("enter the operation(+,-,*,/)")
if c== "+":
    s=a+b
    print(a,"+",b,"=",s)
elif c== "-":
    s=a-b
    print(a,"-",b,"=",s)
elif c== "*":
    s=a*b
    print(a,"*",b,"=",s)
elif c=="/":
    s=a/b
    print(a,"/",b,"=",s)
else:
    print("wrong operator !")
