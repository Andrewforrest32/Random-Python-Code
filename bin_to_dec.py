def bin_to_dec(num_bin):
    """Converts a binary string to a decimal integer."""
    num_dec = 0
    for i, digit in enumerate(num_bin[::-1]):  # Iterate in reverse order
        # Calculate the place value based on the index
        place_value = 2**i
        # Add the contribution of the current digit to the decimal value
        num_dec += int(digit) * place_value

    return num_dec

# Example usage
binary_number = input("Enter a binary number: ")
decimal_number = bin_to_dec(binary_number)

print(f"{binary_number} in decimal is {decimal_number}")
