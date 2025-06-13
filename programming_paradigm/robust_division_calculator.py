# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Attempts to divide numerator by denominator, handling:
      - Non-numeric inputs
      - Division by zero
    Returns either a float result or an error message string.
    """
    try:
        # 1. Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        # Thrown if either conversion fails
        return "Error: Please enter numeric values only."

    try:
        # 2. Perform division
        result = num / den
    except ZeroDivisionError:
        # Thrown if den == 0.0
        return "Error: Cannot divide by zero."
    
    # 3. If all went well, return formatted result
    return f"The result of the division is {result}"
