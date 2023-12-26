from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"


class NistschemaSvIvAtomicStringEnumeration5Type(Enum):
    WELL = "well"
    FOR = "for"
    THESE = "these"
    SUCH = "such"
    AS = "as"


@dataclass
class NistschemaSvIvAtomicStringEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicStringEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
