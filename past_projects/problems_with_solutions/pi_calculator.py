import decimal
import argparse

def calculate_pi(n):
    """
    Calculates the value of pi to the Nth digit using the Chudnovsky algorithm.
    
    Parameters:
    n (int): The number of decimal places to calculate.
    
    Returns:
    str: The value of pi to the Nth decimal place.
    """
    decimal.getcontext().prec = n + 1  # Set the precision to n + 1 decimal places
    
    # Chudnovsky algorithm constants
    k = 0
    s = 0
    while k < n:
        s += (decimal.Decimal(-1) ** k * decimal.Decimal(factorial(6 * k)) * (decimal.Decimal(13591409) + decimal.Decimal(545140134) * decimal.Decimal(k))) / (decimal.Decimal(factorial(3 * k)) * decimal.Decimal(factorial(k)) ** 3 * decimal.Decimal(640320) ** (decimal.Decimal(3) * decimal.Decimal(k) + decimal.Decimal(1.5)))
        k += 1
    
    pi = (decimal.Decimal(12) * s) ** -1
    return str(pi)[:n+1]

def factorial(n):
    """
    Calculates the factorial of a given number.
    
    Parameters:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Calculate the value of pi to the Nth decimal place.")
    parser.add_argument("-n", "--decimal-places", type=int, required=True, help="The number of decimal places to calculate (minimum 5, maximum 55)")
    args = parser.parse_args()
    
    # Ensure the input is within the valid range
    if args.decimal_places < 5 or args.decimal_places > 55:
        print("Invalid input. Please enter a number between 5 and 55.")
        exit(1)
    
    # Calculate and print the value of pi to n decimal places
    print(f"The value of pi to {args.decimal_places} decimal places is: {calculate_pi(args.decimal_places)}")