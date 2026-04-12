class car():
    
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fule_type = fuel_type
        self.__speed = 0
        self.is_start = False
        
        
    def start_engine(self):
        if self.is_start == True:
            # print("Car is allready Start.")
            return True
        else:
            self.is_start = True
            # print("Car is Start.")
            return True
    
      
    def accelerate_car(self,increase):
        if self.is_start == False:
            # print("Error: Start Car first.")
            return False
        
        self.__speed = self.__speed + increase
        
        if self.__speed >= 180:
            self.__speed = 180
        else:
            pass# print(f"Speed of car {self.__speed}")
        return True

    def car_break(self):
        if self.__speed > 0:
            self.__speed = 0
            # print("Break apply (Car Stopped.)")
        else:
            # print("Car stopped already.")
            pass
        
        return True
    
    def car_details(self):
        status = "ON" if self.is_start is True else "OFF"
        return f'''
    ===CAR DETIAILS==
    Car Brand : {self.brand}
    Car Model : {self.model}
    Car Fuel_Type : {self.fule_type}
    Car Star or Not : {status}
    Car Speed : {self.__speed} km/h
    '''
    
        

    
car1 = car("BMW","BMW 43","Desiol")
car2 = car("Audi","AUDI 54", "Elsctric")

car1.start_engine()
car1.accelerate_car(54)

car2.start_engine()
car2.accelerate_car(534)

print(car1.car_details())
print(car2.car_details())