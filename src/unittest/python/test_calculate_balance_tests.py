import unittest
from freezegun import freeze_time
from uc3m_money import AccountManager
from uc3m_money import AccountManagementException

class MyTestCase(unittest.TestCase):
    """clase para probar el metodo"""

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc7(self):
        """
        Test TC7. INVALID IBAN CODE...
        Path: 1_2_3_4_5_22
        """
        iban = "ES355905439021242088295"
        am = AccountManager()
        # we won't reach the checking of files, so rename nothing
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance (iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")
