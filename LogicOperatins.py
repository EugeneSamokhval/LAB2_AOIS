def logic_and(first_variable: int, second_variable: int):
    if first_variable and second_variable:
        return 1
    else:
        return 0


def logic_or(first_variable: int, second_variable: int):
    if not first_variable and not second_variable:
        return 0
    else:
        return 1


def logic_not(variable):
    if variable == 1:
        return 0
    else:
        return 1


def logic_then(first_variable: int, second_variable: int):
    if first_variable and not second_variable:
        return 0
    else:
        return 1
