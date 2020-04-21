from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-4-NS"


class NistschemaSvIvAtomicDoubleEnumeration4Type(Enum):
    """
    :cvar VALUE_1_7976931348623157_E308:
    :cvar VALUE_1_9543492578327128_E_234:
    :cvar VALUE_2_0744434746534796_E36:
    :cvar VALUE_3_4043189586904751_E216:
    :cvar VALUE_4_2180257301126178_E_54:
    :cvar VALUE_4_3411284761058989_E126:
    :cvar VALUE_4_6337466732941437_E_144:
    :cvar VALUE_4_9_E_324:
    """
    VALUE_1_7976931348623157_E308 = "1.7976931348623157E308"
    VALUE_1_9543492578327128_E_234 = "1.9543492578327128E-234"
    VALUE_2_0744434746534796_E36 = "2.0744434746534796E36"
    VALUE_3_4043189586904751_E216 = "3.4043189586904751E216"
    VALUE_4_2180257301126178_E_54 = "4.2180257301126178E-54"
    VALUE_4_3411284761058989_E126 = "4.3411284761058989E126"
    VALUE_4_6337466732941437_E_144 = "4.6337466732941437E-144"
    VALUE_4_9_E_324 = "4.9E-324"


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
