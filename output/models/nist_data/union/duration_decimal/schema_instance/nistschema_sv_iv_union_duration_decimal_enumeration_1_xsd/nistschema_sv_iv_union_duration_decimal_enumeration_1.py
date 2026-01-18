from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-1-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration1Type(Enum):
    P2016_Y12_M19_DT03_H19_M26_S = XmlDuration("P2016Y12M19DT03H19M26S")
    P1985_Y05_M23_DT13_H27_M38_S = XmlDuration("P1985Y05M23DT13H27M38S")
    VALUE_MINUS_19315130_661 = Decimal("-19315130.661")
    P2030_Y05_M26_DT02_H26_M21_S = XmlDuration("P2030Y05M26DT02H26M21S")
    P2013_Y04_M14_DT17_H28_M59_S = XmlDuration("P2013Y04M14DT17H28M59S")
    VALUE_MINUS_2585_976 = Decimal("-2585.976")
    P1998_Y03_M11_DT00_H17_M15_S = XmlDuration("P1998Y03M11DT00H17M15S")
    P1997_Y09_M05_DT00_H39_M56_S = XmlDuration("P1997Y09M05DT00H39M56S")
    P2003_Y06_M13_DT16_H21_M34_S = XmlDuration("P2003Y06M13DT16H21M34S")


@dataclass(kw_only=True)
class NistschemaSvIvUnionDurationDecimalEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-1"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-1-NS"

    value: NistschemaSvIvUnionDurationDecimalEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
