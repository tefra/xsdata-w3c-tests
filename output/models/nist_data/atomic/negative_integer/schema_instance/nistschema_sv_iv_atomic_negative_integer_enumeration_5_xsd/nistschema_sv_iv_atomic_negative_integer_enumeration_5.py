from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-5-NS"


class NistschemaSvIvAtomicNegativeIntegerEnumeration5Type(Enum):
    """
    :cvar VALUE_MINUS_4336721877308:
    :cvar VALUE_MINUS_852169232158110:
    :cvar VALUE_MINUS_6208:
    :cvar VALUE_MINUS_972552137318:
    :cvar VALUE_MINUS_632:
    :cvar VALUE_MINUS_8638729626:
    :cvar VALUE_MINUS_1243882220834:
    :cvar VALUE_MINUS_312437399392143:
    """
    VALUE_MINUS_4336721877308 = -4336721877308
    VALUE_MINUS_852169232158110 = -852169232158110
    VALUE_MINUS_6208 = -6208
    VALUE_MINUS_972552137318 = -972552137318
    VALUE_MINUS_632 = -632
    VALUE_MINUS_8638729626 = -8638729626
    VALUE_MINUS_1243882220834 = -1243882220834
    VALUE_MINUS_312437399392143 = -312437399392143


@dataclass
class NistschemaSvIvAtomicNegativeIntegerEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNegativeIntegerEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
