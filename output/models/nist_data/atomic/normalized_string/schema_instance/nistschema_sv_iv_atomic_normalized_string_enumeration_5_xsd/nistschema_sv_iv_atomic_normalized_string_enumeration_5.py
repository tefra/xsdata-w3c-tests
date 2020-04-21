from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration5Type(Enum):
    """
    :cvar BY:
    :cvar PC:
    :cvar BE:
    :cvar DEVICES:
    :cvar OPERATING:
    :cvar THE:
    """
    BY = "By"
    PC = "PC"
    BE = "be"
    DEVICES = "devices"
    OPERATING = "operating"
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
