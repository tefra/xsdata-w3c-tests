from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-5-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration5Type(Enum):
    VALUE_MINUS_9_833664239753505 = Decimal("-9.833664239753505")
    P2030_Y05_M26_DT02_H26_M21_S = XmlDuration("P2030Y05M26DT02H26M21S")
    VALUE_2_02830188 = Decimal("2.02830188")
    P2024_Y02_M08_DT18_H57_M25_S = XmlDuration("P2024Y02M08DT18H57M25S")
    VALUE_MINUS_19315130_661 = Decimal("-19315130.661")
    VALUE_MINUS_471562_69552 = Decimal("-471562.69552")
    VALUE_MINUS_33596_4487 = Decimal("-33596.4487")


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-5"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-5-NS"

    value: Optional[
        NistschemaSvIvUnionDurationDecimalEnumeration5Type
    ] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
