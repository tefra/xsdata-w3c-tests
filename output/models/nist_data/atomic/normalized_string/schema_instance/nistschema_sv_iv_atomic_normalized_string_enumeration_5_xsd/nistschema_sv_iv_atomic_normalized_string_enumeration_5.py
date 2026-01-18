from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration5Type(Enum):
    BY = "By"
    DEVICES = "devices"
    THE = "the"
    PC = "PC"
    BE = "be"
    OPERATING = "operating"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-5-NS"

    value: NistschemaSvIvAtomicNormalizedStringEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
