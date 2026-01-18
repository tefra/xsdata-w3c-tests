from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-enumeration-3-NS"


class NistschemaSvIvUnionDurationDecimalEnumeration3Type(Enum):
    VALUE_680338314_09 = Decimal("680338314.09")
    VALUE_63_6636824795 = Decimal("63.6636824795")
    P1972_Y11_M10_DT09_H45_M32_S = XmlDuration("P1972Y11M10DT09H45M32S")
    P1978_Y02_M28_DT09_H56_M37_S = XmlDuration("P1978Y02M28DT09H56M37S")
    P1976_Y08_M29_DT20_H45_M11_S = XmlDuration("P1976Y08M29DT20H45M11S")
    P2015_Y06_M24_DT07_H17_M43_S = XmlDuration("P2015Y06M24DT07H17M43S")


@dataclass(kw_only=True)
class NistschemaSvIvUnionDurationDecimalEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-enumeration-3"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-enumeration-3-NS"

    value: NistschemaSvIvUnionDurationDecimalEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
