from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-3-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration3Type(Enum):
    """
    :cvar VALUE_MINUS_10458828265:
    :cvar VALUE_MINUS_29118543:
    :cvar VALUE_MINUS_39825826839070:
    :cvar VALUE_MINUS_50729019:
    :cvar VALUE_MINUS_71959641:
    :cvar VALUE_MINUS_805328452431:
    :cvar VALUE_MINUS_8989002307:
    :cvar VALUE_MINUS_92:
    :cvar VALUE_MINUS_9862058680016422:
    """
    VALUE_MINUS_10458828265 = -10458828265
    VALUE_MINUS_29118543 = -29118543
    VALUE_MINUS_39825826839070 = -39825826839070
    VALUE_MINUS_50729019 = -50729019
    VALUE_MINUS_71959641 = -71959641
    VALUE_MINUS_805328452431 = -805328452431
    VALUE_MINUS_8989002307 = -8989002307
    VALUE_MINUS_92 = -92
    VALUE_MINUS_9862058680016422 = -9862058680016422


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNonPositiveIntegerEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )