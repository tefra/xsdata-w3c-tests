from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"


class NistschemaSvIvAtomicStringEnumeration5Type(Enum):
    """
    :cvar AS_VALUE:
    :cvar FOR_VALUE:
    :cvar SUCH:
    :cvar THESE:
    :cvar WELL:
    """
    AS_VALUE = "as"
    FOR_VALUE = "for"
    SUCH = "such"
    THESE = "these"
    WELL = "well"


@dataclass
class NistschemaSvIvAtomicStringEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
