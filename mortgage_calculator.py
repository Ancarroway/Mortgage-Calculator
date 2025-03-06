
def enter_data():
    """Prompt user for input data and initialize values."""
    print("**** Mortgage Calculation Program by Ashley*****")
    print("This program is going to calculate the mortgage payment")
    mortgage_amount = float(input("Enter the Mortgage amount ($): ").replace(",", ""))
    years = int(input("Enter the number of years: "))
    interest_rate = float(input("Enter the rate as %: "))
    return mortgage_amount, years, interest_rate


def calculate_interest_and_headings(mortgage_amount, interest_rate, years):
    """Calculate yearly payment using the fixed-rate mortgage formula and print report headings."""
    rate = interest_rate / 100  # Convert percentage to decimal
    yearly_payment = (mortgage_amount * rate) / (1 - (1 + rate) ** -years)  # Fixed-rate formula
    total_interest = (yearly_payment * years) - mortgage_amount  # Total interest over the life of the loan
    sum_of_years_digits = sum(range(1, years + 1))

    print(f"\nYearly pay: ${yearly_payment:.2f}")
    print(f"Total Interest: ${total_interest:.2f}")
    print(f"Sum of years digits: {sum_of_years_digits}\n")

    print("Year Starting   Balance   Year Interest  Principle Paid  Ending Balance")
    return yearly_payment, total_interest, sum_of_years_digits


def calculate_mortgage_schedule(mortgage_amount, years, interest_rate, yearly_payment, sum_of_years_digits):
    """Loop through each year to calculate and display the mortgage schedule."""
    starting_balance = mortgage_amount
    total_interest_paid = 0
    total_principal_paid = 0

    for year in range(1, years + 1):
        year_interest = starting_balance * (interest_rate / 100)
        total_interest_paid += year_interest
        principal_paid = yearly_payment - year_interest
        total_principal_paid += principal_paid
        ending_balance = starting_balance - principal_paid
        ending_balance = max(ending_balance, 0)  # Ensure no negative balance

        print(f"{year:5d} {starting_balance:13.2f} {year_interest:13.2f} {principal_paid:17.2f} {ending_balance:17.2f}")

        starting_balance = ending_balance

    return total_interest_paid, total_principal_paid, ending_balance


def print_ending_info(total_interest_paid, total_principal_paid, ending_balance):
    """Print ending balance and totals."""
    print(f"\nEnding balance: ${ending_balance:.2f}")
    print(f"Total interest paid: ${total_interest_paid:.2f}")
    print(f"Total principal paid: ${total_principal_paid:.2f}")


def main():
    """Main function to call other functions in sequence."""
    mortgage_amount, years, interest_rate = enter_data()
    yearly_payment, total_interest, sum_of_years_digits = calculate_interest_and_headings(mortgage_amount, interest_rate, years)
    total_interest_paid, total_principal_paid, ending_balance = calculate_mortgage_schedule(
        mortgage_amount, years, interest_rate, yearly_payment, sum_of_years_digits
    )
    print_ending_info(total_interest_paid, total_principal_paid, ending_balance)


if __name__ == "__main__":
    main()
