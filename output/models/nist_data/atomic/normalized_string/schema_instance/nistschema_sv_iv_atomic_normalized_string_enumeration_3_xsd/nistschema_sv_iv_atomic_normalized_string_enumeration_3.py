from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration3Type(Enum):
    AND = "and"
    NIST = "NIST"
    ENABLING = "enabling"
    MANUFACTURERS = "manufacturers"
    DATABASE = "database"
    THE = "the"
    PICO_CELLULAR = "pico-cellular"
    INCLUDING = "including"
    EB_XML = "ebXML"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3-NS"

    value: NistschemaSvIvAtomicNormalizedStringEnumeration3Type = field()
