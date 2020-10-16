from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration5Type(Enum):
    """
    :cvar BY:
    :cvar DEVICES:
    :cvar THE:
    :cvar PC:
    :cvar BE:
    :cvar OPERATING:
    """
    BY = "By"
    DEVICES = "devices"
    THE = "the"
    PC = "PC"
    BE = "be"
    OPERATING = "operating"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
