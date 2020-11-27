from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration2Type(Enum):
    BE = "be"
    AS_VALUE = "as"
    TOOLS = "tools"
    XML = "XML"
    SUCH = "Such"
    CREATES = "creates"
    RELATED = "related"
    SOFTWARE = "software"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
