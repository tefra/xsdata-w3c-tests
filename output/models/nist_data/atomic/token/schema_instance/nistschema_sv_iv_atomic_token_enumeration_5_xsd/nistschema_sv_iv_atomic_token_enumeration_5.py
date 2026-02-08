from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-5-NS"


class NistschemaSvIvAtomicTokenEnumeration5Type(Enum):
    THROUGH = "through"
    MANUFACTURERS = "manufacturers"
    THESE = "these"
    THIS = "this"
    AND = "and"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTokenEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-5-NS"

    value: NistschemaSvIvAtomicTokenEnumeration5Type = field()
