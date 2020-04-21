from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-5-NS"


class NistschemaSvIvAtomicFloatEnumeration5Type(Enum):
    """
    :cvar VALUE_1_4_E_45:
    :cvar VALUE_1_8092974_E_25:
    :cvar VALUE_2_0771560_E15:
    :cvar VALUE_2_2696584_E_5:
    :cvar VALUE_3_4028235_E38:
    """
    VALUE_1_4_E_45 = "1.4E-45"
    VALUE_1_8092974_E_25 = "1.8092974E-25"
    VALUE_2_0771560_E15 = "2.0771560E15"
    VALUE_2_2696584_E_5 = "2.2696584E-5"
    VALUE_3_4028235_E38 = "3.4028235E38"


@dataclass
class NistschemaSvIvAtomicFloatEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicFloatEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
