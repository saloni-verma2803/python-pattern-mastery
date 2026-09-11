#que 46 : pascal's triengle 
#-------------------------------------------------------------------
n=int(input("enter no. :"))
for i in range(n):
  for j in range(n-i):
    print(" ",end="")
  num=1
  for k in range(i+1):
    print(num,end=" ")
    num=num*(i-k)//(k+1)
  print()