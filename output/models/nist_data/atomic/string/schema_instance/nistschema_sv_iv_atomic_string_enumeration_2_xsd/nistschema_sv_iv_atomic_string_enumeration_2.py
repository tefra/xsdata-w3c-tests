from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-2-NS"

    value: NistschemaSvIvAtomicStringEnumeration2Type = field()
