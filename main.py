# Monthly Rent Calculator 

ask_for = input("Do you have to calculate Total of each Expense (Yes/No): ").lower()
if ask_for == "yes" or ask_for == "y":
    rent_of_room = int(input("Enter Rent of the room: "))
    monthly_kitchen_bill = int(input("Enter the Total bill of monthly Expenses of Kitchen: "))
    electricity_units_consume = int(input("Enter the Total Electricity units of the Month: "))
    electricity_cost_per_unit = float(input("Enter the cost of one Electricity unit: "))
    gass_units_consume = int(input("Enter the Total Gas units of the Month: "))
    gass_cost_per_unit = float(input("Enter the Total Gas cost per unit: "))
    room_mates = int(input("Enter Roommates: "))
    print("\n")

    # Displaying all the inputs
    print("Rent of the Room:", rent_of_room)
    print("Kitchen Expenses:", monthly_kitchen_bill)
    print("Total Electricity units consumed:", electricity_units_consume)
    print("Electricity Cost Per Unit:", electricity_cost_per_unit)

    # Calculate electricity and gas bills correctly
    electricity_bill = electricity_units_consume * electricity_cost_per_unit
    print("Total Monthly Electricity Bill:", electricity_bill)

    print("Total Gas units consumed:", gass_units_consume)
    print("Gas Cost Per Unit:", gass_cost_per_unit)

    gass_bill = gass_units_consume * gass_cost_per_unit
    print("Total Monthly Gas Bill:", gass_bill)

    print("Roommates among whom the expenses will be divided:", room_mates)
    print("\n")

    # Correctly compute the total monthly expenses
    total_monthly_expenses = rent_of_room + monthly_kitchen_bill + electricity_bill + gass_bill
    print("Your Total Bill for all these expenses is:", total_monthly_expenses, "\n")

    # Calculate the amount each roommate has to pay
    among_each = total_monthly_expenses / room_mates
    print(f"Each of you will have to pay: {among_each} \nThank You!")
else:
    print("Please calculate the total expenses.")