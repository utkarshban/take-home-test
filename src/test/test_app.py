import unittest
from unittest.mock import patch
from app import app
import json

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')

        self.assertEqual(response.status_code, 200)


    @patch('app.transactions.balance')
    def test_balance(self, mock_helper):
        mock_helper.return_value = {"ABC": 1000}
        tester = app.test_client(self)
        response = tester.get('/user/balance')
        response_body = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body, {"ABC": 1000})


    def test_add_transaction_render_template(self):
        tester = app.test_client(self)
        response = tester.get('/user/add/transaction', content_type='text/html')
        response_body = response.data.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertTrue("Enter the transaction details" in response_body)


    def test_spend_render_template(self):
        tester = app.test_client(self)
        response = tester.get('/user/spend', content_type='text/html')
        response_body = response.data.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertTrue("Enter the points to spend" in response_body)


    if __name__ == '__main__':
        unittest.main()
