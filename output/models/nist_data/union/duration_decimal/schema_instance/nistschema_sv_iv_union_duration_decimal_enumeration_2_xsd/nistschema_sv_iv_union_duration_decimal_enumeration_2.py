from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-2-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration2Type(Enum):
    VALUE_680338314_09 = Decimal("680338314.09")
    VALUE_MINUS_293280_774 = Decimal("-293280.774")
    P2003_Y06_M13_DT16_H21_M34_S = XmlDuration("P2003Y06M13DT16H21M34S")
    P2014_Y02_M08_DT09_H42_M46_S = XmlDuration("P2014Y02M08DT09H42M46S")
    P1988_Y08_M11_DT04_H57_M19_S = XmlDuration("P1988Y08M11DT04H57M19S")
    P2013_Y04_M14_DT17_H28_M59_S = XmlDuration("P2013Y04M14DT17H28M59S")
    VALUE_MINUS_3_05 = Decimal("-3.05")
    P1998_Y03_M11_DT00_H17_M15_S = XmlDuration("P1998Y03M11DT00H17M15S")


@dataclass(kw_only=True)
class NistschemaSvIvUnionDurationDecimalEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-2-NS"

    value: NistschemaSvIvUnionDurationDecimalEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
