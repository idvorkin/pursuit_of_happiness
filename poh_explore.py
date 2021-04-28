from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import jsonpickle  # json encoder doesn't encode dataclasses nicely, jsonpickle does the trick
from icecream import ic

# input("How is your Pursuit of Happiness")
# input("Inner Peace, Passion , Compassion")
# input("Inner Peace, Caring, Compassion")


class eCategory(Enum):
    INNER_PEACE = "INNER_PEACE"
    COMPASSION = "COMPASSION"
    PASSION = "PASSION"

class eTarget(Enum):
    SELF = "SELF"
    OTHER = "OTHER"
    PROCESS = "PROCESS"


# XXX: Is Self a Person?
# Can add remove list of people over time.
@dataclass
class Person:
    Name:str

class eTimeframe(Enum):
    PAST = "PAST"
    PRESENT = "PRESENT"
    FUTURE = "FUTURE"

@dataclass
class Timeframe:
    Frame:eTimeframe
    Actual = datetime.now


Person.Self = Person(Name="SELF")

class Process:
    Name:str

LikertScale = type(int)


@dataclass
class Passion:
    Strength: LikertScale = 4


class Compassion:
    Strength: LikertScale = 4

class InnerPeace:
    Strength: LikertScale = 4
    Target: eTarget = eTarget.SELF

class Reading:
    Category: eCategory  = eCategory.INNER_PEACE
    Strength: LikertScale = 4
    # One of the following
    Person: Person  = None
    Process: Process = None
    Timeframe =  Timeframe(Frame=eTimeframe.PRESENT)
    ObservedAt = datetime.now()
    Details = ""


@dataclass
class StateOfMind:
    Time: datetime
    InnerPeace: InnerPeace
    Passion: Passion
    Compassion: Compassion


# Trending ...
# Inner Peace - 10
# Passion - 7
# Compassion  - 7

# Quick Entry


# Inner Peace
#   Are you Anxious?
#   Self - Yourself
#   Other - Someone Else
#   Process - How stuff works

#  Compassion
#    Are you caring?
#


# Self

# Others

def toriSpending():
    r =  Reading()
    r.Category = eCategory.COMPASSION
    r.Strength = 4
    r.Person = "Tori"
    r.Process = "Spending"
    r.Details = """
    She's mad at me because I'm getting too many low prices things
    """
    return r



def main():
    jsonpickle.set_encoder_options("json", ensure_ascii=False, )
    print ("Tori Spending")
    print(jsonpickle.encode(toriSpending(), indent=4, unpicklable=False))
    ic(toriSpending())

main()
