import os


def clear_terminal():
    """Clears a terminal output"""
    # screen will be cleared for Mac, Linux
    if os.name == 'posix':
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')
