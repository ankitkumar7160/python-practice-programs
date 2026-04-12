class car():
    
    def __init__(self,brand,model,fule_type,__speed,is_start):
        self.brand = brand
        self.model = model
        self.fule_type = fule_type
        self.__speed = 0
        self.is_start = False
        
        
    def start_engine(self):
        if self.is_start == True:
            print("Car is allready Start.")
            return True
        else:
            self.is_start = True
            print("Car is not Start.")
            return True
    
      
    def accelerate_car(self,increase):
        if self.is_start == False:
            print("Error: Start Car first.")
            return False
        else:
            self.__speed = self.__speed + increase
            print(f"Speed of car {self.__speed}")
            return True

    def car_break(self):
        if self.__speed > 0:
            self.__speed = 0
            print("Break apply (Car Stopped.)")
        else:
            print("Car stopped already.")
        return self.car_break
        

    
car1 = car("BMW","BMW 43","Desiol")

print(car1.accelerate_car(67))