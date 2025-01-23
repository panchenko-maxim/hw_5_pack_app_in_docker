from faker import Faker

fake = Faker()


def get_name_address() -> tuple:
    return fake.name(), fake.address()
