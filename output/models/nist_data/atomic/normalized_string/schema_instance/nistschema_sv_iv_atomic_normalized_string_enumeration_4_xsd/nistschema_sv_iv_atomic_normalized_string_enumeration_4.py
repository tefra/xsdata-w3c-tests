from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration4Type(Enum):
    """
    :cvar AND_VALUE:
    :cvar ENGINEERING:
    :cvar MEASUREMENT:
    :cvar OF:
    :cvar WITHOUT:
    """
    AND_VALUE = "and"
    ENGINEERING = "engineering"
    MEASUREMENT = "measurement"
    OF = "of"
    WITHOUT = "without"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )