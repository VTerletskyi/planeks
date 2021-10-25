from faker import Faker
from random import randrange


def sentence(*, qty: int, string_char: str, separator: str):
    text = f'{string_char}'
    for x in range(qty):
        text += Faker().sentence() + ' '
    text += f'{string_char}'.replace(f'{separator}', '')
    return text


def integer(*, lower: int, upper: int):
    return randrange(lower, upper)


def address():
    return Faker().address().replace('\n', ' ')


column_types = {
    1: Faker().name,
    2: Faker().job,
    3: Faker().email,
    4: Faker().url,
    5: Faker().phone_number,
}
