import datetime

passTransaction = "SUCCESS!"
failTransaction = "FAILED!"

class User:
    def __init__(self, n, c, a, cur) -> None:
        self.__name = n
        self.__card =  c
        self.__amount = a
        self.__currency = cur
    
    def get_name(self):
        return self.__name
    
    def get_currency(self):
        return self.__currency

    def add_money(self, value):
        self.__amount += value

    def get_money(self, value):
        if value >= self.__amount:
            return False
        self.__amount -= value
        return True
    
    def __str__(self) -> str:
        return f'''
        CARD INFO:
        HOLDER: {self.__name}
        CARD NUMBER: {self.__card}
        AMOUNT: {self.__amount} {self.__currency}
        '''

class Transaction():
    def __init__(self) -> None:
        self.__sender = ""
        self.__receiver = ""
        self.__amount = float()
        self.__transfer_rate = {
            "USD":0, 
            "RUB":0
            }
        self.__status = bool
    
    def set_transfer_rates(self, usd, rub):
        self.__transfer_rate["USD"] = usd
        self.__transfer_rate["RUB"] = rub

    def make_transaction(self, sender: User, receiver: User, g_amount):
        self.g_amount1 = g_amount
        self.g_amount2 = g_amount
        self.g_amount = g_amount
        self.__sender = sender
        self.__receiver = receiver
        self.__senderr = sender
        self.__receiverr = receiver
        self.__transfer_money()

    def __get_current_datatime(self):
        return datetime.datetime.now()
    
    def __transfer_money(self):
        if self.__sender.get_currency() == 'USD':
            self.g_amount1 /= self.__transfer_rate['USD']
            if self.__sender.get_money(self.g_amount1):
                if self.__receiver.get_currency() == 'USD':
                    self.__receiver.add_money(self.g_amount1)
                else:
                    self.g_amount2 /= self.__transfer_rate['RUB']
                    self.__receiver.add_money(self.g_amount2)
                self.__status == True
            else: 
                print("Sender does not have enough money!")
                self.__status = False
        else:
            if self.__sender.get_money(self.g_amount1):
                self.g_amount1 /= self.__transfer_rate['RUB']
                self.__sender.get_money(self.g_amount1)
                if self.__receiver.get_currency() == 'RUB':
                    self.__receiver.add_money(self.g_amount1)
                else:
                    self.g_amount2 /= self.__transfer_rate['USD']
                    self.__receiver.add_money(self.g_amount2)
                self.__status == True
            else:
                print("Sender does not have enough money!")
                self.__status = False

    def __str__(self) -> str:
        return f'''
            TRANSACTION
            SENDER: {self.__senderr.get_name()} {self.__senderr.get_currency()}
            RECEIVER: {self.__receiverr.get_name()} {self.__receiverr.get_currency()}
            MOUNT: {self.g_amount}. TRANSFER TIMESTAMP: {self.__get_current_datatime()}
            STATUS: {passTransaction if self.__status else failTransaction}
            '''
    
u1 = User("Shahroz Gulliyev", "1234 4567 7890 1357", 567.9, "USD")
u2 = User("Ramz Gulliyev", "3873 1823 0293 0606", 3847.1, "RUB")

print(u1)
print(u2)

tr1 = Transaction()
tr1.set_transfer_rates(11340, 147.17)

tr1.make_transaction(u1, u2, 500000)
print(tr1)

print(u1)
print(u2)