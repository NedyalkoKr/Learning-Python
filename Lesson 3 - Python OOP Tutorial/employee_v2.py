class Employee:
    
    def __init__(self, first_name, last_name, email, salary):
        # self is the name used by convention to refer to
        # the instance that this method is called on
        # class methods needs to know on which instance they are called
        
        # these are called instance attributes
        # and each and every instance will have access to them
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
        
        # adding behaviour to instances using methods
        # method is a callable instance attribute
        
    def full_name(self):
        _full_name = f'{self.first_name} {self.last_name}'
        return _full_name
        

# we dont have to pass self when we creating(constructing) instance
# instance will be pass automaticaly by PY
employee1 = Employee("Ivan", "Ivanov", "ivan@gmail.com", 50000)
employee2 = Employee("Petko", "Petkanov", "petko@gmail.com", 60000)
employee3 = Employee(first_name="Maria", last_name="Ivanova", email="maria@gmail.com", salary=70000)

print(employee1.first_name)
print(employee2.first_name)
print(employee3.first_name)

# calling a method on each instance we have created

print(employee1.full_name())
print(employee2.full_name())
print(employee3.full_name())

# calling a method on a instance is equivalent to this
# but we have to expliclty pass the instance

print(Employee.full_name(employee1))