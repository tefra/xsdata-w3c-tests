from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-4-NS"


class NistschemaSvIvAtomicNonNegativeIntegerEnumeration4Type(Enum):
    VALUE_165524680951923075 = 165524680951923075
    VALUE_25316000768963 = 25316000768963
    VALUE_641253638624229571 = 641253638624229571
    VALUE_90692 = 90692
    VALUE_6809792634202668 = 6809792634202668
    VALUE_5435077718428 = 5435077718428
    VALUE_75086583090071 = 75086583090071
    VALUE_17593746 = 17593746


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-4"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-enumeration-4-NS"
        )

    value: NistschemaSvIvAtomicNonNegativeIntegerEnumeration4Type = field()
