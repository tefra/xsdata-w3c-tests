from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


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
    COMMERCIAL_AT = "@"
    DOLLAR_SIGN = "$"
    PERCENT_SIGN = "%"
    CIRCUMFLEX_ACCENT = "^"
    ASTERISK = "*"
    LEFT_PARENTHESIS = "("
    RIGHT_PARENTHESIS = ")"
    LOW_LINE = "_"
    HYPHEN_MINUS = "-"
    PLUS_SIGN = "+"
    FULL_STOP_FULL_STOP = ".."
    FULL_STOP = "."
    TILDE = "~"
    EXCLAMATION_MARK = "!"


@dataclass
class Bar:
    class Meta:
        name = "bar"

    value: Optional[St] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    bar: list[Bar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
