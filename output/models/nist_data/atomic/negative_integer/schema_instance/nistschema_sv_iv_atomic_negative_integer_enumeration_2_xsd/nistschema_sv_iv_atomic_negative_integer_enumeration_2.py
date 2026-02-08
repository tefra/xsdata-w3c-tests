from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-2-NS"


class NistschemaSvIvAtomicNegativeIntegerEnumeration2Type(Enum):
    VALUE_MINUS_51678619095983 = -51678619095983
    VALUE_MINUS_2567 = -2567
    VALUE_MINUS_58812994566 = -58812994566
    VALUE_MINUS_7328890 = -7328890
    VALUE_MINUS_759 = -759
    VALUE_MINUS_567986 = -567986
    VALUE_MINUS_462214 = -462214
    VALUE_MINUS_997161630 = -997161630


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-2-NS"

    value: NistschemaSvIvAtomicNegativeIntegerEnumeration2Type = field()
