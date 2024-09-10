from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):

        pass

    @abstractmethod
    def execute(self):

        pass

    @abstractmethod
    def debug(self):

        pass

class VScode(Editor):

    def open(self):
        print("VScode editor opened")

    def execute(self):
        print("VScode editor executed")

    def debug(self):
        print("VScode editor debugged")

editor_instance = VScode()

editor_instance.open()
editor_instance.execute()
editor_instance.debug()