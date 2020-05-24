def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    open_bracket = close_bracket = 0
    for sym in brackets_row:
        if sym == '(':
            open_bracket += 1
        elif sym == ')':
            if open_bracket > 0:
                open_bracket -= 1
            else:
                return False
    return False if open_bracket else True
