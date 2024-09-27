from faker import Faker


fake = Faker(locale="en")


def fake_email():
    return fake.email()


def fake_password():
    return fake.password()
