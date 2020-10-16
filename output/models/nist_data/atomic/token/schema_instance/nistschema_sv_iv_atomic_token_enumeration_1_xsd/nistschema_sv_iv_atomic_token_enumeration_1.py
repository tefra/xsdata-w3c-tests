from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-1-NS"


class NistschemaSvIvAtomicTokenEnumeration1Type(Enum):
    """
    :cvar BE:
    :cvar KEY:
    :cvar HAS:
    :cvar INFORMATION:
    :cvar SHIFT:
    :cvar DISCOVER:
    :cvar PROVIDE:
    :cvar USER:
    :cvar COMMERCE:
    """
    BE = "be"
    KEY = "key"
    HAS = "has"
    INFORMATION = "information"
    SHIFT = "shift"
    DISCOVER = "discover"
    PROVIDE = "provide"
    USER = "user"
    COMMERCE = "commerce"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
