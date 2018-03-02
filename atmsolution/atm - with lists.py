class ATM():
    def __init__(self,balance,bankname):
        self.balance = balance
        self.bankname=bankname
        self.withdrawals_list = []


    def draw_money(self,request):
        print "="*30 +"\nWelcome To " + self.bankname + "\n" + "="*30
        if request > self.balance :
            print "Low Account Credit"
        else:
            print "Current Balance is:" + str(self.balance)
            self.balance-=request
            self.withdrawals_list.append(request)
            while request>0 :
                if request >= 100:
                    print "give 100"
                    request = request -100
                elif request>=50:
                    print "give 50"
                    request -= 50
                elif request >= 10:
                    print "give 10"
                    request -= 10
                elif request >= 5:
                    print "give 5"
                    request -= 5
                else:
                    print "give 1"
                    request -= 1
            print "Balance after withdraw is:" + str(self.balance)

    def show_withdraws(self):
        print "The withdraws done on this atm are as following:\n" + str(self.withdrawals_list)
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1,"Smart Bank")
atm2 = ATM(balance2,"Baraka Bank")

atm1.draw_money(300)
atm1.draw_money(150)
atm1.show_withdraws()
