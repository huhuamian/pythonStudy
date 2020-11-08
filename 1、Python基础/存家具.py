class Home:
    def __init__(self, new_area, new_info, new_adress):
        self.area = new_area
        self.info = new_info
        self.adress = new_adress
        self.useArea = new_area
        self.furnitures = []

    def __str__(self):
        # pass
        msg = '我有一座房子，面积是：%d平米，户型是：%s是，面朝：%s,'%(self.area, self.info, self.adress)
        msg += '当前可用面积为：%s,当前家具有:%s'%(self.useArea, str(self.furnitures))
        return msg

    def addFurniture(self, FurnitureItem):
        self.furnitures.append(FurnitureItem.getFurntureNmae())
        self.useArea -= FurnitureItem.getFurntureArea()



class Furniture:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "家具%s占用的面积为：%d平方米"%(self.name, self.area)

    def getFurntureNmae(self):
        return self.name

    def getFurntureArea(self):
        return self.area


bed = Furniture('床', 4)
print(bed)
yingerbed = Furniture('婴儿床', 2)
print(yingerbed)

fangzi = Home(new_info='四室两厅两卫', new_area=200, new_adress='大海')
fangzi.addFurniture(bed)
fangzi.addFurniture(yingerbed)
print(fangzi)