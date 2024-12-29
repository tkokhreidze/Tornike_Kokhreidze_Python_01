from A_leap_year_writing_your_own_functions import is_year_leap


def days_in_month(year, month):
#
# Write your new code here.
#
    if not isinstance(year, int) or not isinstance(month, int):
        return None  

    if month < 1 or month > 12 or year < 1582: 
        return None  

    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        days_in_months[2] = 29

    return days_in_months[month]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
