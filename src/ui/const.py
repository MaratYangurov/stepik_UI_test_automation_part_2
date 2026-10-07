from faker import Faker


class Data:
    APPLE = 'apple'
    BREADCRUMB = ['Главная страница', 'Software', 'Brand', 'Apple', 'Ipod Shuffle']
    HTC = 'HTC'


class InputData:

    @staticmethod
    def generator_email():
        fake = Faker()
        username = fake.user_name()
        return f'{username}@mail.com'

    EMAIL = generator_email()
    FIRST_NAME = "Agent"
    LAST_NAME = 'Smith'
    TELEPHONE = '252325235235235'
    PASSWORD = '1234'
    ADDRESS_1 = 'Vice'
    CITY = 'City'
    POST_CODE = '2342523523'