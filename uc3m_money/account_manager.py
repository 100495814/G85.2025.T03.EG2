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

    """Class for providing the methods for managing the orders"""

    def __init__(self):
        pass

    @staticmethod
    def validate_iban(self, iban):
        """
        Valida un número IBAN español.
        """
        # Comprobar que el IBAN tiene la longitud correcta y empieza con 'ES'
        if len(iban) != 24 or not iban.startswith("ES") or not iban[2:].isdigit():
            return False

        # Convertir el IBAN al formato numérico para validación
        # #('ES' -> '1428' y mover los primeros 4 caracteres al final)
        iban_numerico = iban[4:] + '142800'

        # Tomar los primeros 9 dígitos como número inicial
        n = int(iban_numerico[:9])
        iban_numerico = iban_numerico[9:]  # Eliminar los primeros 9 dígitos procesados

        # Procesar el resto en bloques de 7 dígitos
        while iban_numerico:
            extra_digitos = iban_numerico[:7]  # Tomar los siguientes 7 dígitos
            iban_numerico = iban_numerico[7:]  # Eliminar los procesados

            # Concatenar con el resultado anterior y calcular mod 97
            n = int(str(n) + extra_digitos) % 97

        return n == 1  # Si el resultado final es 1, el IBAN es válido

    @staticmethod
    def validate_concept(concept: str):
        """Function validate concept"""

        # Check if concept is a string
        if not isinstance(concept, str):
            return False

        if len(concept) > 30 or (len(concept) < 10 and " " in concept):
            return False

        # Ensure that there are no special characters
        if re.search(r'[^a-zA-Z0-9 ]', concept):
            return False

        # Ensure that there is at least one space between the letters/numbers in the concept
        if " " not in concept:
            return False

        return True
    @staticmethod
    def validate_transfer_type(transfer_type: str):
        """Validate transfer type function"""
        if transfer_type not in {"ORDINARY", "URGENT", "IMMEDIATE"}:
            return False
        return True

    @staticmethod
    def validate_date(date):
        """Validate date function"""
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

    def transfer_request(self, from_iban: str, to_iban: str, concept: str,
                         transfer_type: str, date: str, amount: float):
        """Procesa una solicitud de transferencia con validación y almacenamiento."""

        # Validación de entradas
        validations = [
            (AccountManager.validate_iban(from_iban), "from_iban no válido"),
            (AccountManager.validate_concept(concept), "Concepto de transferencia inválido"),
            (AccountManager.validate_transfer_type(transfer_type),
             "tipo de transferencia no válido"),
            (AccountManager.validate_date(date), "fecha no válida"),
            (AccountManager.validate_amount(amount), "monto no válido"),
            (AccountManager.validate_iban(to_iban), "to_iban no válido")
        ]

        for condition, error_msg in validations:
            if not condition:
                raise ValueError(error_msg)

        # Crear objeto transferencia y generar código
        transfer = TransferRequest(from_iban, to_iban, concept,
                                   transfer_type, date, amount)
        transfer_code = hashlib.md5(str(transfer).encode()).hexdigest()
        transfer_data = transfer.to_json()
        transfer_data["transfer_code"] = transfer_code

        # Preparar directorio de datos
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)

        # Operaciones con el archivo JSON
        file_path = os.path.join(data_dir, 'transfers.json')

        try:
            with open(file_path, 'r+', encoding='utf-8') as f:
                try:
                    transfers = json.load(f)
                    if transfer_data in transfers:
                        raise AccountManagementException("Transferencia duplicada")
                    transfers.append(transfer_data)
                    f.seek(0)
                    json.dump(transfers, f, indent=4)
                except json.JSONDecodeError:
                    json.dump([transfer_data], f, indent=4)
        except FileNotFoundError:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump([transfer_data], f, indent=4)

        return transfer_code