print('To find all the Prime numbers between any Two number')

lower = int(input('Enter Prime number between '))
upper = int(input('and '))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
