from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-2-NS"


class NistschemaSvIvAtomicFloatEnumeration2Type(Enum):
    VALUE_1_4_E_45 = 1.4e-45
    VALUE_3_1628908_E_25 = 3.1628908e-25
    VALUE_3_3473630_E_5 = "3.3473630E-5"
    VALUE_1_5006857_E15 = "1.5006857E15"
    VALUE_3_4028235_E38 = 3.4028235e38


@dataclass(kw_only=True)
class NistschemaSvIvAtomicFloatEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-2-NS"

    value: NistschemaSvIvAtomicFloatEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
