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

    def test_deposit_with_invalid_json(self):
        """
        Verifica que la función lance AccountManagementException
        cuando el JSON no tenga la estructura requerida.
        """
        manager = AccountManager()
        with self.assertRaises(AccountManagementException) as context:
            manager.deposit_into_account(self.file_name)

        self.assertIn("Formato JSON incorrecto", str(context.exception))

    def test_deposit_with_valid_json(self):
        """
        Sobrescribe el archivo con datos válidos y verifica que la función
        no lance excepción y retorne una firma correcta.
        """
        # 1) Sobrescribimos el archivo con datos válidos
        valid_data = {
            "IBAN": "ES9121000418450200051332",
            "AMOUNT": "EUR 100.50"
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




if __name__ == "__main__":
    unittest.main()