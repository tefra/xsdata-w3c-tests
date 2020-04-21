from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-2-NS"


class NistschemaSvIvAtomicDoubleEnumeration2Type(Enum):
    """
    :cvar VALUE_1_7976931348623157_E308:
    :cvar VALUE_2_4983147023924484_E216:
    :cvar VALUE_2_7311892445441031_E36:
    :cvar VALUE_2_8869019830516350_E_144:
    :cvar VALUE_2_9181385291440688_E126:
    :cvar VALUE_3_3925700348046903_E_54:
    :cvar VALUE_4_8523411539849754_E_234:
    :cvar VALUE_4_9_E_324:
    """
    VALUE_1_7976931348623157_E308 = "1.7976931348623157E308"
    VALUE_2_4983147023924484_E216 = "2.4983147023924484E216"
    VALUE_2_7311892445441031_E36 = "2.7311892445441031E36"
    VALUE_2_8869019830516350_E_144 = "2.8869019830516350E-144"
    VALUE_2_9181385291440688_E126 = "2.9181385291440688E126"
    VALUE_3_3925700348046903_E_54 = "3.3925700348046903E-54"
    VALUE_4_8523411539849754_E_234 = "4.8523411539849754E-234"
    VALUE_4_9_E_324 = "4.9E-324"


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
