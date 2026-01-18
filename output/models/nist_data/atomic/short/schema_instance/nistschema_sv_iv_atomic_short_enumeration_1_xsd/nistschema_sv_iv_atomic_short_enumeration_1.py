from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-1-NS"


class NistschemaSvIvAtomicShortEnumeration1Type(Enum):
    VALUE_MINUS_8076 = -8076
    VALUE_5805 = 5805
    VALUE_11013 = 11013
    VALUE_MINUS_5 = -5
    VALUE_7589 = 7589
    VALUE_MINUS_84 = -84


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-1-NS"

    value: NistschemaSvIvAtomicShortEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
