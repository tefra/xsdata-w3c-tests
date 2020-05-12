from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-4-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration4Type(Enum):
    """
    :cvar VALUE_66130353503:
    :cvar VALUE_2337:
    :cvar VALUE_27711148:
    :cvar VALUE_849926:
    :cvar VALUE_600957:
    :cvar VALUE_822:
    :cvar VALUE_7497:
    :cvar VALUE_3167940084:
    :cvar VALUE_435109:
    """
    VALUE_66130353503 = 66130353503
    VALUE_2337 = 2337
    VALUE_27711148 = 27711148
    VALUE_849926 = 849926
    VALUE_600957 = 600957
    VALUE_822 = 822
    VALUE_7497 = 7497
    VALUE_3167940084 = 3167940084
    VALUE_435109 = 435109


@dataclass
class NistschemaSvIvAtomicPositiveIntegerEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicPositiveIntegerEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
