# Income Tax Calculation for salaried individuals

Helps you to get ITR-related stuff using Python

## Calculate tax under old regime 
calculate_income_from_salary_tax_old()
  
### Example:
For an income of 1500000, the tax calculation in the function will be as follows:

1. The basic exemption limit of Rs. 2,50,000 will be applied, so the taxable income will be 1250000 (1500000 - 250000).
2. The first slab of 250000 will be taxed at a rate of 5%, which amounts to 12500 (250000 * 0.05).
3. The second slab of 250000 will be taxed at a rate of 20%, which amounts to 50000 (250000 * 0.2).
4. The remaining income of 750000 will be taxed at a rate of 30%, which amounts to 225000 (750000 * 0.3).
5. The total tax liability before cess and surcharge will be the sum of the tax amounts for each slab, which is 287500 (12500 + 50000 + 225000).
6. A health and education cess of 4% will be applied on the tax amount, which amounts to 11500 (287500 * 0.04).
7. Since the income is above 500000, a surcharge of 10% will be applied on the tax amount, which amounts to 28750 (287500 * 0.1).
8. The total tax liability after cess and surcharge will be the sum of the tax amount and the surcharge, which is 317750 (287500 + 28750).
9. Therefore, the tax rate for an income of 1500000 according to the code is 21.18% (317750 / 1500000 * 100)


## Output
```
FY 2022-23 (AY 2023-24) TAX CALCULATION

1. Income from salary

1.1 Input
You have selected the old regime
Annual income entered is ₹15.0 lakh

1.2 Output
Health & Education cess (New regime) is ₹18000.0.
Health & Education cess (Old regime) is ₹10500.0.
You have to pay ₹300300.0 under old tax regime
You have to pay ₹514800.0 under new tax regime
You will save ₹214500.0 under new regime


2. DEDUCTION CALCULATION

2.1 Input
80C Deduction : ₹60000
Medical 80D deduction : ₹25000
Home loan 24B deduction : ₹0

2.2 Output
Your total deductions under the old regime are ₹85000
```
