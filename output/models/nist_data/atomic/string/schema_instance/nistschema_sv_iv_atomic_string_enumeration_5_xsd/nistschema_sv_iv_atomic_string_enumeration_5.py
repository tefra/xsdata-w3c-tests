from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"


class NistschemaSvIvAtomicStringEnumeration5Type(Enum):
    """
    :cvar WELL:
    :cvar FOR_VALUE:
    :cvar THESE:
    :cvar SUCH:
    :cvar AS_VALUE:
    """
    WELL = "well"
    FOR_VALUE = "for"
    THESE = "these"
    SUCH = "such"
    AS_VALUE = "as"


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
        metadata={
            "required": True,
        }
    )
