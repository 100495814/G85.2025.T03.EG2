import unittest
import os

from uc3m_money import AccountManager, AccountManagementException


class MyTestCase(unittest.TestCase):
    def test_minusvalido_2TC1(self):
        my_test = AccountManager()
        archivo = os.path.join(os.path.dirname(__file__), "src/main/python/uc3m_money/valid_deposit.json")
        with self.assertRaises(AccountManagementException) as nigga:
            my_test.deposit_into_manager(archivo)

        self.assertEqual(nigga.exception.message, "invalid_iban_file")








