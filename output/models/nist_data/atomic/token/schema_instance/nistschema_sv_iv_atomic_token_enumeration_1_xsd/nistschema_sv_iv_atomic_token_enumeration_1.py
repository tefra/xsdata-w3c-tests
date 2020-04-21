from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-1-NS"


class NistschemaSvIvAtomicTokenEnumeration1Type(Enum):
    """
    :cvar BE:
    :cvar COMMERCE:
    :cvar DISCOVER:
    :cvar HAS:
    :cvar INFORMATION:
    :cvar KEY:
    :cvar PROVIDE:
    :cvar SHIFT:
    :cvar USER:
    """
    BE = "be"
    COMMERCE = "commerce"
    DISCOVER = "discover"
    HAS = "has"
    INFORMATION = "information"
    KEY = "key"
    PROVIDE = "provide"
    SHIFT = "shift"
    USER = "user"


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
        metadata=dict(
            required=True
        )
    )
