def print_multiplication_table(size):
    for row_number in range(1, size + 1):
        for column_number in range(1, size + 1):
            product = row_number * column_number
            print(f"{product:4}", end="")
        print()

# Example
print_multiplication_table(10)