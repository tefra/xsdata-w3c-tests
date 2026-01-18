from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-5-NS"


class NistschemaSvIvAtomicLongEnumeration5Type(Enum):
    VALUE_MINUS_998 = -998
    VALUE_1827924515 = 1827924515
    VALUE_88745595866 = 88745595866
    VALUE_MINUS_14260976357358 = -14260976357358
    VALUE_59419563214914 = 59419563214914
    VALUE_4468 = 4468
    VALUE_4631900674078 = 4631900674078


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-5-NS"

    value: NistschemaSvIvAtomicLongEnumeration5Type = field(
        metadata={
            "required": True,
        }
    )
