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
    Male = 1
    Female = 2
    Other = 3


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
    birth_date: str = '19 Mar 1985'
    subjects: Tuple[Subject] = (Subject.Computer_Science, Subject.Biology)
    hobbies: Tuple[Hobby] = (Hobby.Music,)
    picture_file: str = 'fortest.png'
    state: str = 'Haryana'
    city: str = 'Karnal'
    currentAddress: str = 'Figueres, Catalonia, Spain'



student = User(name='Salvador', gender=Gender.Male)