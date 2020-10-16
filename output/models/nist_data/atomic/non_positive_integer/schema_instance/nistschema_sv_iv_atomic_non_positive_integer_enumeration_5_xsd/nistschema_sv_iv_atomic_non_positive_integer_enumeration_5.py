from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-5-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration5Type(Enum):
    """
    :cvar VALUE_MINUS_71:
    :cvar VALUE_MINUS_611:
    :cvar VALUE_MINUS_27:
    :cvar VALUE_MINUS_241238476:
    :cvar VALUE_MINUS_8591039:
    :cvar VALUE_MINUS_934828787:
    :cvar VALUE_MINUS_342967456457:
    :cvar VALUE_MINUS_841018047002872:
    :cvar VALUE_MINUS_8884375099:
    """
    VALUE_MINUS_71 = -71
    VALUE_MINUS_611 = -611
    VALUE_MINUS_27 = -27
    VALUE_MINUS_241238476 = -241238476
    VALUE_MINUS_8591039 = -8591039
    VALUE_MINUS_934828787 = -934828787
    VALUE_MINUS_342967456457 = -342967456457
    VALUE_MINUS_841018047002872 = -841018047002872
    VALUE_MINUS_8884375099 = -8884375099


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNonPositiveIntegerEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
