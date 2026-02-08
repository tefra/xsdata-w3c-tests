from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-5-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration5Type(Enum):
    VALUE_MINUS_71 = -71
    VALUE_MINUS_611 = -611
    VALUE_MINUS_27 = -27
    VALUE_MINUS_241238476 = -241238476
    VALUE_MINUS_8591039 = -8591039
    VALUE_MINUS_934828787 = -934828787
    VALUE_MINUS_342967456457 = -342967456457
    VALUE_MINUS_841018047002872 = -841018047002872
    VALUE_MINUS_8884375099 = -8884375099


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-5"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-5-NS"
        )

    value: NistschemaSvIvAtomicNonPositiveIntegerEnumeration5Type = field()
