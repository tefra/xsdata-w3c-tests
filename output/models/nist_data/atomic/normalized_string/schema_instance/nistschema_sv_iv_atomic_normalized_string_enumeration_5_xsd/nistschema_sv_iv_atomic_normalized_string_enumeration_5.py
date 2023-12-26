from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration5Type(Enum):
    BY = "By"
    DEVICES = "devices"
    THE = "the"
    PC = "PC"
    BE = "be"
    OPERATING = "operating"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"

    value: Optional[
        NistschemaSvIvAtomicNormalizedStringEnumeration5Type
    ] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
