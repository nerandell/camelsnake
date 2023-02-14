import re


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
    snake_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_str)
    # Replace any occurrence of a lowercase letter or digit followed by an uppercase letter with
    # the lowercase letter or digit, an underscore, and the uppercase letter
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_str).lower()


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
    # Find any underscore character followed by a lowercase letter, and replace the underscore and lowercase letter
    # with the uppercase letter using a lambda function
    return re.sub('_(.)', lambda m: m.group(1).upper(), input_str)
