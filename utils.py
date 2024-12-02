def isDigit(num_value, num_name):
    if num_value.isdigit():
        return True
    print(f"Error: {num_name} must be a number. {num_value} is not a number")
    return False
