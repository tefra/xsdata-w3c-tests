from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-2-NS"


class NistschemaSvIvAtomicStringEnumeration2Type(Enum):
    """
    :cvar AS_VALUE:
    :cvar BUSINESS:
    :cvar IS_VALUE:
    :cvar LAUNCHING:
    :cvar NIST_ITL:
    :cvar ROBUST:
    :cvar TREMENDOUS:
    :cvar VOICE_ENABLED:
    """
    AS_VALUE = "as"
    BUSINESS = "Business"
    IS_VALUE = "is"
    LAUNCHING = "launching"
    NIST_ITL = "NIST/ITL"
    ROBUST = "robust"
    TREMENDOUS = "tremendous"
    VOICE_ENABLED = "voice-enabled"


@dataclass
class NistschemaSvIvAtomicStringEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
