from enum import Enum
from dataclasses import dataclass
from datetime import datetime

input("How is your Pursuit of Happiness")
# input("Inner Peace, Passion , Compassion")
input("Inner Peace, Caring, Compassion")


class ePoH(Enum):
    INNER_PEACE = "INNER_PEACE"
    COMPASSION = "COMPASSION"
    PASSION = "PASSION"


LikertScale = type(int)


@dataclass
class PoH_root:
    PoH: ePoH
    Strength: LikertScale


@dataclass
class Passion:
    Strength: LikertScale


class Compassion:
    Strength: LikertScale


@dataclass
class StateOfMind:
    Time: datetime
    InnerPeace: PoH_root
    Passion: PoH_root
    Compassion: PoH_root


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


def main():
    pass
