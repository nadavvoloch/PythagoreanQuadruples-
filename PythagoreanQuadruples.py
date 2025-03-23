import random
import csv

def return_quad_lst(x):
    a = x
    if a % 2 == 1:
        b = (a ** 2 - 1) // 2
        c = (a ** 4) // 8 + (a ** 2) // 4 - 3 // 8
        d = c + 1
    else:
        b = (a ** 2) // 4 - 1
        if b % 2 == 0:
            c = (a ** 4) // 64 + (a ** 2) // 8 - 3 // 4
            d = c + 2
        else:
            c = (a ** 4) // 32 + (a ** 2) // 4
            d = c + 1
    return [int(a), int(b), int(c), int(d)]

def generate_unique_random_numbers(n):
    if n > (10000 - 3 + 1):
        raise ValueError("Cannot generate more than 9998 unique numbers in the range 3 to 10000.")
    return random.sample(range(3, 1001), n)

# Formatting helpers
headers = ['a', 'b', 'c', 'd', 'a² + b² + c²', 'd²', 'Match?']
col_widths = [6, 12, 15, 15, 24, 24, 8]

def format_row(row, widths, align="right"):
    cells = []
    for val, width in zip(row, widths):
        if align == "left" and isinstance(val, str):
            cells.append(f"{val:<{width}}")
        else:
            cells.append(f"{val:>{width}}")
    return "| " + " | ".join(cells) + " |"

# Main execution
z = int(input("How many quadruples do you want? "))
rand = generate_unique_random_numbers(z)

# Print table header
print(format_row(headers, col_widths, align="left"))
print("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")

# Prepare CSV
with open('pythagorean_quadruples.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for number in rand:
        a, b, c, d = return_quad_lst(number)
        lhs = a**2 + b**2 + c**2
        rhs = d**2
        match = "YES" if lhs == rhs else "NO"

        row_data = [a, b, c, d, lhs, rhs, match]
        print(format_row(row_data, col_widths))
        writer.writerow(row_data)

print("\n✅ Results saved to 'pythagorean_quadruples.csv'")
