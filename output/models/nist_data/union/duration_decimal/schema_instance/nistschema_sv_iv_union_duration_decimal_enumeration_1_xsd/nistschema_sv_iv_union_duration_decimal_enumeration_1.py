from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-1-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration1Type(Enum):
    P2016_Y12_M19_DT03_H19_M26_S = "P2016Y12M19DT03H19M26S"
    P1985_Y05_M23_DT13_H27_M38_S = "P1985Y05M23DT13H27M38S"
    VALUE_MINUS_19315130_661 = "-19315130.661"
    P2030_Y05_M26_DT02_H26_M21_S = "P2030Y05M26DT02H26M21S"
    P2013_Y04_M14_DT17_H28_M59_S = "P2013Y04M14DT17H28M59S"
    VALUE_MINUS_2585_976 = "-2585.976"
    P1998_Y03_M11_DT00_H17_M15_S = "P1998Y03M11DT00H17M15S"
    P1997_Y09_M05_DT00_H39_M56_S = "P1997Y09M05DT00H39M56S"
    P2003_Y06_M13_DT16_H21_M34_S = "P2003Y06M13DT16H21M34S"


@dataclass
class NistschemaSvIvUnionDurationDecimalEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-1-NS"

    value: Optional[NistschemaSvIvUnionDurationDecimalEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
