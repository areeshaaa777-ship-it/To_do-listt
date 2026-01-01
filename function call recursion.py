def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n-1)

# Example usage:
n = 5
print(sum_numbers(n))  # Output: 15
