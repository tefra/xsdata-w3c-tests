from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-5-NS"


class NistschemaSvIvAtomicFloatEnumeration5Type(Enum):
    VALUE_1_4_E_45 = 1.4e-45
    VALUE_1_8092974_E_25 = 1.8092974e-25
    VALUE_2_2696584_E_5 = "2.2696584E-5"
    VALUE_2_0771560_E15 = "2.0771560E15"
    VALUE_3_4028235_E38 = 3.4028235e38


@dataclass(kw_only=True)
class NistschemaSvIvAtomicFloatEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-5-NS"

    value: NistschemaSvIvAtomicFloatEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
