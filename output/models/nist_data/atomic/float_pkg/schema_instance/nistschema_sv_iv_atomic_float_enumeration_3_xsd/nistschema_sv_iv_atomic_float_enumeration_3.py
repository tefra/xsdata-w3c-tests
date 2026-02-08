from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-3-NS"


class NistschemaSvIvAtomicFloatEnumeration3Type(Enum):
    VALUE_1_4_E_45 = 1.4e-45
    VALUE_2_8312165_E_25 = 2.8312165e-25
    VALUE_1_5954879_E_5 = "1.5954879E-5"
    VALUE_3_2481804_E15 = "3.2481804E15"
    VALUE_3_4028235_E38 = 3.4028235e38


@dataclass(kw_only=True)
class NistschemaSvIvAtomicFloatEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-3-NS"

    value: NistschemaSvIvAtomicFloatEnumeration3Type = field()
