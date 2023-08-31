def part_c(starting_amount):
	#########################################################################
	number_of_months = 36
	cost_of_house = 750000
	down_payment_percentage = 0.25
	down_payment = down_payment_percentage*cost_of_house #computing down_payment
	
	#Basic variable declaration for bisecton search
	low = 0
	high = 1
	epsilon = 100
	r = (high + low)/2
	steps = 0
	
	#Define current savings
	current_savings = starting_amount*(1 + r/12)**number_of_months
	
	
	########################################################################################################
	## Determine the lowest return on investment needed to get the down payment for your dream home below ##
	########################################################################################################
	#If the starting amount is enough to pay the down payment, then the best rate of return is
	#zero. Else, use bisection search to find the rate of return
	
	if starting_amount >= down_payment:
	    r = 0
	else:
	    #Iterate until the difference between current savings 
	    #and the down_payment is not larger than the allowed error, epsilon.
	    while abs(current_savings - down_payment) > epsilon:
	        steps += 1
	        
	        #Establish upper and lower bounds if r is too high or too low.
	        if current_savings > down_payment: 
	            high = r
	        else:
	            low = r
	            
	        r = (high + low)/2 #Update r based on the new high and low bounds 
	        
	        current_savings = starting_amount*(1 + r/12)**number_of_months #Update current_savings
	        
	        #If the loop has not found an answer by after 200 iterations, chances are 
	        #there isn't one, so the loop breaks and assigns a value of None to r.
	        if steps > 200:
	            r = None
	            break
	
	##########################################################
	## Print out the best savings rate and steps taken here ##
	##########################################################
	
	print("\nlowest possible interest rate: " + str(r))
	print("\nSteps: ", steps)
	
	
	
	
	
	
	return r, steps