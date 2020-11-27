from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration4Type(Enum):
    WITHOUT = "without"
    MEASUREMENT = "measurement"
    AND_VALUE = "and"
    ENGINEERING = "engineering"
    OF = "of"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
