from faker import Faker
class RandomGenerator:

    def __init__(self):
        self.randomdata = Faker()

    def random_first_name(self):
        return self.randomdata.first_name()

    def random_last_name(self):
        return self.randomdata.last_name()

    @staticmethod
    def random_email():
        return Faker().email()

    def random_number(self):
        return self.randomdata.phone_number()

    @staticmethod
    def random_password():
        return Faker().password(4, 20)


