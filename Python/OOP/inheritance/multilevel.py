class GrandParent:

    def m1(self):

        print("Grandparent m1 method")

class Parent(GrandParent):

    def m2(self):

        print("parent class m2 method")

class Child(Parent):

    def m3(self):

        print("Child m3 method")

child_instance = Child()

child_instance.m1()

child_instance.m2()

child_instance.m3()