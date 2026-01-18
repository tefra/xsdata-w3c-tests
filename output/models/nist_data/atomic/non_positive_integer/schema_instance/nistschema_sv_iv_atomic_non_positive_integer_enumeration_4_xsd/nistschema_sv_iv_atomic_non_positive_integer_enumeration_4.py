from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-4-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration4Type(Enum):
    VALUE_MINUS_4710744954 = -4710744954
    VALUE_MINUS_1090 = -1090
    VALUE_MINUS_9949071662356567 = -9949071662356567
    VALUE_MINUS_9764893 = -9764893
    VALUE_MINUS_774596823389670285 = -774596823389670285
    VALUE_MINUS_216459046 = -216459046
    VALUE_MINUS_209931154 = -209931154


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-4"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-4-NS"
        )

    value: NistschemaSvIvAtomicNonPositiveIntegerEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
