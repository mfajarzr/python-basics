# String most commonly used for :
# 1. Showing Message to users
# 2. Storing names, labels, titles, etc
# 3. User input
# 4. f-String
# 5. Data that should not be used for calculation

print("Welcome to Makassar postal code directory for Subdistricts Tamalate")

name = input("\nPlease enter your name: ")
print("""
Choose your ward/village:
      1. Balang baru
      2. Barombong
      3. Bongaya
      4. Bonto duri
      5. Jongaya
      """)

while True:
    try:
        choice = int(
            input("\nPlease enter the name of your ward/ vilage number (1-5): "))

        if choice == 1:
            subdistrict = "Balang Baru"
            postal_code = "90224"
            break

        elif choice == 2:
            subdistrict = "Barombong"
            postal_code = "90225"
            break

        elif choice == 3:
            subdistrict = "Bongaya"
            postal_code = "90223"
            break

        elif choice == 4:
            subdistrict = "Bonto Duri"
            postal_code = "90224"
            break

        elif choice == 5:
            subdistrict = "Jongaya"
            postal_code = "90223"
            break

        else:
            print("Invalid, please select 1-5")

    except ValueError:
        print("Please enter the correct value")

print(
    f"Thank you {name}, you have selected {subdistrict}, your postal code is {postal_code}")
