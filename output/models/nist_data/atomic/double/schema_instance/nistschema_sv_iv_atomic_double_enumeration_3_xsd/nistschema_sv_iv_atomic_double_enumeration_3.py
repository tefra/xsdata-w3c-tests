from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-3-NS"


class NistschemaSvIvAtomicDoubleEnumeration3Type(Enum):
    """
    :cvar VALUE_4_9_E_324:
    :cvar VALUE_3_0828824769404266_E_234:
    :cvar VALUE_2_4426721708407727_E_144:
    :cvar VALUE_3_3142672291800245_E_54:
    :cvar VALUE_2_1028238996196812_E36:
    :cvar VALUE_2_5674850917565879_E126:
    :cvar VALUE_4_6505307100535510_E216:
    :cvar VALUE_1_7976931348623157_E308:
    """
    VALUE_4_9_E_324 = Decimal('4.9E-324')
    VALUE_3_0828824769404266_E_234 = Decimal('3.0828824769404266E-234')
    VALUE_2_4426721708407727_E_144 = Decimal('2.4426721708407727E-144')
    VALUE_3_3142672291800245_E_54 = Decimal('3.3142672291800245E-54')
    VALUE_2_1028238996196812_E36 = Decimal('2.1028238996196812E+36')
    VALUE_2_5674850917565879_E126 = Decimal('2.5674850917565879E+126')
    VALUE_4_6505307100535510_E216 = Decimal('4.6505307100535510E+216')
    VALUE_1_7976931348623157_E308 = Decimal('1.7976931348623157E+308')


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
