from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-3-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration3Type(Enum):
    """
    :cvar VALUE_680338314_09:
    :cvar VALUE_63_6636824795:
    :cvar P1972_Y11_M10_DT09_H45_M32_S:
    :cvar P1978_Y02_M28_DT09_H56_M37_S:
    :cvar P1976_Y08_M29_DT20_H45_M11_S:
    :cvar P2015_Y06_M24_DT07_H17_M43_S:
    """
    VALUE_680338314_09 = "680338314.09"
    VALUE_63_6636824795 = "63.6636824795"
    P1972_Y11_M10_DT09_H45_M32_S = "P1972Y11M10DT09H45M32S"
    P1978_Y02_M28_DT09_H56_M37_S = "P1978Y02M28DT09H56M37S"
    P1976_Y08_M29_DT20_H45_M11_S = "P1976Y08M29DT20H45M11S"
    P2015_Y06_M24_DT07_H17_M43_S = "P2015Y06M24DT07H17M43S"


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-3-NS"

    value: Optional[NistschemaSvIvUnionDurationDecimalEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
