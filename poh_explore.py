from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import jsonpickle  # json encoder doesn't encode dataclasses nicely, jsonpickle does the trick
from icecream import ic

# input("How is your Pursuit of Happiness")
# input("Inner Peace, Passion , Compassion")
# input("Inner Peace, Caring, Compassion")

# Update pickler for enums to be more pretty for JSON
# https://stackoverflow.com/questions/49963305/how-to-deal-with-a-single-value-when-implementing-jsonpickle-custom-handlers
class EnumPrettyPickle(Enum):
    def __getstate__(self):
        return self.name

class eCategory(EnumPrettyPickle):
    INNER_PEACE = "INNER_PEACE"
    COMPASSION = "COMPASSION"
    PASSION = "PASSION"


class eTarget(EnumPrettyPickle):
    SELF = "SELF"
    OTHER = "OTHER"
    PROCESS = "PROCESS"


# XXX: Is Self a Person?
# Can add remove list of people over time.
@dataclass
class Person:
    Name: str


class eTimeframe(EnumPrettyPickle):
    PAST = "PAST"
    PRESENT = "PRESENT"
    FUTURE = "FUTURE"
    def __getstate__(self):
        return self.name


@dataclass
class Timeframe:
    Frame: eTimeframe
    Actual = datetime.now


Person.Self = Person(Name="SELF")


class Process:
    Name: str


LikertScale = type(int)

# Consider Tab Completion:
# https://python-prompt-toolkit.readthedocs.io/en/master/pages/asking_for_input.html#autocompletion


@dataclass
class Passion:
    Strength: LikertScale = 4


class Compassion:
    Strength: LikertScale = 4


class InnerPeace:
    Strength: LikertScale = 4
    Target: eTarget = eTarget.SELF


class Reading:
    Category: eCategory = eCategory.INNER_PEACE
    Timeframe = Timeframe(Frame=eTimeframe.PRESENT)
    Strength: LikertScale = 4
    # One of the following
    Person: Person = None
    Process: Process = None
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
    r = Reading()
    r.Category = eCategory.COMPASSION
    r.Strength = 4
    r.Person = "Tori"
    r.Process = "Spending"
    r.Timeframe = Timeframe(Frame=eTimeframe.PRESENT)
    r.Details = """
    She's mad at me because I'm getting too many low prices things
    """
    return r

def messingUpAtWork():
    r = Reading()
    r.Category = eCategory.INNER_PEACE
    r.Strength = 2
    r.Process = "WRITING"
    r.Timeframe = Timeframe(Frame=eTimeframe.PAST)
    r.Details = """
    Didn't provide enough context in my VP e-mail
    """
    return r


# COOL FEATURE
# Ask or correct as needed with MRU/MFU, etc.
# Use NLP to infer Person, Process, TimeFrame, Category


def pd(o):
    return print(jsonpickle.encode(o, indent=4, unpicklable=False))


def main():
    jsonpickle.set_encoder_options(
        "json",
        ensure_ascii=False,
    )
    pd(toriSpending())
    pd(messingUpAtWork())


main()
