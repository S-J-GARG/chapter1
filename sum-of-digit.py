print('Enter the three digit number\n')
x=input()
a=0
m=int(x,10)
j= m%10
i= m/100
k=int(float(i))
c= (m/10)%10
l=int(float(j+k+c))
print('sum of ',x,' digit is:',l)
import math
print('Now Enter any number')
a1=int(input())
while a1!=0:
    a=a+a1%10
    a1=int(float(a1/10)) #! Here 🙂 if we don't convert a1 into integer value it will cause error
print('The sum of its digit =',a)