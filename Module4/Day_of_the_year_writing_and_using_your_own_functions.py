from A_leap_year_writing_your_own_functions import is_year_leap
from How_many_days_writing_and_using_your_own_functions import days_in_month


def day_of_year(year, month, day):
#
# Write your new code here.
#
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return None
    if month < 1 or month > 12 or day < 1 or year < 1582:
        return None
    
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days_in_months[2] = 29

    days_in_current_month = days_in_month(year, month)
    if days_in_current_month is None or day > days_in_current_month:
        return None 

    day_of_year = 0
    for m in range(1, month):
        days_in_prev_month = days_in_month(year, m)
        if days_in_prev_month is None: 
          return None
        day_of_year += days_in_prev_month
    day_of_year += day
    return day_of_year

print(day_of_year(2000, 12, 31))  # 366
print(day_of_year(2024, 2, 29)) # 60
print(day_of_year(2024, 1, 1)) # 1
print(day_of_year("2024", 1, 1)) #None
print(day_of_year(1500, 1, 1)) # None
