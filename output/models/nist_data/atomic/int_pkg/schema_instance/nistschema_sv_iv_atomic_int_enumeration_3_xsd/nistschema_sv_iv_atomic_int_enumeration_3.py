from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-enumeration-3-NS"


class NistschemaSvIvAtomicIntEnumeration3Type(Enum):
    VALUE_2147483647 = 2147483647
    VALUE_70977758 = 70977758
    VALUE_323669986 = 323669986
    VALUE_MINUS_314 = -314
    VALUE_MINUS_53685045 = -53685045
    VALUE_9391921 = 9391921
    VALUE_43292492 = 43292492
    VALUE_MINUS_2142090 = -2142090


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-int-enumeration-3-NS"

    value: NistschemaSvIvAtomicIntEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
