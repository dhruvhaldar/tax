def tax_calculation(fy_year, ay_year, income, regime):
  print(f"\n\nFY {fy_year} (AY {ay_year}) TAX CALCULATION")
  
  if regime==1:
    print(f"You have selected the old regime")
  if regime==2:
    total_income_tax_old = calculate_income_tax_old(income)
    print(f"Your income tax under the old regime is ₹ {total_income_tax_old}.")
    
    total_income_tax_new = calculate_income_tax_new(income)
    print(f"Your income tax under the new regime is ₹ {total_income_tax_new}.")
    tax_difference = total_income_tax_new-total_income_tax_old
    if tax_difference>=0 :
      print(f"You will save ₹{tax_difference} under new regime")
    else :
      print(f"Your tax difference is ₹{tax_difference}, you won't save any tax in the new regime.")
                    
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

def convert_to_lakh(income):
  lakh = income / 100000
  return lakh

def deductions_old(investment_80C,medical_80D,home_loan_24b):

  # initialize the total deductions
  total_deductions = 0

  # input the investment under section 80C
  #investment_80C = float(input("Enter your investment under section 80C: "))
  # 80C Investment set as function parameter

  # check if the investment exceeds the limit of 1.5 lakh
  if investment_80C > 150000: investment_80C = 150000
  total_deductions += investment_80C

  # input the medical insurance premium under section 80D
  #medical_80D = float(input("Enter your medical insurance premium under section 80D: "))
  # Medical insurance premium set as function parameter


  # check if the premium exceeds the limit of 25,000
  if medical_80D > 25000: medical_80D = 25000
  total_deductions += medical_80D

  # input the home loan interest under section 24(b)
  #home_loan_24b = float(input("Enter your home loan interest under section 24(b): "))
  # Home loan set as function parameter

  # check if the interest exceeds the limit of 2 lakh
  if home_loan_24b > 200000: home_loan_24b = 200000
  total_deductions += home_loan_24b

  # display input deductions
  print(f"80C Deduction : {investment_80C}")
  print(f"Medical 80D deduction : {medical_80D}")
  print(f"Home loan 24B deduction : {home_loan_24b}")


  # display the total deductions
  print(f"Your total deductions under the old regime are {total_deductions}.")


#################################################################################################################################

# ask the user to select old or new regime as an option (1 or 2)

#regime = input("Please select your preferred regime:\n1.Old\n2.New\n")
regime = 1 # Selected old regime

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
        
        #income = input("Please enter your total income as an integer:\n")
        income = 115000 # Sample income
        
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
                  
                  # tax_calculation(FY_Year,AY_Year)
                  tax_calculation("2022-23","2023-24",income,regime)
                  income_in_lakh=convert_to_lakh(income)
                  print(f"Annual income entered is ₹ {income_in_lakh} lakh.")
                  calculate_income_tax_old(income)
                  calculate_income_tax_new(income)

                ##########################################################################################################
                if regime==1:
                  print(f"\nDEDUCTION CALCULATION")
                  
                  #deductions_old(investment_80C,medical_80D,home_loan_24b)
                  deductions_old(60000,25000,0)