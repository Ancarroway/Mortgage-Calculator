
# Mortgage Calculation Program by Ashley

## Description
This program calculates the yearly **mortgage payment schedule** based on user input for:

- Mortgage amount
- Loan term (years)
- Interest rate (as a percentage)

The program uses the **Fixed-Rate Mortgage Formula** to compute the yearly payment, and then generates a complete amortization schedule showing the:

- Starting Balance
- Interest Paid
- Principal Paid
- Ending Balance for each year.

## Features
✅ Interactive user input for mortgage details.  
✅ Calculates **total interest paid** and **total principal paid** over the life of the loan.  
✅ Displays a clear **amortization schedule** in table format.  
✅ Handles invalid inputs gracefully using `.replace()` to handle commas in dollar amounts.  
✅ Ensures the final balance never goes negative.

## How to Run
1. Save the program code to a file called `mortgage_calculator.py`.  
2. Run the program using:
```
python mortgage_calculator.py
```
3. Follow the prompts to enter the mortgage amount, loan term, and interest rate.

## Example Output
```
**** Mortgage Calculation Program by Ashley*****
This program is going to calculate the mortgage payment
Enter the Mortgage amount ($): 200,000
Enter the number of years: 30
Enter the rate as %: 5

Yearly pay: $13052.66
Total Interest: $191579.96
Sum of years digits: 465

Year Starting   Balance   Year Interest  Principle Paid  Ending Balance
    1     200000.00      10000.00           3052.66       196947.34
    2     196947.34       9847.37           3205.29       193742.05
...
```

## About
This program was created to **practice procedural programming**, calculations using **formulas**, handling **user input**, and creating **tabular reports**. It also demonstrates how to calculate the amortization schedule step-by-step.
