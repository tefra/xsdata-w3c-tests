from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A0:
    :cvar A0_A:
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
    """
    A00 = "a00೦"
    A0 = "a0-೪"
    A0_A = "a0A೯"
    A10 = "a10൦"
    A1 = "a1-൪"
    A1_A = "a1A൯"
    A20 = "a20๐"
    A2 = "a2-๔"
    A2_A = "a2A๙"
    A30 = "a30໐"
    A3 = "a3-໔"
    A3_A = "a3A໙"
    A40 = "a40༠"
    A4 = "a4-༤"
    A4_A = "a4A༩"


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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
