from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration1Type(Enum):
    """
    :cvar SUCH:
    :cvar THEREFORE:
    :cvar AND_VALUE:
    :cvar BY:
    :cvar INTO:
    :cvar PARTICIPATING:
    :cvar TESTS:
    """
    SUCH = "Such"
    THEREFORE = "Therefore"
    AND_VALUE = "and"
    BY = "by"
    INTO = "into"
    PARTICIPATING = "participating"
    TESTS = "tests"


@dataclass
class NistschemaSvIvAtomicNormalizedStringEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNormalizedStringEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
