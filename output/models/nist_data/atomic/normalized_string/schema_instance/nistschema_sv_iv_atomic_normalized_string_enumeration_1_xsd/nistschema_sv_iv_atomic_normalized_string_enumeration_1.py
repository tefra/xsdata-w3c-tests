from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration1Type(Enum):
    TESTS = "tests"
    THEREFORE = "Therefore"
    BY = "by"
    SUCH = "Such"
    PARTICIPATING = "participating"
    INTO = "into"
    AND_VALUE = "and"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
