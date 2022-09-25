from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'
    Biology = 'Biology'
    Computer_Science = 'Computer Science'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Dali'
    email: str = 'test@test.test'
    user_number: str = '9999999999'
    birth_day: str = '11'
    birth_month: str = 'April'
    birth_year: str = '2000'
    subjects: Tuple[Subject] = (Subject.Computer_Science, Subject.Biology)
    hobbies: Tuple[Hobby] = (Hobby.Music,)


first_user = User(name='Salvador', gender=Gender.Male)