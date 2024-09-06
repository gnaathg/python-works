class Dishes:

    name:str
    price:int
    cuisine:str
    qty:str

    def __init__(self,name,price,cuisine,qty):

        self.name=name
        self.price=price
        self.cuisine=cuisine
        self.qty=qty

    def diaplay_dishes(self):

        print(self.name,self.price,self.cuisine,self.qty)

    def __str__(self):

        return self.cuisine
    
class Restaurant:

    name:str
    place:str
    rating:str
    dishes:list

    def __init__(self,name,place,rating):

        self.name=name
        self.place=place
        self.rating=rating
        self.dishes=[]

    def add_dishes(self,dish):

        self.dishes.append(dish)


    def list_dishes(self):

        for d in self.dishes:

            print(d)


biriyani_instance=Dishes("Biriyani",130,"Indian","Full")

mandhi_instance=Dishes("Mandhi",190,"Arabic","Full")

fried_rice=Dishes("Fried_rice",150,"Malaysian","Half")

