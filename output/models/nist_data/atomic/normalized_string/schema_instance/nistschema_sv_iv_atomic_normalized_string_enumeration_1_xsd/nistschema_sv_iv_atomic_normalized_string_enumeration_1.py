from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration1Type(StrEnum):
    TESTS = "tests"
    THEREFORE = "Therefore"
    BY = "by"
    SUCH = "Such"
    PARTICIPATING = "participating"
    INTO = "into"
    AND = "and"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"

    value: NistschemaSvIvAtomicNormalizedStringEnumeration1Type = field()
