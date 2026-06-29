from datetime import datetime
import time
class Person:
    def __init__(self, name, birth_year, age):
        self.name = name
        self.birth_year = birth_year
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, birth_year={self.birth_year}, age={self.age})"
        
    def display_info(self):
        print("--- Person Information ---")
        time.sleep(1.2)
        print(f"Name: {self.name}")
        time.sleep(1.2)
        print(f"Birth Year: {self.birth_year}")
        time.sleep(1.2)
        print(f"Age: {self.age}")

    @classmethod
    def from_birth_year(cls, name, birth_year, *args, **kwargs):
        current_year = datetime.now().year
        calculated_age = current_year - birth_year
        return cls(name, birth_year, calculated_age, *args, **kwargs)
    @staticmethod
    def greet(name):
        return f"Hello, {name} "
    
class Man(Person):
    def __init__(self, name, birth_year, age, gender="male"):
        super().__init__(name, birth_year, age)
        self.gender = gender
        
    def display_info(self):
        super().display_info()
        time.sleep(1.2)
        print(f"Gender: {self.gender.capitalize()}")

class Woman(Person):
    def __init__(self, name, birth_year, age, gender="female"):
        super().__init__(name, birth_year, age)
        self.gender = gender
        
    def display_info(self):
        super().display_info()
        time.sleep(1.2)
        print(f"Gender: {self.gender.capitalize()}")

# --- User Input & Execution ---

user_name = input("Enter name: ")
user_birth_year = int(input("Enter birth year: "))
user_gender = input("Enter gender (male/female): ").strip().lower()

print("-" * 30)

if user_gender == "male":
    person_obj = Man.from_birth_year(user_name, user_birth_year)
elif user_gender == "female":
    person_obj = Woman.from_birth_year(user_name, user_birth_year)
else:
    person_obj = Person.from_birth_year(user_name, user_birth_year)

person_obj.display_info()
time.sleep(1.5)
print("=" * 30)
print("Saving your information...")
print("=" * 30)
time.sleep(1.5)
greeting = Person.greet(person_obj.name)
print(greeting)
