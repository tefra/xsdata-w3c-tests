from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

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


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3-NS"

    value: Optional[
        NistschemaSvIvAtomicNormalizedStringEnumeration3Type
    ] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
