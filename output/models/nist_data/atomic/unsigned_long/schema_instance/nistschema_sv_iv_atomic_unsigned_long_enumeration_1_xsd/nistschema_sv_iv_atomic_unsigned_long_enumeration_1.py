from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-1-NS"


class NistschemaSvIvAtomicUnsignedLongEnumeration1Type(Enum):
    """
    :cvar VALUE_16:
    :cvar VALUE_235157797394:
    :cvar VALUE_2841737:
    :cvar VALUE_475868893660:
    :cvar VALUE_502437096339080:
    :cvar VALUE_6246890837920823:
    :cvar VALUE_69228431818957325:
    """
    VALUE_16 = 16
    VALUE_235157797394 = 235157797394
    VALUE_2841737 = 2841737
    VALUE_475868893660 = 475868893660
    VALUE_502437096339080 = 502437096339080
    VALUE_6246890837920823 = 6246890837920823
    VALUE_69228431818957325 = 69228431818957325


@dataclass
class NistschemaSvIvAtomicUnsignedLongEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicUnsignedLongEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
