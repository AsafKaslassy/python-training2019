print('enter a number you want to check whether it is a prime... ')
num = int(input())

x = int(num/2)

while(x>=2):
   if num%x == 0:
       print(num, 'divides by', x)
       break
   x = x - 1
else:
   print(num,'is a prime number') 