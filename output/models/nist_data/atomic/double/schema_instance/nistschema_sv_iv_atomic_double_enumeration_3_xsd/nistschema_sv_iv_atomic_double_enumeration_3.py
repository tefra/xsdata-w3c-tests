from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-3-NS"


class NistschemaSvIvAtomicDoubleEnumeration3Type(Enum):
    VALUE_4_9_E_324 = 5e-324
    VALUE_3_0828824769404266_E_234 = 3.0828824769404265e-234
    VALUE_2_4426721708407727_E_144 = 2.4426721708407726e-144
    VALUE_3_3142672291800245_E_54 = 3.314267229180025e-54
    VALUE_2_1028238996196812_E36 = 2.102823899619681e+36
    VALUE_2_5674850917565879_E126 = 2.567485091756588e+126
    VALUE_4_6505307100535510_E216 = 4.650530710053551e+216
    VALUE_1_7976931348623157_E308 = 1.7976931348623157e+308


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
