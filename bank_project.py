class bank:
    bname='SBI'
    ROI=0.09
    def __init__(self,name,mbn,accn,bal,pin):
        self.name=name
        self.mbn=mbn
        self.accn=accn
        self.bal=bal
        self.pin=pin
    @classmethod
    def  changeROI(cls,n):
        cls.ROI=n
    def withdraw(self):
        if self.pin==self.getpin():
            amt=int(input('enter amount:'))
            if self.bal>=amt:
                self.bal-=amt
                print('amount debited sucessfully')
            else:
                print('insufficient balence')
        else:
            print('incorrect pin')
    
    def checkbalence(self):
        if self.pin==self.getpin():
            print(f'{self.name} current balence is {self.bal}')
        else:
            print('incorrect pin')
    @staticmethod
    def getpin():
        return int(input('get pin:'))
ob1=bank('vinay',9133119385,8946234724779832749,50000,9133)
ob1.checkbalence()
ob1.withdraw()             
