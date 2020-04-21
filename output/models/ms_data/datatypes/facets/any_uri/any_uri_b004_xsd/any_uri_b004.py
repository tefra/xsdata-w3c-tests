from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class St(Enum):
    """
    :cvar II_EI:
    :cvar II_QI:
    :cvar II_UI:
    :cvar IIGI:
    :cvar IIKI:
    :cvar IIOI:
    :cvar IISI:
    :cvar II0I:
    :cvar II4I:
    :cvar II4U_IG:
    :cvar IJ_EI:
    :cvar IJ_II:
    :cvar IJ_MI:
    :cvar IJ_QI:
    :cvar IJ_UI:
    :cvar IJ_YI:
    :cvar IJCI:
    :cvar IJGI:
    :cvar IJKI:
    :cvar IK_AI:
    :cvar IL4I:
    :cvar IL8I:
    :cvar IM_EI:
    :cvar IM_II:
    :cvar IM_MI:
    :cvar IM_QI:
    :cvar IM_UI:
    :cvar IM_YI:
    :cvar IMCI:
    :cvar IMGI:
    :cvar IMKI:
    :cvar IMOI:
    :cvar IMSI:
    :cvar IMWI:
    :cvar IM0I:
    :cvar IM4I:
    :cvar IM8I:
    :cvar IN_AI:
    :cvar IN_EI:
    :cvar IN_II:
    :cvar IN_MI:
    :cvar IN_QI:
    :cvar IN_UI:
    :cvar IN_YI:
    :cvar INCI:
    :cvar INGI:
    :cvar INKI:
    :cvar INOI:
    :cvar IN4I:
    """
    II_EI = "!"
    II_QI = "$"
    II_UI = "%"
    IIGI = "("
    IIKI = ")"
    IIOI = "*"
    IISI = "+"
    II0I = "-"
    II4I = "."
    II4U_IG = ".."
    IJ_EI = "1"
    IJ_II = "2"
    IJ_MI = "3"
    IJ_QI = "4"
    IJ_UI = "5"
    IJ_YI = "6"
    IJCI = "7"
    IJGI = "8"
    IJKI = "9"
    IK_AI = "@"
    IL4I = "^"
    IL8I = "_"
    IM_EI = "a"
    IM_II = "b"
    IM_MI = "c"
    IM_QI = "d"
    IM_UI = "e"
    IM_YI = "f"
    IMCI = "g"
    IMGI = "h"
    IMKI = "i"
    IMOI = "j"
    IMSI = "k"
    IMWI = "l"
    IM0I = "m"
    IM4I = "n"
    IM8I = "o"
    IN_AI = "p"
    IN_EI = "q"
    IN_II = "r"
    IN_MI = "s"
    IN_QI = "t"
    IN_UI = "u"
    IN_YI = "v"
    INCI = "w"
    INGI = "x"
    INKI = "y"
    INOI = "z"
    IN4I = "~"


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
