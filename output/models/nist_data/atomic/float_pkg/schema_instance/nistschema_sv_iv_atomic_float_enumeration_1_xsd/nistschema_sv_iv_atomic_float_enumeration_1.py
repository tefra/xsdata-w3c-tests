from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-1-NS"


class NistschemaSvIvAtomicFloatEnumeration1Type(Enum):
    """
    :cvar VALUE_1_4_E_45:
    :cvar VALUE_1_9703874_E_32:
    :cvar VALUE_2_5357204_E7:
    :cvar VALUE_2_6927628_E_19:
    :cvar VALUE_2_7455975_E_6:
    :cvar VALUE_2_8222192_E20:
    :cvar VALUE_3_4028235_E38:
    """
    VALUE_1_4_E_45 = "1.4E-45"
    VALUE_1_9703874_E_32 = "1.9703874E-32"
    VALUE_2_5357204_E7 = "2.5357204E7"
    VALUE_2_6927628_E_19 = "2.6927628E-19"
    VALUE_2_7455975_E_6 = "2.7455975E-6"
    VALUE_2_8222192_E20 = "2.8222192E20"
    VALUE_3_4028235_E38 = "3.4028235E38"


@dataclass
class NistschemaSvIvAtomicFloatEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicFloatEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )