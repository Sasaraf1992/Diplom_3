from faker import Faker

fake = Faker()


class StellarBurgerTestData:
    FAKE_USER = {"email": fake.email(),
                 "password": fake.password(),
                 "name": fake.user_name()
                 }