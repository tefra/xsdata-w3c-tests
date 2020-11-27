from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-5-NS"


class NistschemaSvIvAtomicLongEnumeration5Type(Enum):
    VALUE_MINUS_998 = -998
    VALUE_1827924515 = 1827924515
    VALUE_88745595866 = 88745595866
    VALUE_MINUS_14260976357358 = -14260976357358
    VALUE_59419563214914 = 59419563214914
    VALUE_4468 = 4468
    VALUE_4631900674078 = 4631900674078


@dataclass
class NistschemaSvIvAtomicLongEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicLongEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
