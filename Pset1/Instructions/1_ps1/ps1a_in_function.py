def part_a(salary, savings_percent, total_cost):
	#########################################################################
	monthly_salary = salary/12
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
	    
	    #Counter variable, each time the loop iterates a month elapses
	    months = months + 1
	    
	    #Increase savings by percentage of monthly salary + compounded interest from savings account
	    amount_saved = amount_saved + savings_percent*monthly_salary + amount_saved*(0.05/12)
	    
	
	#######################################################
	## Print out the number of months it would take here ##
	#######################################################
	print("\nMonths: ", months)
	return months