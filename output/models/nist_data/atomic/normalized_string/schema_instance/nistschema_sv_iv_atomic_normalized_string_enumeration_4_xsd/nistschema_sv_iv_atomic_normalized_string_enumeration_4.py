from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration4Type(Enum):
    WITHOUT = "without"
    MEASUREMENT = "measurement"
    AND = "and"
    ENGINEERING = "engineering"
    OF = "of"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-4-NS"

    value: NistschemaSvIvAtomicNormalizedStringEnumeration4Type = field()
