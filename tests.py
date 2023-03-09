import unittest

import requests


class TestAPIapp(unittest.TestCase):

    def setUp(self):
        self.path = 'http://127.0.0.1:8080/flask'

    def test_connection(self):
        """ check connections to running server + DB Redis """
        response = requests.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_create_key_value(self):
        key = 'key_test'
        value = 'value_01_test'
        url_key = self.path + '/' + key
        response = requests.post(url=url_key, data=value)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()


