from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A000:
    :cvar A0_4:
    :cvar A0_A9:
    :cvar A10:
    :cvar A1:
    :cvar A1_A:
    :cvar A20:
    :cvar A2:
    :cvar A2_A:
    :cvar A30:
    :cvar A3:
    :cvar A3_A:
    :cvar A40:
    :cvar A4:
    :cvar A4_A:
    :cvar A50:
    :cvar A5:
    :cvar A5_A:
    :cvar A60:
    :cvar A6:
    :cvar A6_A:
    :cvar A70:
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    :cvar A9:
    :cvar A9_A:
    """
    A000 = "a000"
    A0_4 = "a0-4"
    A0_A9 = "a0A9"
    A10 = "a10٠"
    A1 = "a1-٤"
    A1_A = "a1A٩"
    A20 = "a20۰"
    A2 = "a2-۴"
    A2_A = "a2A۹"
    A30 = "a30०"
    A3 = "a3-४"
    A3_A = "a3A९"
    A40 = "a40০"
    A4 = "a4-৪"
    A4_A = "a4A৯"
    A50 = "a50੦"
    A5 = "a5-੪"
    A5_A = "a5A੯"
    A60 = "a60૦"
    A6 = "a6-૪"
    A6_A = "a6A૯"
    A70 = "a70୦"
    A7 = "a7-୪"
    A7_A = "a7A୯"
    A80 = "a80௧"
    A8 = "a8-௫"
    A8_A = "a8A௯"
    A90 = "a90౦"
    A9 = "a9-౪"
    A9_A = "a9A౯"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
