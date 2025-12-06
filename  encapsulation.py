class Computer:
    
    def __init__(self):
        self.__maxprice = 900
        
    
    def sell(self):
        print("Selling Price {}". format (self.__maxprice))
        
    def setMaxprice(self , price):
        self.__maxprice = price
        
        
mycomputer = Computer()
mycomputer.__maxprice = 500
mycomputer.sell()
print()

mycomputer.setMaxprice(500)
mycomputer.sell()