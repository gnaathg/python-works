class Vehicle:

    def start(self):

        print("vehicle start method")

    def accelerate(self):

        print("vehicle accelerate method")

class Thar(Vehicle):

    pass

thar_instance = Thar()

thar_instance.start()

thar_instance.accelerate()