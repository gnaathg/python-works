class Mobile:

    name:str
    display:str
    price:int
    brand:str


    def __init__(self,name,display,price,brand):

        self.name=name
        self.display=display
        self.price=price
        self.brand=brand


    def display_mobile(self):

        print(self.name,self.display,self.price,self.brand)


mobile_reference = Mobile("Phone 1","Amoled","16000","CMF by Nothing")

mobile_reference.display_mobile()