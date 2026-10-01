class myClass:
    
    __privateVar = 30
    def __privMeth(self):
        print("This is a private method")
    def hello(self):
        print("Accessing private variable:", self.__privateVar)
    
foo = myClass()
foo.hello()
foo._myClass__privMeth()
