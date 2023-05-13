# Income Tax Calculation for salaried individuals

Helps you to get ITR-related stuff using Python

## Calculate tax under old regime (function calculate_income_from_salary_tax_old)

This function is for calculating income tax on total income earned from salary in the old tax regime in India. The tax rates and slabs are assumed as per the web page context. The age group is assumed to be below 60 years.
  
The function follows a progressive tax system where the tax rates increase with increasing income. The tax slabs and rates are defined in two lists, slabs and rates respectively. The slabs list contains the upper limit of each tax slab, while the rates list contains the tax rate for each slab.
  
The basic exemption limit of Rs. 2,50,000 is applied first. If the total income from salary is less than or equal to Rs. 2,50,000, then no tax is applicable, and the function returns zero tax. Otherwise, the total income from salary is reduced by Rs. 2,50,000, and the remaining income is taxed using the tax slabs and rates.
  
A for loop is used to iterate over the tax slabs and rates. If the remaining income falls within the current tax slab, then the tax is calculated using the corresponding tax rate. If the remaining income is more than the current tax slab, then the tax is calculated using the current tax slab and rate, and the remaining income is reduced by the current tax slab. This process continues until the remaining income becomes zero.
  
After calculating the tax on income from salary, a health and education cess of 4% is applied on the tax amount. The final tax amount is calculated by adding the cess to the tax amount.
  
The code also includes a provision for surcharge based on the total income from salary. The surcharge slabs and rates are defined in two lists, surcharge_slabs and surcharge_rates respectively. A for loop is used to iterate over the surcharge slabs and rates. 
  
If the total income from salary is above the current surcharge slab, then the surcharge rate for the current slab is applied on the tax amount. This process continues until the total income from salary becomes less than or equal to the current surcharge slab or the highest surcharge slab is reached.
  
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
9. Therefore, the tax rate for an income of 1500000 according to the code is 21.18% (317750 / 1500000 * 100)
