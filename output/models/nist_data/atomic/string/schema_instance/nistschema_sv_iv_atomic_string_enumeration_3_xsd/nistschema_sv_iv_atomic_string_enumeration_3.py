from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-3-NS"


class NistschemaSvIvAtomicStringEnumeration3Type(Enum):
    """
    :cvar SYNTAX:
    :cvar THROUGH:
    :cvar ONLY:
    :cvar ANY:
    :cvar OUR:
    :cvar THAT:
    """
    SYNTAX = "syntax"
    THROUGH = "through"
    ONLY = "only"
    ANY = "any"
    OUR = "our"
    THAT = "that"


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
