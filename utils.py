def isDigit(num_value, num_name):
    if num_value.isdigit():
        return True
    print(f"Error: {num_name} must be a number. {num_value} is not a number")
    return False


def getNumberFromUser(subject):
    while True:
        value = input(f"{subject}: ")
        if isDigit(value, "subject"):
            return int(value)


def setIndexAndSpacer(index):
    if index != "":
        return index + ". ", len(index) * " " + "  "
    else:
        return "", ""
