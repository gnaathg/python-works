class Editor:

    name:str

    vendor:str


    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    
    def open(self):

        print(f"{self.name}open")

    def execute(self):

        print(f"{self.execute}execute")

class Vscode(Editor):

    def __init__(self, name, vendor):

        super().__init__(name, vendor)

class Pycharm(Editor):

    def __init__(self, name, vendor):

        super().__init__(name, vendor)

vsc_instance = Vscode("visualstudiocode","vscvendor")

vsc_instance.open()

pyc_instance = Pycharm("pycharm","jetbrains")

pyc_instance.open()



