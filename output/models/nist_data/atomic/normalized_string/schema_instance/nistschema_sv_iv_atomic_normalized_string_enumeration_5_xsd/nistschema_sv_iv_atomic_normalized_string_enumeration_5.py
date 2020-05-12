from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration5Type(Enum):
    """
    :cvar BE:
    :cvar BY:
    :cvar DEVICES:
    :cvar OPERATING:
    :cvar PC:
    :cvar THE:
    """
    BE = "be"
    BY = "By"
    DEVICES = "devices"
    OPERATING = "operating"
    PC = "PC"
    THE = "the"


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
        metadata=dict(
            required=True
        )
    )
