from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-1-NS"


class NistschemaSvIvAtomicDoubleEnumeration1Type(Enum):
    VALUE_4_9_E_324 = "4.9E-324"
    VALUE_2_2133245030541942_E_234 = 2.2133245030541942e-234
    VALUE_2_2871337380701436_E_144 = "2.2871337380701436E-144"
    VALUE_4_8330246595957178_E_54 = "4.8330246595957178E-54"
    VALUE_3_5861613937406181_E36 = "3.5861613937406181E36"
    VALUE_2_7457332729808998_E126 = "2.7457332729808998E126"
    VALUE_2_8407030485906319_E216 = "2.8407030485906319E216"
    VALUE_1_7976931348623157_E308 = 1.7976931348623157e308


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDoubleEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-1-NS"

    value: NistschemaSvIvAtomicDoubleEnumeration1Type = field()
