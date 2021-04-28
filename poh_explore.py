from enum import Enum

input("How is your Pursuit of Happiness")
# input("Inner Peace, Passion , Compassion")
input("Inner Peace, Caring, Compassion")

class ePoH(enum):
    INNER_PEACE,
    COMPASSION,
    PASSION

# Alias int to lipert

Lipert = type(int)

@data
class eLippert(enum):
    INNER_PEACE,
    COMPASSION,
    PASSION

@dataclass
class PoH_root:
    PoH: ePoH
    Strength: Lippert




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
