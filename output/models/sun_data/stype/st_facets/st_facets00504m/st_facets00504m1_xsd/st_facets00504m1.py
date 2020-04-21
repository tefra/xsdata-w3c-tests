from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0_4:
    :cvar A000:
    :cvar A0_A9:
    :cvar A1:
    :cvar A10:
    :cvar A1_A:
    :cvar A2:
    :cvar A20:
    :cvar A2_A:
    :cvar A3:
    :cvar A30:
    :cvar A3_A:
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
    :cvar A5:
    :cvar A50:
    :cvar A5_A:
    :cvar A6:
    :cvar A60:
    :cvar A6_A:
    :cvar A7:
    :cvar A70:
    :cvar A7_A:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A9:
    :cvar A90:
    :cvar A9_A:
    """
    A0_4 = "a0-4"
    A000 = "a000"
    A0_A9 = "a0A9"
    A1 = "a1-٤"
    A10 = "a10٠"
    A1_A = "a1A٩"
    A2 = "a2-۴"
    A20 = "a20۰"
    A2_A = "a2A۹"
    A3 = "a3-४"
    A30 = "a30०"
    A3_A = "a3A९"
    A4 = "a4-৪"
    A40 = "a40০"
    A4_A = "a4A৯"
    A5 = "a5-੪"
    A50 = "a50੦"
    A5_A = "a5A੯"
    A6 = "a6-૪"
    A60 = "a60૦"
    A6_A = "a6A૯"
    A7 = "a7-୪"
    A70 = "a70୦"
    A7_A = "a7A୯"
    A8 = "a8-௫"
    A80 = "a80௧"
    A8_A = "a8A௯"
    A9 = "a9-౪"
    A90 = "a90౦"
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
