from faker import Faker
from datetime import datetime

class RandomInputs:

    def __init__(self):
        self.fake = Faker('ro_RO')

    def random_names(self):
        full_name = self.fake.name()
        fname, lname = full_name.split(' ', 1)
        return fname, lname

    def random_address(self):
        random_address = self.fake.address()
        return random_address

    def random_city(self):
        random_city = self.fake.city()
        return random_city

    def random_postcode(self):
        random_postalcode = self.fake.postcode()
        return random_postalcode

    def random_phone_no(self):
        random_phone = self.fake.phone_number()
        return random_phone

    def time_of_testing(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    def random_shop_name(self):
        random_shop = self.fake.company()
        return random_shop

    def random_age(self):
        random_age = self.fake.random_number(2)
        return random_age

    def random_salary(self):
        random_salary = self.fake.random_number(4)
        return  random_salary

    def random_depart_name(self):
        random_depart = self.fake.job()
        return random_depart




