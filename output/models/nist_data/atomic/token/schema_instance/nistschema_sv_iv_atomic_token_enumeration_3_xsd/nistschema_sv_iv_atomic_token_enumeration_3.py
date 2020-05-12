from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-3-NS"


class NistschemaSvIvAtomicTokenEnumeration3Type(Enum):
    """
    :cvar AREAS:
    :cvar COMPATIBILITY:
    :cvar COMPUTING:
    :cvar CONTAINS:
    :cvar ENGINEERING:
    :cvar STANDARDIZATION:
    """
    AREAS = "areas"
    COMPATIBILITY = "compatibility"
    COMPUTING = "Computing"
    CONTAINS = "contains"
    ENGINEERING = "engineering"
    STANDARDIZATION = "standardization"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
