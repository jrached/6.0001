x = 3 
low = 0.0
high = x
epsilon = 0.01
guess = (high + low)/2
i = 0

while abs(guess**2 - x) >= epsilon:
    i += 1
    
    if guess**2 > x:
        high = guess
    else:
        low = guess
        
    guess = (high + low)/2
    
print("Number of guesses: " + str(i))
print("Square root of " + str(x) +" is: " + str(guess))
print(guess**2 - x)
