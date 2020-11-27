from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class St(Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    I = "i"
    J = "j"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    S = "s"
    T = "t"
    U = "u"
    V = "v"
    W = "w"
    X = "x"
    Y = "y"
    Z = "z"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE = "@"
    VALUE_10 = "$"
    VALUE_11 = "%"
    VALUE_12 = "^"
    VALUE_13 = "*"
    VALUE_14 = "("
    VALUE_15 = ")"
    VALUE_16 = "_"
    VALUE_17 = "-"
    VALUE_18 = "+"
    VALUE_19 = ".."
    VALUE_20 = "."
    VALUE_21 = "~"
    VALUE_22 = "!"


@dataclass
class Bar:
    class Meta:
        name = "bar"

    value: Optional[St] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    bar: List[St] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )
