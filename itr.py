#import sys
#sys.stdout = open('output.txt', 'w')

def tax_calculation(fy_year, ay_year, regime):
  print(f"FY {fy_year} (AY {ay_year}) TAX CALCULATION")
  print(f"\n1. Income from salary")
  print(f"\n1.1 Input")
  if regime==1:
    print(f"You have selected the old regime")
  if regime==2:
    print(f"You have selected the new regime")  
                    
# define a function to calculate income_from_salary tax under the old regime
def calculate_income_from_salary_tax_old(total_income_from_salary):
  """
  This function is for calculating income tax on total income earned from salary in the old tax regime in India. The tax rates and slabs are assumed as per the web page context. The age group is assumed to be below 60 years.
  
  The function follows a progressive tax system where the tax rates increase with increasing income. The tax slabs and rates are defined in two lists, slabs and rates respectively. The slabs list contains the upper limit of each tax slab, while the rates list contains the tax rate for each slab.
  
  The basic exemption limit of Rs. 2,50,000 is applied first. If the total income from salary is less than or equal to Rs. 2,50,000, then no tax is applicable, and the function returns zero tax. Otherwise, the total income from salary is reduced by Rs. 2,50,000, and the remaining income is taxed using the tax slabs and rates.
  
  A for loop is used to iterate over the tax slabs and rates. If the remaining income falls within the current tax slab, then the tax is calculated using the corresponding tax rate. If the remaining income is more than the current tax slab, then the tax is calculated using the current tax slab and rate, and the remaining income is reduced by the current tax slab. This process continues until the remaining income becomes zero.
  
  After calculating the tax on income from salary, a health and education cess of 4% is applied on the tax amount. The final tax amount is calculated by adding the cess to the tax amount.
  
  The code also includes a provision for surcharge based on the total income from salary. The surcharge slabs and rates are defined in two lists, surcharge_slabs and surcharge_rates respectively. A for loop is used to iterate over the surcharge slabs and rates. 
  
  If the total income from salary is above the current surcharge slab, then the surcharge rate for the current slab is applied on the tax amount. This process continues until the total income from salary becomes less than or equal to the current surcharge slab or the highest surcharge slab is reached.

  Args:
      total_income_from_salary (int): Total annual Income from Salary

  Returns:
      tax (float): Total Income tax from old regime
  
  Example:
      For an income of 1500000, the tax calculation in the code will be as follows:
  
      1. The basic exemption limit of Rs. 2,50,000 will be applied, so the taxable income will be 1250000 (1500000 - 250000).
      2. The first slab of 250000 will be taxed at a rate of 5%, which amounts to 12500 (250000 * 0.05).
      3. The second slab of 250000 will be taxed at a rate of 20%, which amounts to 50000 (250000 * 0.2).
      4. The remaining income of 750000 will be taxed at a rate of 30%, which amounts to 225000 (750000 * 0.3).
      5. The total tax liability before cess and surcharge will be the sum of the tax amounts for each slab, which is 287500 (12500 + 50000 + 225000).
      6. A health and education cess of 4% will be applied on the tax amount, which amounts to 11500 (287500 * 0.04).
      7. Since the income is above 500000, a surcharge of 10% will be applied on the tax amount, which amounts to 28750 (287500 * 0.1).
      8. The total tax liability after cess and surcharge will be the sum of the tax amount and the surcharge, which is 317750 (287500 + 28750).
      9. Therefore, the tax rate for an income of 1500000 according to the code is 21.18% (317750 / 1500000 * 100).
  """
  # assume total_income_from_salary is a positive integer
  # assume the tax rates and slabs are as per the web page context
  # assume the age group is below 60 years
  # initialize the tax variable to zero
  tax = 0
  
  # Negative income
  if total_income_from_salary < 0:
      raise AssertionError("Total income from salary cannot be negative.")
  # apply the basic exemption limit of Rs. 2,50,000
  if total_income_from_salary <= 250000:
    print(f"You don't have to pay tax")
    return tax
  else:
    total_income_from_salary -= 250000
  # define a list of tax slabs and rates
  slabs = [250000,500000,float('inf')]
  rates = [0.05,0.2,0.3]
  # use a for loop to iterate over the slabs and rates
  for i in range(len(slabs)):
    # apply the tax rate for the current slab
    if total_income_from_salary <= slabs[i]:
      tax += total_income_from_salary * rates[i]
      break # exit the loop if the income_from_salary is within the slab
    else:
      tax += slabs[i] * rates[i]
      total_income_from_salary -= slabs[i]
  # apply the health and education cess of 4% on the tax amount
  cess = tax * 0.04
  print(f"Health & Education cess (Old regime) is Rs {cess}.")
  tax += cess
  
  # define a list of surcharge slabs and rates
  surcharge_slabs = [5000000 - (250000 + (250000 / .05) + (500000 / .2)), 10000000 - (250000 + (250000 / .05) + (500000 / .2) + (5000000 / .3)), float('inf')]
  surcharge_rates = [0.1, 0.15, 0]
  # use a for loop to iterate over the surcharge slabs and rates
  for i in range(len(surcharge_slabs)):
    # apply the surcharge rate for the current slab
    if total_income_from_salary > surcharge_slabs[i]:
      tax += tax * surcharge_rates[i]
      break # exit the loop if the income_from_salary is above the slab
  
  return tax

def calculate_income_from_salary_tax_new(total_income_from_salary):

  # assume total_income_from_salary is a positive integer
  # assume the tax rates and slabs are as per the web page context
  # assume the age group is below 60 years
  # initialize the tax variable to zero
  tax = 0

  # define a list of tax slabs and rates
  slabs = [250000,500000,750000,1000000,1250000,1500000,float('inf')] 
  rates = [0.05,0.1,0.15,0.2,0.25,0.3]

  # use a for loop to iterate over the slabs and rates
  for i in range(len(slabs)): # apply the tax rate for the current slab 
    if total_income_from_salary <= slabs[i]: 
      tax += total_income_from_salary * rates[i] 
      break 
    # exit the loop if the income_from_salary is within the slab else: 
    # tax += slabs[i] * rates[i] total_income_from_salary -= slabs[i]

  # apply the health and education cess of 4% on the tax amount
  cess = tax * 0.04 
  print(f"Health & Education cess (New regime) is Rs {cess}.") 
  tax += cess

  # define a list of surcharge slabs and rates
  surcharge_slabs = [5000000 - (250000 + (250000 / .05) + (250000 / .1) + (250000 / .15) + (250000 / .2) + (250000 / .25)), float('inf')] 
  surcharge_rates = [0.1, 0.25] # reduced from 37% to 25% under the new regime

  # use a for loop to iterate over the surcharge slabs and rates
  for i in range(len(surcharge_slabs)): # apply the surcharge rate for the current slab 
    if total_income_from_salary > surcharge_slabs[i]: 
      tax += tax * surcharge_rates[i] 
      break # exit the loop if the income_from_salary is above the slab return tax  
  return tax

def convert_to_lakh(income_from_salary):
  lakh = income_from_salary / 100000
  return lakh

def difference(tax_new,tax_old):
  if tax_new-tax_old>=0 :
    print(f"You will save Rs {tax_new-tax_old} under new regime")
  else :
    print(f"Your tax difference is Rs {tax_new-tax_old}, you won't save any tax in the new regime.")


def calculate_80_deduction(section_80C_ELSS, section_80C_PPF, section_80C_Life, section_80CCC, section_80CCD1, section_80CCD1b, section_80D, section_80E, section_80G, section_80TTA_Bank1, section_80TTA_Bank2, section_80TTA_Bank3, section_80TTA_Bank4, section_80TTA_Bank5, section_80TTB, section_24b): 
  
  # Initialize the deduction amount 
  total_deductions = 0
  
  # Calculate the total amount of section 80C, 80CCC and 80CCD(1)
  total_80C = section_80C_ELSS + section_80C_PPF + section_80C_Life + section_80CCC + section_80CCD1

  # Check if the total amount exceeds the limit of Rs 1.5 lakh
  if total_80C > 150000:
    # Set the deduction amount to Rs 1.5 lakh
    section_80CCE = 150000
  else:
    # Set the deduction amount to the total amount
    section_80CCE = total_80C
  
  # Add all interests from 5 Bank Accounts
  section_80TTA = section_80TTA_Bank1 + section_80TTA_Bank2 + section_80TTA_Bank3 + section_80TTA_Bank4 + section_80TTA_Bank5
    
  # Add the deduction amount for each section
  total_deductions += section_80CCE # Deduction for investments or expenditures under Section 80C, 80CCC, 80CCD(1) and 80CCD(1b)
  total_deductions += section_80D # Deduction for medical insurance premium
  total_deductions += section_80E # Deduction for interest on education loan
  total_deductions += section_80G # Deduction for donations to specified funds or institutions
  total_deductions += section_80TTA # Deduction for interest income from savings account (for non-senior citizens)
  total_deductions += section_80TTB # Deduction for interest income from deposits (for senior citizens)
  
  # check if the interest exceeds the limit of 2 lakh
  if section_24b > 200000: section_24b = 200000
  total_deductions += section_24b # Deduction for interest on home loan

  # display input deductions
  print(f"\n2.1 Input")
  print(f"80CCE Deduction : Rs {section_80CCE}")
  print(f"80D Deduction Medical : Rs {section_80D}")
  print(f"80E Deduction for interest on education loan : Rs {section_80E}")
  print(f"80G Deduction for donations to specified funds or institutions : Rs {section_80G}")
  print(f"80TTA Deduction for interest income from savings account (for non-senior citizens) : Rs {section_80TTA}")
  print(f"80TTB Deduction for interest income from deposits (for senior citizens) : Rs {section_80TTB}")
  print(f"24B Home loan deduction : Rs {section_24b}")


  # display the total deductions
  print(f"\n2.2 Output")
  print(f"Your total deductions under the old regime Section 80 is Rs {total_deductions}")

  # Return the deduction amount
  return total_deductions

##############################################################################

def income_from_hp(type,home_loan_interest):
  
  print(f"\n3. Income from house property")
  # input the type of house property
  #type = input("Enter the type of house property: self-occupied, let out or deemed let out: ")

  # initialize the income from house property variable to zero
  income_from_hp = 0

  # if the type is self-occupied
  if type == "self-occupied":
    # input the home loan interest
    #home_loan_interest = float(input("Enter the home loan interest paid during the year: ")) 
    
    # check if the interest exceeds the limit of 2 lakh 
    if home_loan_interest > 200000: home_loan_interest = 200000
    # deduct the interest from the income from house property
    income_from_hp -= home_loan_interest

  # if the type is let out or deemed let out
  elif type in ["let out", "deemed let out"]:
    # input the gross annual value 
    #gross_annual_value = float(input("Enter the gross annual value of the property: ")) 
    gross_annual_value = 100000.0
    # input the property tax 
    #property_tax = float(input("Enter the property tax paid during the year: ")) 
    property_tax = 40000.0
    # deduct the property tax from the gross annual value 
    net_annual_value = gross_annual_value - property_tax 
    # deduct 30% of net annual value as standard deduction 
    standard_deduction = net_annual_value * 0.3 
    net_annual_value -= standard_deduction 
    # input the home loan interest 
    #home_loan_interest = float(input("Enter the home loan interest paid during the year: ")) 
    # deduct the interest from the net annual value 
    net_annual_value -= home_loan_interest 
    # assign the net annual value to the income from house property 
    income_from_hp = net_annual_value 
    
  else: 
    # print an error message for invalid input 
    print("Invalid input. Please enter a valid type of house property.")

  return income_from_hp

#################################################################################################################################
# MAIN #

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
        # ask the user to enter their total income_from_salary as an integer
        
        #income_from_salary = input("Please enter your total income_from_salary as an integer:\n")
        income_from_salary = 1150000 # Input annual income_from_salary
        
        # validate the input and convert it to an integer
        try:
            income_from_salary = int(income_from_salary)
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
        else:
            if income_from_salary <0:
                print("Invalid input. Please enter a positive integer.")    
            else:
                # call the appropriate function based on the regime option and print the result
                if regime>=1:
                  fy_year = "2022-23"
                  ay_year = "2023-24"
                  # tax_calculation(FY_Year,AY_Year)
                  tax_calculation(fy_year,ay_year,regime)
                  print(f"Annual income entered is Rs {convert_to_lakh(income_from_salary)} lakh\n")
                  
                  
                  print(f"1.2 Output")
                  new_income_tax_salary = calculate_income_from_salary_tax_new(income_from_salary)
                  old_income_tax_salary = calculate_income_from_salary_tax_old(income_from_salary)
                  
                  print(f"\nYou have to pay Rs {old_income_tax_salary} under old tax regime")
                  print(f"You have to pay Rs {new_income_tax_salary} under new tax regime")
                  difference(new_income_tax_salary,old_income_tax_salary)

                ##########################################################################################################
                if regime==1:
                  print(f"\n\n2. DEDUCTION CALCULATION")
                  section_80C_ELSS = 100000 # ELSS Funds
                  section_80C_PPF = 0 # PPF
                  section_80C_Life = 0 # Life Insurance premium 
                  section_80CCC = 20000 # Pension plan 
                  section_80CCD1 = 50000 # NPS contribution by employee or self-employed 
                  section_80CCD1b = 50000 # Additional NPS contribution 
                  section_80D = 25000 # Medical insurance premium for self and parents 
                  section_80E = 40000 # Interest on education loan 
                  section_80G = 10000 # Donation to a charitable trust 
                  section_80TTA_Bank1 = 1000 # Interest income from savings bank account 1
                  section_80TTA_Bank2 = 1000 # Interest income from savings bank account 2
                  section_80TTA_Bank3 = 1000 # Interest income from savings bank account 3
                  section_80TTA_Bank4 = 2000 # Interest income from savings bank account 4
                  section_80TTA_Bank5 = 0 # Interest income from savings bank account 5
                  section_80TTB = 0 # Not applicable as the taxpayer is not a senior citizen 
                  section_24b = 150000 # Interest on home loan
                  deduction = calculate_80_deduction(section_80C_ELSS, section_80C_PPF, section_80C_Life, section_80CCC, section_80CCD1, section_80CCD1b, section_80D, section_80E, section_80G, section_80TTA_Bank1, section_80TTA_Bank2, section_80TTA_Bank3, section_80TTA_Bank4, section_80TTA_Bank5, section_80TTB, section_24b)
                  
# close the file                  
#sys.stdout.close()