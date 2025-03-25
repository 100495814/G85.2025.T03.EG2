import unittest
import os
import json

from uc3m_money import AccountManager, AccountManagementException


class TestDeposit(unittest.TestCase):
    def setUp(self):
        """
        Crea (o sobrescribe) el archivo 'valid_deposit.json' con datos inválidos
        antes de cada prueba.
        """
        self.file_name = "valid_deposit.json"

        # Contenido inválido: falta la clave "AMOUNT"
        invalid_data = {
            "IBAN": "ES9121000418450200051332"
        }

        with open(self.file_name, "w") as f:
            json.dump(invalid_data, f)

    def tearDown(self):
        """
        Elimina el archivo después de cada prueba para que no afecte a otras.
        """
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_TCNV2(self):
        """
        Verifica que la función lance AccountManagementException
        cuando el JSON no tenga la estructura requerida.
        """
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCV1(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121000418450200051332",
            "AMOUNT": "EUR 100.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        try:
            deposit_signature = manager.deposit_into_account(self.file_name)
            # 3) Verificamos que el resultado sea un string (posible hash)
            self.assertIsInstance(deposit_signature, str)
            # Si esperamos un hash SHA-256 en hexadecimal, debería tener 64 caracteres
            self.assertEqual(len(deposit_signature), 64)
        except AccountManagementException as e:
            self.fail(f"No debería lanzar excepción con datos válidos. Excepción: {e}")

    def test_TCNV1(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "AMOUNT": "EUR 100.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV3(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "GB29NWBK60161331926819",
            "AMOUNT": "EUR 100.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("IBAN inválido", str(context.exception))

    def test_TCNV4(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES912180841845020005133",
            "AMOUNT": "EUR 100.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("IBAN inválido", str(context.exception))

    def test_TCNV5(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES91218084184502000513344",
            "AMOUNT": "EUR 100.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("IBAN inválido", str(context.exception))

    def test_TCNV6(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "USD 100.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Moneda incorrecta", str(context.exception))

    def test_TCNV7(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR one hundred"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Monto no numérico", str(context.exception))

    def test_TCNV8(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 0.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Monto inválido", str(context.exception))

    def test_TCNV9(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR -1.00"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Monto inválido", str(context.exception))

    def test_TCV2(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 0.01"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        try:
            deposit_signature = manager.deposit_into_account(self.file_name)
            # 3) Verificamos que el resultado sea un string (posible hash)
            self.assertIsInstance(deposit_signature, str)
            # Si esperamos un hash SHA-256 en hexadecimal, debería tener 64 caracteres
            self.assertEqual(len(deposit_signature), 64)
        except AccountManagementException as e:
            self.fail(f"No debería lanzar excepción con datos válidos. Excepción: {e}")

    def test_TCV3(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 999999999.99"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        try:
            deposit_signature = manager.deposit_into_account(self.file_name)
            # 3) Verificamos que el resultado sea un string (posible hash)
            self.assertIsInstance(deposit_signature, str)
            # Si esperamos un hash SHA-256 en hexadecimal, debería tener 64 caracteres
            self.assertEqual(len(deposit_signature), 64)
        except AccountManagementException as e:
            self.fail(f"No debería lanzar excepción con datos válidos. Excepción: {e}")

    def test_TCV4(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 123.45"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        try:
            deposit_signature = manager.deposit_into_account(self.file_name)
            # 3) Verificamos que el resultado sea un string (posible hash)
            self.assertIsInstance(deposit_signature, str)
            # Si esperamos un hash SHA-256 en hexadecimal, debería tener 64 caracteres
            self.assertEqual(len(deposit_signature), 64)
        except AccountManagementException as e:
            self.fail(f"No debería lanzar excepción con datos válidos. Excepción: {e}")

    def test_TCV5(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 123.4"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        try:
            deposit_signature = manager.deposit_into_account(self.file_name)
            # 3) Verificamos que el resultado sea un string (posible hash)
            self.assertIsInstance(deposit_signature, str)
            # Si esperamos un hash SHA-256 en hexadecimal, debería tener 64 caracteres
            self.assertEqual(len(deposit_signature), 64)
        except AccountManagementException as e:
            self.fail(f"No debería lanzar excepción con datos válidos. Excepción: {e}")

    def test_TCV6(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 123.4"
        }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        try:
            deposit_signature = manager.deposit_into_account(self.file_name)
            # 3) Verificamos que el resultado sea un string (posible hash)
            self.assertIsInstance(deposit_signature, str)
            # Si esperamos un hash SHA-256 en hexadecimal, debería tener 64 caracteres
            self.assertEqual(len(deposit_signature), 64)
        except AccountManagementException as e:
            self.fail(f"No debería lanzar excepción con datos válidos. Excepción: {e}")

    def test_TCNV10(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {"{"
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 123"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV12(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332IBAN:ES9121808418450200051332",
            "AMOUNT": "EUR 123"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("IBAN inválido", str(context.exception))


    def test_TCNV15(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 123""AMOUNT: EUR 123"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Monto no numérico", str(context.exception))

    def test_TCNV16(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 123"
                "}"}
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Monto no numérico", str(context.exception))

    def test_TCNV18(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBANIBAN": "ES9121808418450200051332",
            "AMOUNT": "EUR 100.50"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV19(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "": "ES9121808418450200051332",
            "AMOUNT": "EUR 100.50"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV20(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "aa": "ES9121808418450200051332",
            "AMOUNT": "EUR 100.50"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV21(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "AMOUNTAMOUNT": "EUR 100.50"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV22(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "": "EUR 100.50"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_TCNV23(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121808418450200051332",
            "aa": "EUR 100.50"
            }
        with open(self.file_name, "w") as f:
            json.dump(valid_data, f)

        # 2) Llamamos a la función
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))



if __name__ == "__main__":
    unittest.main()