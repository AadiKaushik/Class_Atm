
class atm():
    def __init__(self,cardNo,pinNo):
        self.cardNo = cardNo
        self.pinNO = pinNo



    def CashWithdrawl(self):
        print('Cash Withdrawed')

    def BankEnquiry(self):
        print('Your Account has 1500 rupees')


user = atm(1234,1234)
user.BankEnquiry()
