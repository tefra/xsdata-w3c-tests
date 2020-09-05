from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-enumeration-1-NS"


class NistschemaSvIvAtomicNormalizedStringEnumeration1Type(Enum):
    """
    :cvar TESTS:
    :cvar THEREFORE:
    :cvar BY:
    :cvar SUCH:
    :cvar PARTICIPATING:
    :cvar INTO:
    :cvar AND_VALUE:
    """
    TESTS = "tests"
    THEREFORE = "Therefore"
    BY = "by"
    SUCH = "Such"
    PARTICIPATING = "participating"
    INTO = "into"
    AND_VALUE = "and"


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
