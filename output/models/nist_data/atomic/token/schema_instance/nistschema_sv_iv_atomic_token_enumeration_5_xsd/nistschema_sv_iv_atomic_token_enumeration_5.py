from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-5-NS"


class NistschemaSvIvAtomicTokenEnumeration5Type(Enum):
    """
    :cvar AND_VALUE:
    :cvar MANUFACTURERS:
    :cvar THESE:
    :cvar THIS:
    :cvar THROUGH:
    """
    AND_VALUE = "and"
    MANUFACTURERS = "manufacturers"
    THESE = "these"
    THIS = "this"
    THROUGH = "through"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
