#Problem Set 0
#Name: Juan Rached Viso
#Time: 0:05

#Import numpy package for logarithm function
import numpy 

#Prompt user for x and y
x = float(input("Input base number: "))
y = float(input("Input power number: "))

#Compute and display x^y
print("\n", x, "to the power of ", y, "is: ", x**y)

#Compute and display log2(x) if x is greater than zero
if (x > 0) :
    print("\n The log base 2 of ", x, "is: ", numpy.log2(x))
else:
    print("\n Logarithm function only takes numbers greater than zero. Try again.")