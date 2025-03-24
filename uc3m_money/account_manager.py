"""Module """
import os
import re
import hashlib
import json
from datetime import datetime
from pathlib import Path
from uc3m_money.account_deposit import AccountDeposit
from uc3m_money.transfer_request import TransferRequest
from uc3m_money.account_management_exception import AccountManagementException


class AccountManager:

    """Class for providing the methods for managing the orders"""
    def _init_(self):
        pass

    @staticmethod
    def validate_concept(concept: str):
        """Función validar concepto"""

        # Comprueba si el concepto es un string
        if not isinstance(concept, str):
            return False

        if len(concept) > 30 or (len(concept) < 10 and " " in concept):
            return False

        # Se asegura de que no haya caracteres especiales
        if re.search(r'[^a-zA-Z0-9 ]', concept):
            return False

        # Se asegura de que haya al menos un espacio entre letras y num en concept
        if " " not in concept:
            return False

        return True
    @staticmethod
    def validate_transfer_type(transfer_type: str):
        """Función validar tipo de transferencia"""
        if transfer_type not in {"ORDINARY", "URGENT", "IMMEDIATE"}:
            return False
        return True

    @staticmethod
    def validate_date(date):
        """Función validar fecha"""
        try:
            dt = datetime.strptime(date, "%d/%m/%Y")
            if not (2025 <= dt.year < 2051 and dt >= datetime.today()):
                return False
        except ValueError:
            return False
        return True

    @staticmethod
    def validate_amount(amount):
        """Verifica si el amount es válido.
        Comprueba que: Sea un entero o float,
        esté entre 10.00 y 10000.00,
        tenga exactamente 2 decimales.
        """
        if not isinstance(amount, (int, float)):
            return False

        return (10.00 <= amount <= 10000.00
                and round(amount, 2) == amount)

    def validate_iban(iban: str):
        """Devuelve True si el IBAN es un IBAN español válido, en otro caso devuelve False."""
        # Comprueba que IBAN es un string
        if not isinstance(iban, str):
            return False

        # Validar formato IBAN básico para España (debe tener exactamente 24 caracteres y empezar por 'ES')
        if len(iban) != 24 or not iban.startswith("ES") or not iban[2:].isdigit():
            return False

        # Mueve los primeros 4 caracteres al final.
        iban_rearranged = iban[4:] + iban[:4]

        # Convertir letras a números (A=10, B=11, ..., Z=35)
        iban_numeric = ''.join(str(ord(char) - 55) if char.isalpha() else char
        for char in iban_rearranged)

        # Calcular mod 97 usando el metodo por partes
        remainder = int(iban_numeric[:9]) % 97
        iban_numbers = iban_numeric[9:]

        while iban_numbers:
            remainder = int(str(remainder) + iban_numbers[:7]) % 97
            iban_numbers = iban_numbers[7:]

        # Devuelve True si es valido, en otro caso devuelve False
        if remainder == 1:
            return True
        return False


    @staticmethod
    def validate_concept(concept: str):
        """Funcion validar concepto"""

        # Comprueba que el concepto es un string
        if not isinstance(concept, str):
            return False

        if len(concept) > 30 or (len(concept) < 10 and " " in concept):
            return False

        # Se asegura de que no haya caracteres especiales
        if re.search(r'[^a-zA-Z0-9 ]', concept):
            return False

        # Se asegura de que haya al menos un espacio entre las letras/números del concepto
        if " " not in concept:
            return False

        return True
    @staticmethod
    def validate_transfer_type(transfer_type: str):
        """Función validar tipo de transferencia"""
        if transfer_type not in {"ORDINARY", "URGENT", "IMMEDIATE"}:
            return False
        return True

    @staticmethod
    def validate_date(date):
        """Funcion validar fecha"""
        try:
            dt = datetime.strptime(date, "%d/%m/%Y")
            if not (2025 <= dt.year < 2051 and dt >= datetime.today()):
                return False
        except ValueError:
            return False
        return True


    @staticmethod
    def validate_amount(amount):
        """Funcion validar cantidad"""
        # Comprueba si el importe es un número entero o flotante
        if not isinstance(amount, (int, float)):
            return False
        # Comprueba si la cantidad está en el rango correcto
        if  (10.00 <= amount <= 10000.00 and round(amount, 2) == amount):
            return True
        return False

    def transfer_request(self, from_iban : str, to_iban: str, concept: str,
                         transfer_type: str, date: str, amount: float):
        """Funcion solicitud de transferencia"""
        # Necesita: Validar los datos de entrada, Obtener un código de transferencia,
        # Almacenar toda la información de la transferencia en un archivo JSON en caso de que este bien

        if not AccountManager.validate_iban(from_iban):
            raise ValueError("from_iban not valid")

        if not AccountManager.validate_concept(concept):
            raise ValueError("Invalid transfer concept")

        if not AccountManager.validate_transfer_type(transfer_type):
            raise ValueError("transfer type is not valid")

        if not AccountManager.validate_date(date):
            raise ValueError("date not valid")

        if not AccountManager.validate_amount(amount):
            raise ValueError("amount not valid")

        if AccountManager.validate_iban(from_iban):
            if AccountManager.validate_iban(to_iban):
                transfer_code = TransferRequest(from_iban, to_iban, concept,
                                                transfer_type, date, amount)
            else:
                raise ValueError("to_iban not valid")



        transfer = TransferRequest(from_iban, to_iban, concept, transfer_type, date, amount)
        transfer_code = hashlib.md5(str(transfer).encode()).hexdigest()

        transfer_data = transfer.to_json()
        transfer_data["transfer_code"] = transfer_code

        data_dir = os.path.join(os.path.dirname(__file__),'..', 'data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        ruta_json = os.path.join(data_dir, 'transfers.json')
        try:
            print("JSON File saved in:", ruta_json)
            with open("transfers.json", "r+", encoding='utf-8') as file:
                transfers = json.load(file)
                if transfer_data in transfers:
                    raise AccountManagementException("Duplicate transfer")
                transfers.append(transfer_data)
                file.seek(0)
                json.dump(transfers, file, indent=4)
        except FileNotFoundError:
            print("The file does not exists, a new one will be created")
            with open("transfers.json", "w", encoding='utf-8') as file:
                json.dump([transfer_data], file, indent=4)
        except json.JSONDecodeError:
            print("Error reading the JSON file, a new one will be created")
            with open("transfers.json", "w", encoding='utf-8') as file:
                json.dump([transfer_data], file, indent=4)

        return transfer_code
