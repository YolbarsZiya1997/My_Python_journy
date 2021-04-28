# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def colour_print(text: str, effect: str,second_effect) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc

    Args:
        text (str): the text to print.
        effect (str): The effect we want. One fo the constants
        defined at the start of this module
    """
    output_string = "{0}{1}{2}{3}".format(effect,second_effect, text, RESET)
    print(output_string)
    
colour_print("Hello,Red", RED,BOLD)
colour_print("I am blue", BLUE,UNDERLINE)