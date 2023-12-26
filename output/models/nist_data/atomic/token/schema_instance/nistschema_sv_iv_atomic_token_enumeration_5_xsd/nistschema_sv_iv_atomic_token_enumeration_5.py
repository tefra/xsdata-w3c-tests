from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-5-NS"


class NistschemaSvIvAtomicTokenEnumeration5Type(Enum):
    THROUGH = "through"
    MANUFACTURERS = "manufacturers"
    THESE = "these"
    THIS = "this"
    AND = "and"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
