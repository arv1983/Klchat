from faker import Faker
import faker
import random


class GeratorData:
    @staticmethod
    def create_client_cpf() -> dict:
        faker = Faker("pt_BR")
        data = dict(
            tipo_usuario="cliente",
            nome=faker.name(),
            email=faker.email(),
            senha="1234",
            cpf=faker.cpf(),
            telefone=faker.cellphone_number()[4:-1],
        )

        return data

    @staticmethod
    def create_client_cnpj() -> dict:
        faker = Faker("pt_BR")
        data = dict(
            tipo_usuario="cliente",
            nome=faker.name(),
            email=faker.email(),
            senha="1234",
            cnpj=GeratorData.generate_cnpj(),
            telefone=faker.cellphone_number()[4:-1],
        )
        return data

    @staticmethod
    def create_lojista() -> dict:
        faker = Faker("pt_BR")
        data = dict(
            tipo_usuario="lojista",
            nome=faker.name(),
            email=faker.email(),
            senha="1234",
            cnpj=GeratorData.generate_cnpj(),
            telefone=faker.cellphone_number()[4:-1],
        )

        return data

    @staticmethod
    def generate_cnpj():
        def calculate_special_digit(l):
            digit = 0

            for i, v in enumerate(l):
                digit += v * (i % 8 + 2)

            digit = 11 - digit % 11

            return digit if digit < 10 else 0

        cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

        for _ in range(2):
            cnpj = [calculate_special_digit(cnpj)] + cnpj

        return "%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s" % tuple(cnpj[::-1])
