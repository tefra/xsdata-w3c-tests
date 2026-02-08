from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"


class NistschemaSvIvAtomicStringEnumeration5Type(Enum):
    WELL = "well"
    FOR = "for"
    THESE = "these"
    SUCH = "such"
    AS = "as"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicStringEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-string-enumeration-5-NS"

    value: NistschemaSvIvAtomicStringEnumeration5Type = field()
