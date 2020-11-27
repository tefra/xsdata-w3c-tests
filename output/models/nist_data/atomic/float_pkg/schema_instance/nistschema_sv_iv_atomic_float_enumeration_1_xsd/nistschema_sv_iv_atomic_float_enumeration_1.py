from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-enumeration-1-NS"


class NistschemaSvIvAtomicFloatEnumeration1Type(Enum):
    VALUE_1_4_E_45 = 1.4e-45
    VALUE_1_9703874_E_32 = 1.9703874e-32
    VALUE_2_6927628_E_19 = 2.6927628e-19
    VALUE_2_7455975_E_6 = 2.7455975e-06
    VALUE_2_5357204_E7 = 25357204.0
    VALUE_2_8222192_E20 = 2.8222192e+20
    VALUE_3_4028235_E38 = 3.4028235e+38


@dataclass
class NistschemaSvIvAtomicFloatEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-float-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicFloatEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
