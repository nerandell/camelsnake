# camelsnake

`camelsnake` is a Python library for converting between camel case and snake case strings using regular expressions. It
provides two functions:

- `camel_to_snake(camel_str: str) -> str`: Converts a camel case string to a snake case string.
- `snake_to_camel(snake_str: str) -> str`: Converts a snake case string to a camel case string.

## Installation

To install `camelsnake`, simply use `pip`:

```
pip install camelsnake
```

## Usage

To use `camelsnake`, import the library and call the `camel_to_snake` and `snake_to_camel` functions with the
appropriate input strings. Here's an example:

```python
import camelsnake

camel_str = 'HelloWorld'
snake_str = camelsnake.camel_to_snake(camel_str)
print(snake_str)  # Output: 'hello_world'

snake_str = 'my_http_request'
camel_str = camelsnake.snake_to_camel(snake_str)
print(camel_str)  # Output: 'myHttpRequest'
```

## Testing

To run the tests for `camelsnake`, install `pytest` and run the following command in the project directory:

```
pytest
```

This will run the tests in the `test_camelsnake.py` file and output the results.

## License

`camelsnake` is licensed under the MIT License. See the `LICENSE` file for more information.

## Contributing

Contributions to `camelsnake` are welcome! If you find a bug or would like to suggest a new feature, please open an
issue or submit a pull request. See the `CONTRIBUTING.md` file for more information.

PS - I published this package in an attempt to see how ridiculous the task is that qualifies for a library of its own
