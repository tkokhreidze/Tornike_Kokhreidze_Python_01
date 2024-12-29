def power_of_x(start, end):
    for x in range(start, end + 1):
        # First column: (x^2)
        square = x * x
        square_str = f"{x:2} * {x:2} = {square:3}"
        
        # Second column: (x^10)
        power_10 = x ** 10
        power_10_str = f"{x:2} ^ 10 = {power_10:13}"
        
        # Third column: (x^x)
        power_self = x ** x
        power_self_str = f"{x:2} ^ {x:2} = {power_self}"
        
        
        print(f"{square_str} | {power_10_str} | {power_self_str}")

# Example
power_of_x(1, 15)