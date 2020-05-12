from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration2Type(Enum):
    """
    :cvar AS_VALUE:
    :cvar BE:
    :cvar CREATES:
    :cvar RELATED:
    :cvar SOFTWARE:
    :cvar SUCH:
    :cvar TOOLS:
    :cvar XML:
    """
    AS_VALUE = "as"
    BE = "be"
    CREATES = "creates"
    RELATED = "related"
    SOFTWARE = "software"
    SUCH = "Such"
    TOOLS = "tools"
    XML = "XML"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
