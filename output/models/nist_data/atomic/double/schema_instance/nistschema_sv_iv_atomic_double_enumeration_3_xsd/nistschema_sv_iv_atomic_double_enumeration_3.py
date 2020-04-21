from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-3-NS"


class NistschemaSvIvAtomicDoubleEnumeration3Type(Enum):
    """
    :cvar VALUE_1_7976931348623157_E308:
    :cvar VALUE_2_1028238996196812_E36:
    :cvar VALUE_2_4426721708407727_E_144:
    :cvar VALUE_2_5674850917565879_E126:
    :cvar VALUE_3_0828824769404266_E_234:
    :cvar VALUE_3_3142672291800245_E_54:
    :cvar VALUE_4_6505307100535510_E216:
    :cvar VALUE_4_9_E_324:
    """
    VALUE_1_7976931348623157_E308 = "1.7976931348623157E308"
    VALUE_2_1028238996196812_E36 = "2.1028238996196812E36"
    VALUE_2_4426721708407727_E_144 = "2.4426721708407727E-144"
    VALUE_2_5674850917565879_E126 = "2.5674850917565879E126"
    VALUE_3_0828824769404266_E_234 = "3.0828824769404266E-234"
    VALUE_3_3142672291800245_E_54 = "3.3142672291800245E-54"
    VALUE_4_6505307100535510_E216 = "4.6505307100535510E216"
    VALUE_4_9_E_324 = "4.9E-324"


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
