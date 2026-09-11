#   fibonacci no. pyramid
n=int(input("enter no. :"))
n1=0
n2=1
new=0
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(n1,end=" ")
        new = n1+n2
        n1 = n2
        n2 = new
    print()
