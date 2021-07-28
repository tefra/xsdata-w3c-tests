from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration5Type(Enum):
    VALUE_153 = 153
    VALUE_30 = 30
    VALUE_1530 = 1530
    VALUE_125 = 125
    VALUE_68919387654218 = 68919387654218
    VALUE_261 = 261
    VALUE_8001281 = 8001281
    VALUE_29523017399162965 = 29523017399162965
    VALUE_873 = 873


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicNonNegativeIntegerEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
