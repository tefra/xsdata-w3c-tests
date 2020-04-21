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
    :cvar A40:
    :cvar A5:
    :cvar A50:
    :cvar A5_A:
    :cvar A6:
    :cvar A60:
    :cvar A6_A:
    :cvar A70:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A9:
    :cvar A90:
    :cvar A9_A:
    """
    A0 = "a0-ڔ"
    A00 = "a00ٱ"
    A0_A = "a0Aڷ"
    A1 = "a1-ڼ"
    A10 = "a10ں"
    A1_A = "a1Aھ"
    A2 = "a2-ۇ"
    A20 = "a20ۀ"
    A2_A = "a2Aێ"
    A3 = "a3-ۑ"
    A30 = "a30ې"
    A3_A = "a3Aۓ"
    A40 = "a40ە"
    A5 = "a5-ۥ"
    A50 = "a50ۥ"
    A5_A = "a5Aۦ"
    A6 = "a6-ट"
    A60 = "a60अ"
    A6_A = "a6Aह"
    A70 = "a70ऽ"
    A8 = "a8-ड़"
    A80 = "a80क़"
    A8_A = "a8Aॡ"
    A9 = "a9-ঈ"
    A90 = "a90অ"
    A9_A = "a9Aঌ"


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
