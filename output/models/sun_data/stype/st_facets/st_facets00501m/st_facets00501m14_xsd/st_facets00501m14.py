from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A00:
    :cvar A0_A:
    :cvar A10:
    :cvar A20:
    :cvar A3:
    :cvar A30:
    :cvar A3_A:
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
    :cvar A5:
    :cvar A50:
    :cvar A5_A:
    :cvar A60:
    :cvar A70:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A9:
    :cvar A90:
    :cvar A9_A:
    """
    A0 = "a0-ງ"
    A00 = "a00ງ"
    A0_A = "a0Aຈ"
    A10 = "a10ຊ"
    A20 = "a20ຍ"
    A3 = "a3-ຕ"
    A30 = "a30ດ"
    A3_A = "a3Aທ"
    A4 = "a4-ຜ"
    A40 = "a40ນ"
    A4_A = "a4Aຟ"
    A5 = "a5-ຢ"
    A50 = "a50ມ"
    A5_A = "a5Aຣ"
    A60 = "a60ລ"
    A70 = "a70ວ"
    A8 = "a8-ສ"
    A80 = "a80ສ"
    A8_A = "a8Aຫ"
    A9 = "a9-ອ"
    A90 = "a90ອ"
    A9_A = "a9Aຮ"


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
