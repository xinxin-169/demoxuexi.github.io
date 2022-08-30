
class Hero:
    game = 'League of legend'

    def flash(self,adname):
        self.adname = adname

    def qaq(self,name):
        self.flash('冲')
        self.name = name
        print(self.adname+"我闪了过去")


ashe = Hero()
ashe.qaq("艾希")




