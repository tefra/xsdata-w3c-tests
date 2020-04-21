from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-4-NS"


class NistschemaSvIvAtomicTokenEnumeration4Type(Enum):
    """
    :cvar AS_VALUE:
    :cvar IS_VALUE:
    :cvar PICO_CELLULAR:
    :cvar SYNTAX:
    :cvar TECHNIQUES:
    :cvar TO:
    :cvar VISIBLY:
    :cvar WAS:
    """
    AS_VALUE = "as"
    IS_VALUE = "is"
    PICO_CELLULAR = "pico-cellular"
    SYNTAX = "syntax"
    TECHNIQUES = "techniques"
    TO = "to"
    VISIBLY = "visibly"
    WAS = "was"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
