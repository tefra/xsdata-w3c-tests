from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-1-NS"


class NistschemaSvIvAtomicDoubleEnumeration1Type(Enum):
    """
    :cvar VALUE_1_7976931348623157_E308:
    :cvar VALUE_2_2133245030541942_E_234:
    :cvar VALUE_2_2871337380701436_E_144:
    :cvar VALUE_2_7457332729808998_E126:
    :cvar VALUE_2_8407030485906319_E216:
    :cvar VALUE_3_5861613937406181_E36:
    :cvar VALUE_4_8330246595957178_E_54:
    :cvar VALUE_4_9_E_324:
    """
    VALUE_1_7976931348623157_E308 = "1.7976931348623157E308"
    VALUE_2_2133245030541942_E_234 = "2.2133245030541942E-234"
    VALUE_2_2871337380701436_E_144 = "2.2871337380701436E-144"
    VALUE_2_7457332729808998_E126 = "2.7457332729808998E126"
    VALUE_2_8407030485906319_E216 = "2.8407030485906319E216"
    VALUE_3_5861613937406181_E36 = "3.5861613937406181E36"
    VALUE_4_8330246595957178_E_54 = "4.8330246595957178E-54"
    VALUE_4_9_E_324 = "4.9E-324"


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
