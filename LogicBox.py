
# ==========================================
# Project: Logic Box
# Pattern Generator and Number Analyzer
# ==========================================


# ---------- Pattern Generator ----------


for i in range(1, 6):
    print("*" * i)

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of rows: "))

        for i in range(1, n + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print("Number", num, "is Even")
            else:
                print("Number", num, "is Odd")

            total = total + num

        print("Sum of all numbers from", start, "to", end, "is:", total)

    elif choice == 1 or choice == 2 or choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")