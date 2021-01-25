from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-4-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration4Type(Enum):
    P2024_Y02_M08_DT18_H57_M25_S = XmlDuration("P2024Y02M08DT18H57M25S")
    VALUE_MINUS_8662801_7 = Decimal("-8662801.7")
    VALUE_MINUS_6_6957506428 = Decimal("-6.6957506428")
    P2025_Y10_M04_DT21_H48_M39_S = XmlDuration("P2025Y10M04DT21H48M39S")
    VALUE_MINUS_9_833664239753505 = Decimal("-9.833664239753505")
    VALUE_35_153218 = Decimal("35.153218")
    VALUE_30_9431 = Decimal("30.9431")


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-4"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-4-NS"

    value: Optional[NistschemaSvIvUnionDurationDecimalEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
