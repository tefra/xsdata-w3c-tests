from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A00:
    :cvar A0_A:
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
    """
    A0 = "a0-೪"
    A00 = "a00೦"
    A0_A = "a0A೯"
    A1 = "a1-൪"
    A10 = "a10൦"
    A1_A = "a1A൯"
    A2 = "a2-๔"
    A20 = "a20๐"
    A2_A = "a2A๙"
    A3 = "a3-໔"
    A30 = "a30໐"
    A3_A = "a3A໙"
    A4 = "a4-༤"
    A40 = "a40༠"
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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
