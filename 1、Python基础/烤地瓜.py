class SweetPotato:
    def __init__(self):
        self.cookedstring = '生'
        self.cookedlevl = 0
        self.condiments = []

    def __str__(self):
        return '地瓜是%s的,熟度是:%d,添加的佐料有：%s'%(self.cookedstring, self.cookedlevl, self.condiments)

    def cook(self, cooked_time):
        self.cookedlevl += cooked_time
        if self.cookedlevl >= 0 and self.cookedlevl < 3:
            self.cookedstring = '生'
        elif self.cookedlevl >= 3 and self.cookedlevl < 6:
            self.cookedstring = '半生不熟'
        elif self.cookedlevl >= 6 and self.cookedlevl < 9:
            self.cookedstring = '熟了'
        else:
            self.cookedstring = '烤糊了'

    def addCondiments(self, condiment):
        self.condiments.append(condiment)


digua = SweetPotato()
digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments('大蒜')

print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments('洋葱')
print(digua)
digua.cook(1)
digua.addCondiments('酱油')
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments('孜然')
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
digua.addCondiments('烧烤酱')
print(digua)