from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-1-NS"


class NistschemaSvIvAtomicTokenEnumeration1Type(Enum):
    BE = "be"
    KEY = "key"
    HAS = "has"
    INFORMATION = "information"
    SHIFT = "shift"
    DISCOVER = "discover"
    PROVIDE = "provide"
    USER = "user"
    COMMERCE = "commerce"


@dataclass
class NistschemaSvIvAtomicTokenEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicTokenEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
