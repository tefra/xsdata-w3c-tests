from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-1-NS"


class NistschemaSvIvAtomicDoubleEnumeration1Type(Enum):
    """
    :cvar VALUE_4_9_E_324:
    :cvar VALUE_2_2133245030541942_E_234:
    :cvar VALUE_2_2871337380701436_E_144:
    :cvar VALUE_4_8330246595957178_E_54:
    :cvar VALUE_3_5861613937406181_E36:
    :cvar VALUE_2_7457332729808998_E126:
    :cvar VALUE_2_8407030485906319_E216:
    :cvar VALUE_1_7976931348623157_E308:
    """
    VALUE_4_9_E_324 = Decimal('4.9E-324')
    VALUE_2_2133245030541942_E_234 = Decimal('2.2133245030541942E-234')
    VALUE_2_2871337380701436_E_144 = Decimal('2.2871337380701436E-144')
    VALUE_4_8330246595957178_E_54 = Decimal('4.8330246595957178E-54')
    VALUE_3_5861613937406181_E36 = Decimal('3.5861613937406181E+36')
    VALUE_2_7457332729808998_E126 = Decimal('2.7457332729808998E+126')
    VALUE_2_8407030485906319_E216 = Decimal('2.8407030485906319E+216')
    VALUE_1_7976931348623157_E308 = Decimal('1.7976931348623157E+308')


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
        metadata={
            "required": True,
        }
    )
