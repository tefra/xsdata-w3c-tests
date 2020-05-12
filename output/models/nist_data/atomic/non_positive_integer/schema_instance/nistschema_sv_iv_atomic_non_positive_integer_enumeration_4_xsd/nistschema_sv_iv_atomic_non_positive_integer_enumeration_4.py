from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-4-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration4Type(Enum):
    """
    :cvar VALUE_MINUS_4710744954:
    :cvar VALUE_MINUS_1090:
    :cvar VALUE_MINUS_9949071662356567:
    :cvar VALUE_MINUS_9764893:
    :cvar VALUE_MINUS_774596823389670285:
    :cvar VALUE_MINUS_216459046:
    :cvar VALUE_MINUS_209931154:
    """
    VALUE_MINUS_4710744954 = -4710744954
    VALUE_MINUS_1090 = -1090
    VALUE_MINUS_9949071662356567 = -9949071662356567
    VALUE_MINUS_9764893 = -9764893
    VALUE_MINUS_774596823389670285 = -774596823389670285
    VALUE_MINUS_216459046 = -216459046
    VALUE_MINUS_209931154 = -209931154


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNonPositiveIntegerEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
