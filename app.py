# inputs
initial_balance = float(input("Enter investment amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate as %: "))

# Convert the rate ot a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
total_interest = 0.0

# Display the header for the table
print("%5s%21s%12s%18s" % ("Year", "Starting balance balance", "Interest", "Ending balance"))

# Compute and display the result
for year in range(1, years + 1):
    interest = initial_balance * rate
    end_balance = initial_balance + interest

    print("%5d%21f%12f%18f" % (year, initial_balance, interest, end_balance))
    initial_balance = end_balance
    total_interest += interest

# Display the totals for the period
print("Ending Balance: $%0.2f" % end_balance)
print("Total interst earned: $%0.2f" % total_interest)

