# Initialize variables
payout_per_bottle = 0.1  # Assuming $0.10 per bottle

while True:
    total_bottles = 0
    days = 7

    # Loop to enter the number of bottles for each day
    for day in range(1, days + 1):
        bottles = int(input(f"Enter number of bottles for day #{day}: "))
        total_bottles += bottles

    # Calculate total payout
    total_paid_out = total_bottles * payout_per_bottle

    # Output results
    print(f"\nThe total number of bottles collected is {total_bottles}")
    print(f"The total paid out is $ {total_paid_out:.1f}")

    # Ask if user wants to enter another week's worth of data
    keep_going = input("\nDo you want to enter another week’s worth of data? \n(Enter y or n): ")
    if keep_going.lower() != 'y':
        break

