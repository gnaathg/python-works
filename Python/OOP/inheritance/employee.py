class Person :

    name : str

    age : int

    gender: str

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display(self):    

        print(self.name,self.age,self.gender)


class Employee(Person):

    eid:int

    department:str

    salary:int

    def __init__(self, name, age, gender,eid,department,salary):

        super().__init__(name, age, gender)

        self.eid=eid

        self.department=department

        self.salary=salary

    def display(self):

        print(self.eid,self.department,self.salary)

        return super().display()   
     
emp_instance = Employee("Sabari",22,"Male","4310277","Data Analytics",45000)

emp_instance.display()