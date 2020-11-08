class Cat:
    def __init__(self, new_name, new_age):
        # print('haha1')
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return '%s的年龄是：%d'%(self.name, self.age)

    def eat(self):
        print("%s在吃……"%(self.name))

    def drink(self):
        print("%s在喝水……"%(self.name))

    def intrudus(self):
        print('%s现在%d岁'%(self.name, self.age))


tom = Cat('汤姆', 16)
# tom.intrudus()
print(tom)

print('___________________________________________')

lanMao = Cat('蓝猫', 20)
# lanMao.intrudus()
print(lanMao)