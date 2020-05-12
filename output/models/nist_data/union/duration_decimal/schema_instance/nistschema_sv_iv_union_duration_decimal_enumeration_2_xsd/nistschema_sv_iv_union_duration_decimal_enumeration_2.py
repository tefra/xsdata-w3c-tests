from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-2-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration2Type(Enum):
    """
    :cvar VALUE_680338314_09:
    :cvar VALUE_MINUS_293280_774:
    :cvar P2003_Y06_M13_DT16_H21_M34_S:
    :cvar P2014_Y02_M08_DT09_H42_M46_S:
    :cvar P1988_Y08_M11_DT04_H57_M19_S:
    :cvar P2013_Y04_M14_DT17_H28_M59_S:
    :cvar VALUE_MINUS_3_05:
    :cvar P1998_Y03_M11_DT00_H17_M15_S:
    """
    VALUE_680338314_09 = "680338314.09"
    VALUE_MINUS_293280_774 = "-293280.774"
    P2003_Y06_M13_DT16_H21_M34_S = "P2003Y06M13DT16H21M34S"
    P2014_Y02_M08_DT09_H42_M46_S = "P2014Y02M08DT09H42M46S"
    P1988_Y08_M11_DT04_H57_M19_S = "P1988Y08M11DT04H57M19S"
    P2013_Y04_M14_DT17_H28_M59_S = "P2013Y04M14DT17H28M59S"
    VALUE_MINUS_3_05 = "-3.05"
    P1998_Y03_M11_DT00_H17_M15_S = "P1998Y03M11DT00H17M15S"


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-2-NS"

    value: Optional[NistschemaSvIvUnionDurationDecimalEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
