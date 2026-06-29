import time
class Member:
    users_num = 0
    def __init__(self):
        self.fname = ""
        self.Mname = ""
        self.Lname = ""
        self.gender = ""

    def get_full_info(self):
        input_name = input("Enter your full name: ")
        name_parts = input_name.split()
        self.fname = name_parts[0] if len(name_parts) > 0 else ""
        self.Mname = name_parts[1] if len(name_parts) > 1 else ""
        self.Lname = name_parts[2] if len(name_parts) > 2 else ""
        self.gender = input("Enter your gender (male/female): ").strip().lower()
        Member.users_num += 1

    def display_info(self):
        print(f"First Name: {self.fname.capitalize()}, Middle Name: {self.Mname.capitalize()}, Last Name: {self.Lname.capitalize()}")

    def name_with_title(self):
        if self.gender == "male":
            return f"Hello Mr. {self.fname.capitalize()}!"
        elif self.gender == "female":
            return f"Hello Ms. {self.fname.capitalize()}!"
        else:
            return f"Hello {self.fname.capitalize()}!"
        
member1 = Member()
member1.get_full_info()
time.sleep(1)
print('loading...')
time.sleep(1)
member1.display_info()
print(member1.name_with_title())