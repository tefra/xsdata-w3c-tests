from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration5Type(Enum):
    """
    :cvar VALUE_125:
    :cvar VALUE_153:
    :cvar VALUE_1530:
    :cvar VALUE_261:
    :cvar VALUE_29523017399162965:
    :cvar VALUE_30:
    :cvar VALUE_68919387654218:
    :cvar VALUE_8001281:
    :cvar VALUE_873:
    """
    VALUE_125 = 125
    VALUE_153 = 153
    VALUE_1530 = 1530
    VALUE_261 = 261
    VALUE_29523017399162965 = 29523017399162965
    VALUE_30 = 30
    VALUE_68919387654218 = 68919387654218
    VALUE_8001281 = 8001281
    VALUE_873 = 873


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNonNegativeIntegerEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
