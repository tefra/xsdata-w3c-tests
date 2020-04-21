from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-2-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration2Type(Enum):
    """
    :cvar VALUE_12914741768813:
    :cvar VALUE_50094:
    :cvar VALUE_55:
    :cvar VALUE_58297003663756774:
    :cvar VALUE_87918438408:
    :cvar VALUE_92809813592:
    """
    VALUE_12914741768813 = 12914741768813
    VALUE_50094 = 50094
    VALUE_55 = 55
    VALUE_58297003663756774 = 58297003663756774
    VALUE_87918438408 = 87918438408
    VALUE_92809813592 = 92809813592


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNonNegativeIntegerEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
