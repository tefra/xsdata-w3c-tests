from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-3-NS"


class NistschemaSvIvAtomicLongEnumeration3Type(Enum):
    VALUE_43 = 43
    VALUE_MINUS_2032980968765 = -2032980968765
    VALUE_34853718286 = 34853718286
    VALUE_MINUS_368 = -368
    VALUE_80579055795489529 = 80579055795489529
    VALUE_282076 = 282076
    VALUE_MINUS_4722 = -4722
    VALUE_MINUS_12200 = -12200
    VALUE_4812 = 4812


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-3-NS"

    value: NistschemaSvIvAtomicLongEnumeration3Type = field()
