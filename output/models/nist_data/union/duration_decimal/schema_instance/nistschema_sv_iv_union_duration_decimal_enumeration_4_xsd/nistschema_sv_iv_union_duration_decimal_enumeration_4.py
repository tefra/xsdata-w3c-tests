from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-4-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration4Type(Enum):
    """
    :cvar P2024_Y02_M08_DT18_H57_M25_S:
    :cvar P2025_Y10_M04_DT21_H48_M39_S:
    :cvar VALUE_30_9431:
    :cvar VALUE_35_153218:
    :cvar VALUE_MINUS_6_6957506428:
    :cvar VALUE_MINUS_8662801_7:
    :cvar VALUE_MINUS_9_833664239753505:
    """
    P2024_Y02_M08_DT18_H57_M25_S = "P2024Y02M08DT18H57M25S"
    P2025_Y10_M04_DT21_H48_M39_S = "P2025Y10M04DT21H48M39S"
    VALUE_30_9431 = "30.9431"
    VALUE_35_153218 = "35.153218"
    VALUE_MINUS_6_6957506428 = "-6.6957506428"
    VALUE_MINUS_8662801_7 = "-8662801.7"
    VALUE_MINUS_9_833664239753505 = "-9.833664239753505"


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-4-NS"

    value: Optional[NistschemaSvIvUnionDurationDecimalEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
