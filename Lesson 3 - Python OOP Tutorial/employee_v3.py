class Employee:

    # creating class attribute
    # accessing class attribute will happen via
    # class itself like Employee.raise_amout
    # or as instance attribute
    raise_amount = 1.04
    
    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
    
    def full_name(self):
        _full_name = f'{self.first_name} {self.last_name}'
        return _full_name

    def apply_raise(self):
        # How is possible to access class attribute as a instance attribute?
        # ant not just using raise_amount directly
        
        # PY will try to lookup instance attribute on te instance itself
        self.salary = int(self.salary * self.raise_amount)
        return self.salary

employee1 = Employee("Ivan", "Ivanov", "ivan@gmail.com", 50000)

print(f'Base salary for {employee1.first_name} is: ${employee1.salary}')
print(f'Salary with the raise is: ${employee1.apply_raise()}')