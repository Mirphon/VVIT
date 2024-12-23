class Vehicle():
    def __init__(self,make, model):
        self.make =make
        self.model = model
    def get_info(self):
        return (self.make, self.model)

obj = Vehicle('ww', 'tt')
print(obj.get_info())

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return (self.make, self.model, self.fuel_type)
obj1 = Car('ff', 'ee', '12')
print(obj1.get_info())
