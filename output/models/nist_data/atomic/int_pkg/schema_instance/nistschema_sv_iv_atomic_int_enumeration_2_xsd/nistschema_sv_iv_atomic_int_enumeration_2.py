from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-2-NS"


class NistschemaSvIvAtomicIntEnumeration2Type(Enum):
    VALUE_MINUS_2147483648 = -2147483648
    VALUE_516405021 = 516405021
    VALUE_997702013 = 997702013
    VALUE_MINUS_4389 = -4389
    VALUE_MINUS_279694555 = -279694555
    VALUE_2147483647 = 2147483647
    VALUE_MINUS_8333939 = -8333939
    VALUE_68011 = 68011
    VALUE_376934 = 376934


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-2-NS"

    value: NistschemaSvIvAtomicIntEnumeration2Type = field()
