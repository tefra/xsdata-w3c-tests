from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-3-NS"


class NistschemaSvIvAtomicFloatEnumeration3Type(Enum):
    """
    :cvar VALUE_1_4_E_45:
    :cvar VALUE_1_5954879_E_5:
    :cvar VALUE_2_8312165_E_25:
    :cvar VALUE_3_2481804_E15:
    :cvar VALUE_3_4028235_E38:
    """
    VALUE_1_4_E_45 = "1.4E-45"
    VALUE_1_5954879_E_5 = "1.5954879E-5"
    VALUE_2_8312165_E_25 = "2.8312165E-25"
    VALUE_3_2481804_E15 = "3.2481804E15"
    VALUE_3_4028235_E38 = "3.4028235E38"


@dataclass
class NistschemaSvIvAtomicFloatEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicFloatEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
