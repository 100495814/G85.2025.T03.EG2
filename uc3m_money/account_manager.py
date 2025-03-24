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
    def validate_iban(iban: str):
        """Returns True if the IBAN is a valid Spanish IBAN, otherwise False."""
        # Check if IBAN is a string
        if not isinstance(iban, str):
            return False

        # Validate basic IBAN format for Spain (must be exactly 24 characters and start with 'ES')
        if len(iban) != 24 or not iban.startswith("ES") or not iban[2:].isdigit():
            return False

        # Move the first 4 characters to the end
        iban_rearranged = iban[4:] + iban[:4]

        # Convert letters to numbers (A=10, B=11, ..., Z=35)
        iban_numeric = ''.join(str(ord(char) - 55) if char.isalpha() else char
        for char in iban_rearranged)

        # Compute mod 97 using the piecewise method
        remainder = int(iban_numeric[:9]) % 97
        iban_numbers = iban_numeric[9:]

        while iban_numbers:
            remainder = int(str(remainder) + iban_numbers[:7]) % 97
            iban_numbers = iban_numbers[7:]

        # Return True if valid, otherwise False
        if remainder == 1:
            return True
        return False


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
        """Validate date finction"""
        try:
            dt = datetime.strptime(date, "%d/%m/%Y")
            if not (2025 <= dt.year < 2051 and dt >= datetime.today()):
                return False
        except ValueError:
            return False
        return True


    @staticmethod
    def validate_amount(amount):
        """Validate amount function"""
        # Check if amount is an integer or float
        if not isinstance(amount, (int, float)):
            return False
        # Check if the amount is in the correct range
        if  (10.00 <= amount <= 10000.00 and round(amount, 2) == amount):
            return True
        return False

    def transfer_request(self, from_iban : str, to_iban: str, concept: str,
                         transfer_type: str, date: str, amount: float):
        """Transfer request function"""
        # needs to do three things:
        # validate input data
        # get a transfer_code
        # store all transfer info in a json file in case everything is ok

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

        data_dir = os.path.join(os.path.dirname(_file_),'..', 'data')
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