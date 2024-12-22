class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        self.new_radius = new_radius
        self.radius = self.new_radius
obj = Circle(10)
print(obj.get_radius())
obj.set_radius(100)
print(obj.get_radius())