n = int(input("enter first number:"))
c = input("enter operator(+,-,*,/):")
m = int(input("enter second number:"))
if c=="+":
    print("addition:",n+m)
elif c=="-":
    print("subtraction:",n-m)
elif c=="*":
    print("multiplication:",n*m)
elif c=="/":
    print("division:",n/m)
else:
    print("invalid")