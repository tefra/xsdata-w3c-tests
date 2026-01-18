from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration2Type(Enum):
    BE = "be"
    AS = "as"
    TOOLS = "tools"
    XML = "XML"
    SUCH = "Such"
    CREATES = "creates"
    RELATED = "related"
    SOFTWARE = "software"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-2-NS"

    value: NistschemaSvIvAtomicNormalizedStringEnumeration2Type = field(
        metadata={
            "required": True,
        }
    )
