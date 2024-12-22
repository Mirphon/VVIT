class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return self.name, self.id

class Manager(Employee):
    def __init__(self, name='', id='', departament=''):
        self.departament = departament
        super().__init__(name, id)
    def manage_project(self, name_project):
        self.name_project = name_project
        print(f'Проект {self.name_project} создан!')

class Technician(Employee):
    def __init__(self, name='', id='', specialization=''):
        self.specialization = specialization
        super().__init__(name, id)

    def perform_maintenance(self, object_name):
        self.object_name = object_name
        print(f'Техническое обслуживание {self.object_name}а завершено!')

class TechManager(Technician, Manager):
    name_list = []
    def __init__(self,  name, id,specialization, departament):
        super().__init__(name, id, specialization)
        super().__init__(name, id, departament)
    @classmethod
    def add_employee(cls, name):
        cls.name = name
        TechManager.name_list.append(cls.name)
    @classmethod
    def get_team_info(cls):
        return cls.name_list
j = TechManager('Mischa', 52, 6, 'ilov')
user = TechManager(1,2,3,4)
TechManager.add_employee(j.name)
TechManager.add_employee(user.name)
print(TechManager.get_team_info())



