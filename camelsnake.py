"""
This module provides functions to convert strings between camel case and snake case.

The `camel_to_snake` function converts a string from camel case to snake case by inserting an
underscore before each uppercase letter, except for the first letter in the string, and then
converting the whole string to lowercase.

The `snake_to_camel` function converts a string from snake case to camel case by capitalizing the
first letter of each word and removing any underscores.

Both functions use regular expressions to perform the conversions.

Example usage:

>>> camel_to_snake('camelCaseString')
'camel_case_string'

>>> snake_to_camel('snake_case_string')
'SnakeCaseString'
"""

import re

CAMEL_TO_SNAKE_PATTERN = re.compile('(.)([A-Z][a-z]+)')
CAMEL_TO_SNAKE_DIGIT_PATTERN = re.compile('([a-z0-9])([A-Z])')
SNAKE_TO_CAMEL_PATTERN = re.compile('_(.)')


def camel_to_snake(input_str):
    """
    Convert a string from camel case to snake case using regular expressions.

    Args:
        input_str (str): A string in camel case.

    Returns:
        str: The same string in snake case.

    Examples:
        >>> camel_to_snake('helloWorld')
        'hello_world'
        >>> camel_to_snake('MyHTTPRequest')
        'my_http_request'
    """
    # Replace any occurrence of a lowercase letter followed by an uppercase letter with
    # the lowercase letter, an underscore, and the uppercase letter
    snake_str = CAMEL_TO_SNAKE_PATTERN.sub(r'\1_\2', input_str)
    # Replace any occurrence of a lowercase letter or digit followed by an uppercase letter with
    # the lowercase letter or digit, an underscore, and the uppercase letter
    return CAMEL_TO_SNAKE_DIGIT_PATTERN.sub(r'\1_\2', snake_str).lower()


def snake_to_camel(input_str):
    """
    Convert a string from snake case to camel case using regular expressions.

    Args:
        input_str (str): A string in snake case.

    Returns:
        str: The same string in camel case.

    Examples:
        >>> snake_to_camel('hello_world')
        'helloWorld'
        >>> snake_to_camel('my_http_request')
        'myHttpRequest'
    """
    # Find any underscore character followed by a lowercase letter,
    # and replace the underscore and lowercase letter with the uppercase letter
    # using a lambda function
    return SNAKE_TO_CAMEL_PATTERN.sub(lambda m: m.group(1).upper(), input_str)
