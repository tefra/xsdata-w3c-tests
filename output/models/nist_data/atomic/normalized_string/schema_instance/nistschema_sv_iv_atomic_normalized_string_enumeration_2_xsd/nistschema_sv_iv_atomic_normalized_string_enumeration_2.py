from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration2Type(Enum):
    """
    :cvar BE:
    :cvar AS_VALUE:
    :cvar TOOLS:
    :cvar XML:
    :cvar SUCH:
    :cvar CREATES:
    :cvar RELATED:
    :cvar SOFTWARE:
    """
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
