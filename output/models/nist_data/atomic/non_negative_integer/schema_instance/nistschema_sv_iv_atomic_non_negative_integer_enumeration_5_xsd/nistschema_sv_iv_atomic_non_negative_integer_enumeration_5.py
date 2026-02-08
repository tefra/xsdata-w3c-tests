from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-5-NS"
        )

    value: NistschemaSvIvAtomicNonNegativeIntegerEnumeration5Type = field()
