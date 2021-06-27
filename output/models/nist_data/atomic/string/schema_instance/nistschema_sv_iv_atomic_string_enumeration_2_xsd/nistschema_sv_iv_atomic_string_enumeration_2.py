from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-2-NS"


class NistschemaSvIvAtomicStringEnumeration2Type(Enum):
    VOICE_ENABLED = "voice-enabled"
    LAUNCHING = "launching"
    TREMENDOUS = "tremendous"
    ROBUST = "robust"
    IS = "is"
    NIST_ITL = "NIST/ITL"
    AS = "as"
    BUSINESS = "Business"


@dataclass
class NistschemaSvIvAtomicStringEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
