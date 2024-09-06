class Bike :

    name:str
    price:int
    brand:str


    def __init__(self,name,price,brand):

        self.name=name
        self.price=price
        self.brand=brand


    def display_bike(self):

        print(self.name,self.price,self.brand)

    def __str__(self):

        return self.brand
    

class ShowRoom:

    name:str 
    place:str
    bikes:list


    