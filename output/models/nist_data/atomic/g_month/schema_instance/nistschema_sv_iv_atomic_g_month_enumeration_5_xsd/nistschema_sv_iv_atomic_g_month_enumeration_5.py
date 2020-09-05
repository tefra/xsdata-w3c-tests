from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-enumeration-5-NS"


class NistschemaSvIvAtomicGMonthEnumeration5Type(Enum):
    """
    :cvar VALUE_06:
    :cvar VALUE_05:
    :cvar VALUE_02:
    :cvar VALUE_01:
    """
    VALUE_06 = "--06"
    VALUE_05 = "--05"
    VALUE_02 = "--02"
    VALUE_01 = "--01"


@dataclass
class NistschemaSvIvAtomicGMonthEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicGMonthEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
