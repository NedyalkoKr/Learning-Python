class Employee:
    pass

# class instances

employee1 = Employee()
employee2 = Employee()

# creating instance attributes on a instance
# this way will work BUT
# we have created a just 2 instances, but what if we need to create more like 1000
# following this approuch we will have to write the same code a lot
# and if we need to add method to all instances
# manual approuch like this will not work
# after all writing OOP is all about following the DRY and code reusability

employee1.first_name = "Ivan"
employee1.last_name = "Ivanov"
employee1.email = "ivan@gmail.com"
employee1.pay = 50000

employee2.first_name = "Petko"
employee2.last_name = "Petkov"
employee2.email = "petkov@gmail.com"
employee2.pay = 60000