from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-3-NS"


class NistschemaSvIvAtomicStringEnumeration3Type(Enum):
    """
    :cvar ANY:
    :cvar ONLY:
    :cvar OUR:
    :cvar SYNTAX:
    :cvar THAT:
    :cvar THROUGH:
    """
    ANY = "any"
    ONLY = "only"
    OUR = "our"
    SYNTAX = "syntax"
    THAT = "that"
    THROUGH = "through"


@dataclass
class NistschemaSvIvAtomicStringEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
