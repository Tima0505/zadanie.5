import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Создаём тестовые счета перед каждым тестом"""
        self.account1 = BankAccount("Иван Иванов", "ACC001")
        self.account2 = BankAccount("Пётр Петров", "ACC002")


    def test_create_account(self):
        self.assertEqual(self.account1.owner, "Иван Иванов")
        self.assertEqual(self.account1.account_number, "ACC001")
        self.assertEqual(self.account1.balance, 0)

    def test_create_account_invalid_owner(self):
        with self.assertRaises(ValueError):
            BankAccount("", "ACC001")
        with self.assertRaises(ValueError):
            BankAccount(None, "ACC001")

    def test_create_account_invalid_number(self):
        with self.assertRaises(ValueError):
            BankAccount("Иван", "")


    def test_deposit(self):
        self.account1.deposit(1000)
        self.assertEqual(self.account1.get_balance(), 1000)

    def test_deposit_multiple(self):
        self.account1.deposit(500)
        self.account1.deposit(300)
        self.assertEqual(self.account1.get_balance(), 800)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(-100)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account1.deposit(0)


    def test_withdraw(self):
        self.account1.deposit(1000)
        self.account1.withdraw(400)
        self.assertEqual(self.account1.get_balance(), 600)

    def test_withdraw_insufficient_funds(self):
        self.account1.deposit(100)
        with self.assertRaises(ValueError):
            self.account1.withdraw(200)

    def test_withdraw_negative(self):
        self.account1.deposit(500)
        with self.assertRaises(ValueError):
            self.account1.withdraw(-50)

    def test_withdraw_zero(self):
        self.account1.deposit(500)
        with self.assertRaises(ValueError):
            self.account1.withdraw(0)


    def test_transfer(self):
        self.account1.deposit(1000)
        self.account1.transfer(self.account2, 300)
        
        self.assertEqual(self.account1.get_balance(), 700)
        self.assertEqual(self.account2.get_balance(), 300)

    def test_transfer_insufficient_funds(self):
        self.account1.deposit(100)
        with self.assertRaises(ValueError):
            self.account1.transfer(self.account2, 200)
        

        self.assertEqual(self.account1.get_balance(), 100)
        self.assertEqual(self.account2.get_balance(), 0)

    def test_transfer_to_same_account(self):
        self.account1.deposit(500)
        with self.assertRaises(ValueError):
            self.account1.transfer(self.account1, 100)


    def test_get_balance(self):
        self.assertEqual(self.account1.get_balance(), 0)
        self.account1.deposit(250.5)
        self.assertEqual(self.account1.get_balance(), 250.5)


    def test_is_empty_true(self):
        self.assertTrue(self.account1.is_empty())

    def test_is_empty_false(self):
        self.account1.deposit(100)
        self.assertFalse(self.account1.is_empty())

    def test_is_empty_after_operations(self):
        self.account1.deposit(500)
        self.account1.withdraw(500)
        self.assertTrue(self.account1.is_empty())


if __name__ == "__main__":
    unittest.main()