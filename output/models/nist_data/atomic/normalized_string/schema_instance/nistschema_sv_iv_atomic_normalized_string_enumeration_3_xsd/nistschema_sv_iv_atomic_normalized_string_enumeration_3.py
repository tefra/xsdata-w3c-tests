from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration3Type(Enum):
    """
    :cvar AND_VALUE:
    :cvar DATABASE:
    :cvar EB_XML:
    :cvar ENABLING:
    :cvar INCLUDING:
    :cvar MANUFACTURERS:
    :cvar NIST:
    :cvar PICO_CELLULAR:
    :cvar THE:
    """
    AND_VALUE = "and"
    DATABASE = "database"
    EB_XML = "ebXML"
    ENABLING = "enabling"
    INCLUDING = "including"
    MANUFACTURERS = "manufacturers"
    NIST = "NIST"
    PICO_CELLULAR = "pico-cellular"
    THE = "the"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
