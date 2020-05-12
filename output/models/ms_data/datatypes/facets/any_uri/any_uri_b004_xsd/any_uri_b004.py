from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class St(Enum):
    """
    :cvar A:
    :cvar B:
    :cvar C:
    :cvar D:
    :cvar E:
    :cvar F:
    :cvar G:
    :cvar H:
    :cvar I:
    :cvar J:
    :cvar K:
    :cvar L:
    :cvar M:
    :cvar N:
    :cvar O:
    :cvar P:
    :cvar Q:
    :cvar R:
    :cvar S:
    :cvar T:
    :cvar U:
    :cvar V:
    :cvar W:
    :cvar X:
    :cvar Y:
    :cvar Z:
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    :cvar VALUE:
    :cvar VALUE_10:
    :cvar VALUE_11:
    :cvar VALUE_12:
    :cvar VALUE_13:
    :cvar VALUE_14:
    :cvar VALUE_15:
    :cvar VALUE_16:
    :cvar VALUE_17:
    :cvar VALUE_18:
    :cvar VALUE_19:
    :cvar VALUE_20:
    :cvar VALUE_21:
    :cvar VALUE_22:
    """
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
    """
    :ivar value:
    """
    class Meta:
        name = "bar"

    value: Optional[St] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar bar:
    """
    class Meta:
        name = "root"

    bar: List[Bar] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=100
        )
    )
