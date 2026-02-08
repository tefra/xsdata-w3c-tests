from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-5-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration5Type(Enum):
    VALUE_85265 = 85265
    VALUE_2633 = 2633
    VALUE_20007586335496 = 20007586335496
    VALUE_24394 = 24394
    VALUE_15836086414917927 = 15836086414917927
    VALUE_84017762294 = 84017762294
    VALUE_378362663062 = 378362663062


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-5-NS"

    value: NistschemaSvIvAtomicPositiveIntegerEnumeration5Type = field()
