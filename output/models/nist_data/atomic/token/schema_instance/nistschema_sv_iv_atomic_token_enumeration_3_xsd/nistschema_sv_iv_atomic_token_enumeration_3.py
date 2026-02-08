from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-3-NS"


class NistschemaSvIvAtomicTokenEnumeration3Type(Enum):
    COMPUTING = "Computing"
    COMPATIBILITY = "compatibility"
    STANDARDIZATION = "standardization"
    ENGINEERING = "engineering"
    CONTAINS = "contains"
    AREAS = "areas"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTokenEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-3-NS"

    value: NistschemaSvIvAtomicTokenEnumeration3Type = field()
