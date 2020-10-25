print('To find the Area and Perimeter of the triangle')

a1 = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))


# calculate the semi-perimeter
s = (a1 + b + c) / 2
p = a1+b+c

# calculate the area and perimeter
area = (s*(s-a1)*(s-b)*(s-c)) ** 0.5
print('The perimeter of the triangle is', p)
print('The area of the triangle is %0.2f' %area)
