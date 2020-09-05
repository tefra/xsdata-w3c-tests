from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-5-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration5Type(Enum):
    """
    :cvar VALUE_MINUS_9_833664239753505:
    :cvar P2030_Y05_M26_DT02_H26_M21_S:
    :cvar VALUE_2_02830188:
    :cvar P2024_Y02_M08_DT18_H57_M25_S:
    :cvar VALUE_MINUS_19315130_661:
    :cvar VALUE_MINUS_471562_69552:
    :cvar VALUE_MINUS_33596_4487:
    """
    VALUE_MINUS_9_833664239753505 = "-9.833664239753505"
    P2030_Y05_M26_DT02_H26_M21_S = "P2030Y05M26DT02H26M21S"
    VALUE_2_02830188 = "2.02830188"
    P2024_Y02_M08_DT18_H57_M25_S = "P2024Y02M08DT18H57M25S"
    VALUE_MINUS_19315130_661 = "-19315130.661"
    VALUE_MINUS_471562_69552 = "-471562.69552"
    VALUE_MINUS_33596_4487 = "-33596.4487"


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-5-NS"

    value: Optional[NistschemaSvIvUnionDurationDecimalEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
