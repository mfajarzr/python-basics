# A float is most commonly used for numbers with decimals, where precision matters and whole numbers aren’t enough.
# Here are the main use cases:
# 1. measurments
# 2. Fractions & precise math
# 3. Money & Percentages
# 4. Scientific & engineering calculation

# ⭐ Fuel cost calculator
while True:
    print("""
Fuel cost calculator
Input e to continue
Input q to close the program
""")

    start = input()

    if start.lower() == "q":
        print("Goodbye")
        break
    elif start.lower() == "e":
        print("\nLet's start\n")
        dis_traveled = float(input("Distance traveled (km): "))
        fuel_efficiency = float(input("Fuel efficiency (km/l): "))
        fuel_price = float(input("Fuel price per litre(Rp/l): "))

        total_fuel_used = dis_traveled / fuel_efficiency
        total_fuel_cost = total_fuel_used * fuel_price

        print(f"\nyour total fuel used is {total_fuel_used:.2f} l")
        print(f"\nyour total fuel cost is Rp.{total_fuel_cost:,.0f}")

        again = input("\nDo you want to continue (y/n): ")
        if again.lower() == "n":
            print("Goodbye")
            break
        elif again.lower() == "y":
            continue
        else:
            print("your input is invalid")
    else:
        print("Your input is invalid")
