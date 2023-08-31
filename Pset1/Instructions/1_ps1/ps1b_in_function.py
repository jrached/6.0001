def part_b(salary, savings_percent, total_cost, raise_percentage):
	#########################################################################
	down_payment_percent = 0.15
	down_payment = down_payment_percent*total_cost
	amount_saved = 0.0
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	
	#Loop iterates until the amount of money in the savings account is greater than or equal
	#to that of the down_payment
	while amount_saved < down_payment:
	   
	    #Counter variable, each time the loop iterates a month elapses. 
	    months = months + 1
	    
	    #Increase savings by percentage of monthly salary + compounded interest from savings account
	    amount_saved = amount_saved + savings_percent*salary/12 + amount_saved*(0.05/12)
	   
	    #Every time months is a multiple of six (i.e every 6 months) increase 
	    #salary by raise percentage of previous salary
	    if months%6 == 0:
	       salary = salary + raise_percentage*salary
	          
	#######################################################
	## Print out the number of months it would take here ##
	#######################################################
	print("\nMonths: ", months)
	return months