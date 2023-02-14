from camelsnake import camel_to_snake, snake_to_camel
import unittest


class TestCamelSnakeRegex(unittest.TestCase):
    def test_empty_string_camel_to_snake(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_single_char_camel_to_snake(self):
        self.assertEqual(camel_to_snake('A'), 'a')

    def test_camel_to_snake_hello_world(self):
        self.assertEqual(camel_to_snake('HelloWorld'), 'hello_world')

    def test_camel_to_snake_http_request(self):
        self.assertEqual(camel_to_snake('MyHTTPRequest'), 'my_http_request')

    def test_camel_to_snake_with_numbers(self):
        self.assertEqual(camel_to_snake('ThisIsCamelCase123'), 'this_is_camel_case123')

    def test_empty_string_snake_to_camel(self):
        self.assertEqual(snake_to_camel(''), '')

    def test_single_char_snake_to_camel(self):
        self.assertEqual(snake_to_camel('a'), 'a')

    def test_snake_to_camel_hello_world(self):
        self.assertEqual(snake_to_camel('hello_world'), 'helloWorld')

    def test_snake_to_camel_http_request(self):
        self.assertEqual(snake_to_camel('my_http_request'), 'myHttpRequest')

    def test_snake_to_camel_with_numbers(self):
        self.assertEqual(snake_to_camel('this_is_snake_case123'), 'thisIsSnakeCase123')
