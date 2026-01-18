from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-5-NS"


class NistschemaSvIvAtomicShortEnumeration5Type(Enum):
    VALUE_MINUS_49 = -49
    VALUE_370 = 370
    VALUE_74 = 74
    VALUE_3112 = 3112
    VALUE_3174 = 3174
    VALUE_MINUS_45 = -45
    VALUE_32767 = 32767


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-5-NS"

    value: NistschemaSvIvAtomicShortEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
