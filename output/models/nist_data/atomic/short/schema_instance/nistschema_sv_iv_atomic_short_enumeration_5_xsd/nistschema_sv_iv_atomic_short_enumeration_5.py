from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-enumeration-5-NS"


class NistschemaSvIvAtomicShortEnumeration5Type(Enum):
    VALUE_MINUS_49 = -49
    VALUE_370 = 370
    VALUE_74 = 74
    VALUE_3112 = 3112
    VALUE_3174 = 3174
    VALUE_MINUS_45 = -45
    VALUE_32767 = 32767


@dataclass
class NistschemaSvIvAtomicShortEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-short-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicShortEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
