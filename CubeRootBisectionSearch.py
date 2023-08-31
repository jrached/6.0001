# Write your code here

n= 1

low = 0.0
high = n
epsilon = 0.01
guess = (high + low)/2

while abs(guess**3 - n) >= epsilon:
    
    if guess**3 > n:
        high = guess
    else:
        low = guess
    
    guess = (high + low)/2
    
if abs(guess - round(guess)) <= epsilon:
    print(round(guess))
else:
    print("error")
        
print(guess)
print(round(guess))