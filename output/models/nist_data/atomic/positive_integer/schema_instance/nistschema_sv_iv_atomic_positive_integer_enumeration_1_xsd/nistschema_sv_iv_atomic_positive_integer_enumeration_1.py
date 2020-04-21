from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-1-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration1Type(Enum):
    """
    :cvar VALUE_101001635697:
    :cvar VALUE_29:
    :cvar VALUE_3059918349066803:
    :cvar VALUE_39237065970202644:
    :cvar VALUE_408576971836088:
    :cvar VALUE_44881:
    :cvar VALUE_557:
    :cvar VALUE_7652:
    """
    VALUE_101001635697 = 101001635697
    VALUE_29 = 29
    VALUE_3059918349066803 = 3059918349066803
    VALUE_39237065970202644 = 39237065970202644
    VALUE_408576971836088 = 408576971836088
    VALUE_44881 = 44881
    VALUE_557 = 557
    VALUE_7652 = 7652


@dataclass
class NistschemaSvIvAtomicPositiveIntegerEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicPositiveIntegerEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
