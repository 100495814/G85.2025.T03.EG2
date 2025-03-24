"""class for testing the regsiter_order method"""
import unittest
from freezegun import freeze_time
from uc3m_money import AccountManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)

    @freeze_time("2024-03-22")
    def test_transfer_request_ok_tc1(self):
        """TEST DE CASO VALIDO"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Nomina marzo"
        amount_to_test = 10.00
        date_to_test = "01/01/2025"
        type_to_test = "ORDINARY"
        transfer_code = my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                                    concept=concept_to_test, amount=amount_to_test,
                                                    date=date_to_test, transfer_type=type_to_test)
        self.assertEqual(transfer_code, "95ffa9fad91a0e658d761dad85323aae")

    @freeze_time("2024-03-22")
    def test_transfer_request_ok_tc2(self):
        """TEST DE CASO VALIDO"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Pago factura"
        amount_to_test = 10.01
        date_to_test = "2/2/2026"
        type_to_test = "URGENT"
        transfer_code = my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                                    concept=concept_to_test, amount=amount_to_test,
                                                    date=date_to_test, transfer_type=type_to_test)
        self.assertEqual(transfer_code, "ba0a96663a0cacbe561efae348945e9f")

    @freeze_time("2024-03-22")
    def test_transfer_request_ok_tc3(self):
        """TEST DE CASO VALIDO"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Envio Internacional"
        amount_to_test = 10000.00
        date_to_test = "31/12/2050"
        type_to_test = "IMMEDIATE"
        transfer_code = my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                                    concept=concept_to_test, amount=amount_to_test,
                                                    date=date_to_test, transfer_type=type_to_test)
        self.assertEqual(transfer_code, "65ff3ac6560bb40abc13606890d1b451")

    @freeze_time("2024-03-22")
    def test_transfer_request_ok_tc4(self):
        """TEST DE CASO VALIDO"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferencia Pago Educacion"
        amount_to_test = 9999.99
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        transfer_code = my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                                    concept=concept_to_test, amount=amount_to_test,
                                                    date=date_to_test, transfer_type=type_to_test)
        self.assertEqual(transfer_code, "3f1a02b45c1abbedf2763478687e2e43")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc5(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = 5
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 9999.99
        date_to_test = "30/11/2049"
        type_to_test = "URGENT"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc6(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES9999999999999999999999"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 9999.99
        date_to_test = "30/11/2049"
        type_to_test = "URGENT"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc7(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES5674389475483473947883939"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc8(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES2357642374234823883"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc9(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "TM45393287654100123456789012"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc10(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "779121000418450200051332"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc11(self):
        """TEST PARA LOS CASOS NO VÁLIDOS FROM_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ESkelokekelokekelokekelo"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "from_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc12(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = 5
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc13(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9999999999999999999999"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc14(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES5674389475483473947883939"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc15(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES2357642374234823883"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc16(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "TM45393287654100123456789012"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc17(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "779121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc18(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TO_IBAN"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ESkelokekelokekelokekelo"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "to_iban not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc19(self):
        """TEST PARA LOS CASOS NO VÁLIDOS CONCEPT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = 5
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "Invalid transfer concept")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc20(self):
        """TEST PARA LOS CASOS NO VÁLIDOS CONCEPT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Este concepto sería muy largooo"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "Invalid transfer concept")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc21(self):
        """TEST PARA LOS CASOS NO VÁLIDOS CONCEPT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "qwer tyui"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "Invalid transfer concept")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc22(self):
        """TEST PARA LOS CASOS NO VÁLIDOS CONCEPT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "¿?=¡)¿?=¡)aa"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "Invalid transfer concept")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc23(self):
        """TEST PARA LOS CASOS NO VÁLIDOS CONCEPT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "solounstring"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "Invalid transfer concept")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc24(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TYPE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = 5
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "transfer type is not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc25(self):
        """TEST PARA LOS CASOS NO VÁLIDOS TYPE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2049"
        type_to_test = "URGE"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "transfer type is not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc26(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "almendra"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc27(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30112049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc28(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "32/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc29(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "00/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc30(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/00/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc31(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/13/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc32(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2051"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc33(self):
        """TEST PARA LOS CASOS NO VÁLIDOS DATE"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10.01
        date_to_test = "30/11/2024"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "date not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc34(self):
        """TEST PARA LOS CASOS NO VÁLIDOS AMOUNT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = "Dinero"
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "amount not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc35(self):
        """TEST PARA LOS CASOS NO VÁLIDOS AMOUNT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 10000.01
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "amount not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc36(self):
        """TEST PARA LOS CASOS NO VÁLIDOS AMOUNT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 9.99
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "amount not valid")

    @freeze_time("2024-03-22")
    def test_transfer_request_tc36(self):
        """TEST PARA LOS CASOS NO VÁLIDOS AMOUNT"""
        my_manager = AccountManager()
        from_iban_to_test = "ES6036390983922098113875"
        to_iban_to_test = "ES9121000418450200051332"
        concept_to_test = "Transferir dinero"
        amount_to_test = 9.575
        date_to_test = "30/11/2049"
        type_to_test = "ORDINARY"
        with self.assertRaises(Exception) as context:
            my_manager.transfer_request(from_iban=from_iban_to_test, to_iban=to_iban_to_test,
                                        concept=concept_to_test, amount=amount_to_test,
                                        date=date_to_test, transfer_type=type_to_test)

        self.assertEqual(str(context.exception), "amount not valid")



if __name__ == '__main__':
    unittest.main()
