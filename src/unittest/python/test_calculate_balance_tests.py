import unittest
import pathlib
from pathlib import Path
import os
import json
from json import JSONDecodeError
from freezegun import freeze_time
from uc3m_money import AccountManager
from uc3m_money import AccountManagementException

class MyTestCase(unittest.TestCase):
    """clase para probar el metodo"""

    def test_calculate_balance_ok_tc1(self):
        """
        1_2_3_5_10_11_10_14_16_17_18_19
        """
        iban = "ES9121000418450200051332"
        am = AccountManager()
        source_path = (str(Path.home()) + r"")
        destination_path = (str(Path.home()) + r"")
        os.rename(source_path, destination_path)  # Toma el json con formato incorrecto como all_transactions
        self.assertTrue(am.calculate_balance(iban))  # valid
        os.rename(destination_path, source_path)  # restaurar el archivo json a su nombre original

        path_balance_file = (str(Path.home()) + r"")

        try:
            with open(path_balance_file, encoding="UTF-8", mode="r") as file:
                balance_data = json.load(file)
        except FileNotFoundError as fnferr:
            balance_data = {}
        except JSONDecodeError:
            balance_data = {}

        try:
            v1, v2, v3 = balance_data["iban"], balance_data["date"], balance_data["balance"]
        except KeyError as keyerr:
            self.assertFalse(True)

        # Verificar el saldo calculado correctamente usando assertEqual (precisión de punto flotante)
        self.assertAlmostEqual(float(balance_data["balance"]), -1280.06)

    def test_calculate_balance_ok_tc2(self):
        """
        1_2_3_5_6_7_8_9_10_11_12_13_10_11_10_14_16_17_18_19
        """
        iban = "ES865834204541216877204"
        am = AccountManager()
        source_path = (str(Path.home()) + r"")
        destination_path = (str(Path.home()) + r"")
        os.rename(source_path, destination_path)  # Toma el json con formato incorrecto como all_transactions
        self.assertTrue(am.calculate_balance(iban))  # valid
        os.rename(destination_path, source_path)  # restaurar el archivo json a su nombre original

        path_balance_file = (str(Path.home())
                            + r"")

        try:
            with open(path_balance_file, encoding="UTF-8", mode="r") as file:
                balance_data = json.load(file)
        except FileNotFoundError as fnferr:
            balance_data = {}
        except JSONDecodeError:
            balance_data = {}

        try:
            v1, v2, v3 = balance_data["iban"], balance_data["date"], balance_data["balance"]
        except KeyError as keyerr:
            self.assertFalse(True)

        # Verificar el saldo calculado correctamente usando assertEqual (precisión de punto flotante)
        self.assertAlmostEqual(float(balance_data["balance"]), -1280.06)


    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc3(self):
        """
        1_2_3_5_6_7_8_9_10_11_10_14_15
        """
        iban = "ES7620770024003102575766"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance (iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc4(self):
        """
        1_2_3_5_6_7_8_9_10_14_15
        """
        iban = "ES9111112222333344445555"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance (iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc5(self):
        """
        1_2_3_4
        """
        iban = "ES00INVALID00000000000000"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance(iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc6(self):
        """
        1_2_3_5_6_7_8_10_11_10_14_15
        """
        iban = "ES9111112222333344445555"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance(iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc7(self):
        """
        1_2_3_5_10
        """
        iban = "ES7921000813610123456789"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance(iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc8(self):
        """
        1_2_3_5_10_11_10_14_15
        """
        iban = "ES1234567890123456789012"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance(iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc9(self):
        """
        1_2_3_5_10_14_15
        """
        iban = "ES7121000418450200051332"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance(iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

    @freeze_time("2025-03-19 12:00:00")
    def test_calculate_balance_ko_tc10(self):
        """
        1_2_3_5_10_11_12_13_10_11_10_14_15
        """
        iban = "ES9521000418450200051332"
        am = AccountManager()
        with self.assertRaises(AccountManagementException) as result:
            am.calculate_balance(iban)
        self.assertEqual(result.exception.message, "InvalidIBANCode")

