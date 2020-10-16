from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-2-NS"


class NistschemaSvIvAtomicStringEnumeration2Type(Enum):
    """
    :cvar VOICE_ENABLED:
    :cvar LAUNCHING:
    :cvar TREMENDOUS:
    :cvar ROBUST:
    :cvar IS_VALUE:
    :cvar NIST_ITL:
    :cvar AS_VALUE:
    :cvar BUSINESS:
    """
    VOICE_ENABLED = "voice-enabled"
    LAUNCHING = "launching"
    TREMENDOUS = "tremendous"
    ROBUST = "robust"
    IS_VALUE = "is"
    NIST_ITL = "NIST/ITL"
    AS_VALUE = "as"
    BUSINESS = "Business"


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
        metadata={
            "required": True,
        }
    )
