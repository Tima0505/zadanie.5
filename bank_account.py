class BankAccount:
    def __init__(self, owner: str, account_number: str):
        if not owner or not isinstance(owner, str):
            raise ValueError("Имя владельца должно быть непустой строкой")
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Номер счёта должен быть непустой строкой")
        
        self.owner = owner
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        """Пополнение счёта"""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Снятие денежных средств"""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте")
        
        self.balance -= amount

    def transfer(self, other_account: 'BankAccount', amount: float) -> None:
        """Перевод средств на другой счёт"""
        if not isinstance(other_account, BankAccount):
            raise TypeError("Получатель должен быть объектом BankAccount")
        if other_account is self:
            raise ValueError("Нельзя переводить средства на тот же счёт")
        

        self.withdraw(amount)
        try:
            other_account.deposit(amount)
        except Exception:

            self.deposit(amount)
            raise

    def get_balance(self) -> float:
        """Получение текущего баланса"""
        return self.balance

    def is_empty(self) -> bool:
        """Проверка, является ли счёт пустым"""
        return self.balance == 0