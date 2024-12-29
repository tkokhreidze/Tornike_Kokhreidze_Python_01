def print_month_calendar(month, year):
    month_names = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    days_in_month = [
        0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days_in_month[2] = 29  

    print(f"{month_names[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")

    day = 1
    weekday = 0 
    if month < 3:
      month += 12
      year -= 1

    day_of_month  = 1 
    adjusted_month  = month
    century  = year // 100
    year_of_century  = year % 100
    weekday = (day_of_month  + ((13 * (adjusted_month  + 1)) // 5) + year_of_century  + 
               (year_of_century  // 4) + (century  // 4) + (5 * century )) % 7
    weekday = (weekday + 5) % 7 
    
    print("   " * weekday, end="")

    while day <= days_in_month[month]:
        print(f"{day:2}", end=" ")
        day += 1
        weekday = (weekday + 1) % 7
        if weekday == 0:  
            print()

try:
    month, year = map(int, input("Enter month and year (mm-yyyy): ").split("-"))
    print_month_calendar(month, year)
except ValueError:
    print("Invalid input format. Please use mm-yyyy.")
