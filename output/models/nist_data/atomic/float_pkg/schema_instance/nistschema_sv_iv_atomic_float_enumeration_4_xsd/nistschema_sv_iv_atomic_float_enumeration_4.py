from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-4-NS"


class NistschemaSvIvAtomicFloatEnumeration4Type(Enum):
    """
    :cvar VALUE_1_4_E_45:
    :cvar VALUE_1_7053130_E_34:
    :cvar VALUE_3_2152819_E_23:
    :cvar VALUE_2_4912911_E_12:
    :cvar VALUE_1_4657043_E_1:
    :cvar VALUE_3_1031987_E10:
    :cvar VALUE_2_7832936_E21:
    :cvar VALUE_3_4028235_E38:
    """
    VALUE_1_4_E_45 = "1.4E-45"
    VALUE_1_7053130_E_34 = "1.7053130E-34"
    VALUE_3_2152819_E_23 = "3.2152819E-23"
    VALUE_2_4912911_E_12 = "2.4912911E-12"
    VALUE_1_4657043_E_1 = "1.4657043E-1"
    VALUE_3_1031987_E10 = "3.1031987E10"
    VALUE_2_7832936_E21 = "2.7832936E21"
    VALUE_3_4028235_E38 = "3.4028235E38"


@dataclass
class NistschemaSvIvAtomicFloatEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicFloatEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
