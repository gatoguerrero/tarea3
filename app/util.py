# pylint: disable=no-else-return
def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"

#Se trajo está función desde calc.py y se la mejoró para que valide un solo argumento de ser necesario        
def check_types(x, y=None):
    if not isinstance(x, (int, float)):
        raise TypeError("First parameter must be a number")
    if y is not None and not isinstance(y, (int, float)):
        raise TypeError("Second parameter must be a number")        
