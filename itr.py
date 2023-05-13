# define a function to calculate income tax under the old regime
def calculate_income_tax_old(total_income):
  # assume total_income is a positive integer
  # assume the tax rates and slabs are as per the web page context
  # assume the age group is below 60 years
  # initialize the tax variable to zero
  tax = 0
  # apply the basic exemption limit of Rs. 2,50,000
  if total_income <= 250000:
    print(f"You don't have to pay tax")
    return tax
  else:
    total_income -= 250000
  # define a list of tax slabs and rates
  slabs = [250000,500000,float('inf')]
  rates = [0.05,0.2,0.3]
  # use a for loop to iterate over the slabs and rates
  for i in range(len(slabs)):
    # apply the tax rate for the current slab
    if total_income <= slabs[i]:
      tax += total_income * rates[i]
      break # exit the loop if the income is within the slab
    else:
      tax += slabs[i] * rates[i]
      total_income -= slabs[i]
  # apply the health and education cess of 4% on the tax amount
  cess = tax * 0.04
  print(f"Health & Education cess is ₹{cess}.")
  tax += cess
  
  # define a list of surcharge slabs and rates
  surcharge_slabs = [5000000 - (250000 + (250000 / .05) + (500000 / .2)), 10000000 - (250000 + (250000 / .05) + (500000 / .2) + (5000000 / .3)), float('inf')]
  surcharge_rates = [0.1, 0.15, 0]
  
  # use a for loop to iterate over the surcharge slabs and rates
  for i in range(len(surcharge_slabs)):
    # apply the surcharge rate for the current slab
    if total_income > surcharge_slabs[i]:
      tax += tax * surcharge_rates[i]
      break # exit the loop if the income is above the slab
  return tax

# define a function to calculate income tax under the new regime 
def calculate_income_tax_new(total_income): 
   # assume total_income is a positive integer 
   # assume the tax rates and slabs are as per the web page context 
   # assume the age group is below 60 years 
   # initialize the tax variable to zero 
   tax = 0 
   # apply the basic exemption limit of Rs.2,50,000 
   if total_income <=250000: 
     return tax 
   else: 
     total_income -=250000 
   # apply the tax rate of 5% for income up to Rs.5,00,000 
   if total_income <=250000: 
     tax +=total_income * .05 
     return tax 
   else: 
     tax +=250000 * .05 
     total_income -=250000 
   # apply the tax rate of 10% for income up to Rs.7,50,000 
   if total_income <=250000: 
     tax +=total_income * .1 
     return tax 
   else: 
     tax +=250000 * .1 
     total_income -=250000 
   # apply the tax rate of 15% for income up to Rs.10,00,000 
   if total_income <=250000: 
     tax +=total_income * .15 
     return tax 
   else: 
     tax +=250000 * .15 
     total_income -=250000 
   # apply the tax rate of 20% for income up to Rs.12,50,000 
   if total_income <=250000: 
     tax +=total_income * .2 
     return tax 
   else: 
     tax +=250000 * .2 
     total_income -=250000  
   # apply the tax rate of 25% for income up to Rs.15,00,000  
   if total_income <=250000:  
     tax +=total_income * .25  
     return tax  
   else:  
     tax +=250000 * .25  
     total_income -=250000  
   # apply the tax rate of 30% for income above Rs.15,00,000  
   tax +=total_income * .3  
   # apply the health and education cess of 4% on the tax amount  
   tax +=tax * .04  
   # apply the surcharge of 25% or reduced from earlier surcharge rate of 37% if applicable  
   if total_income > (50000000 - (250000 + (250000 / .05) + (250000 / .1) + (250000 / .15) + (250000 / .2) + (250000 / .25) + (35000000 / .3))):  
    #  # income above Rs.5 crore  
     surcharge_rate = min(.25,.37)  
     surcharge_amount = min(tax,surcharge_rate*tax)  
     return round(tax+surcharge_amount)  
   else:  
     return round(tax)  

# ask the user to select old or new regime as an option (1 or 2)
regime = input("Please select your preferred regime:\n1.Old\n2.New\n")
# validate the input and convert it to an integer
try:
    regime = int(regime)
except ValueError:
    print("Invalid input. Please enter either '1' or '2'.")
else:
    if regime not in [1,2]:
        print("Invalid input. Please enter either '1' or '2'.")
    else:
        # ask the user to enter their total income as an integer
        income = input("Please enter your total income as an integer:\n")
        # validate the input and convert it to an integer
        try:
            income = int(income)
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
        else:
            if income <0:
                print("Invalid input. Please enter a positive integer.")    
            else:
                # call the appropriate function based on the regime option and print the result
                if regime>=1:
                  total_income_tax_old = calculate_income_tax_old(income)
                  print(f"Your income tax under the old regime is ₹ {total_income_tax_old}.")
                  total_income_tax_new = calculate_income_tax_new(income)
                  print(f"Your income tax under the new regime is ₹ {total_income_tax_new}.")
                  tax_difference = total_income_tax_new-total_income_tax_old
                  if tax_difference>=0 :
                    print(f"You will save ₹",tax_difference,"under new regime")
                  else :
                    print(f"Your tax difference is ₹", tax_difference,". You won't save any tax in the new regime") 