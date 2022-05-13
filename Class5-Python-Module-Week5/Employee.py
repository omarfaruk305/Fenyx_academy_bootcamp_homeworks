"""
* Define the `Employee` class with an `__init__()` method
* Define a class variable `new_id` and set it equal to `1`
* Each Employee instance will need its own unique ID. 
* Thus, inside `__init__()`, define `self.id` and set it equal to the class variable `new_id`
* Lastly, increment `new_id` by `1`
* Define a `say_id()` method
* Inside `say_id()`, output the string `"My id is "` and then the instance id.
* Define the variable e1 and set it to an instance of Employee
* Define the variable e2 and set it to an instance of Employee
* Have both e1 and e2 output their ids
"""
class Employee:
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print(f"my id is {self.id}")
    def say_new_id(self):
        print(self.new_id)
e1 = Employee()
e2 = Employee()



print(Employee.say_new_id(e1))
