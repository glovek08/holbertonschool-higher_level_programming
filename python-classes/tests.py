
class Car:
    def __init__(self, color: str="", brand: str="", year: int=None):
        self.color = color
        self.brand = brand
        self.year = year
    
    def setColor(self, color: str):
        try:
            self.color = color
        except Exception as error:
            print(error)
    def setBrand(self, brand: str):
        try:
            self.brand = brand
        except Exception as error:
            print(error)
    
    def setYear(self, year: int):
        try:
            self.year = year
        except Exception as error:
            print(error)

    def getInfo(self):
        return [self.color, self.brand, self.year]

    def printInfo(self):
        print(f"Car color: {self.getInfo()[0]}")
        print(f"Car brand: {self.getInfo()[1]}")
        print(f"Car year: {self.getInfo()[2]}")

car1 = Car("#ffffff", "Chevrolet", 2024)
car1.printInfo()
car1.setBrand("Toyota")
print("----- CAR 1 -----")
car1.printInfo()
print("----- CAR 2 -----")
car2 = Car(car1.getInfo()[0], car1.getInfo()[1], car1.getInfo()[2])
car2.setColor("#ff2342")
car2.printInfo()