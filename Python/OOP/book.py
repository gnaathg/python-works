class Book:

    name:str
    pages:int
    price:int
    author:str
    language:str


    def __init__(self,name,pages,price,author,language): #initializng instance variable

        self.name=name
        self.pages=pages
        self.price=price
        self.author=author
        self.language=language



    def display_book(self):

        print(self.name,self.pages,self.price,self.author,self.language)

    def __str__(self): #representation of string in the object

        return self.name 


book_instance = Book("The Subtle Art Of Not Giving A Fuck \n",200 ,500,"\nMark Manson\n","English\n")

book_instance.display_book()

print(book_instance)

