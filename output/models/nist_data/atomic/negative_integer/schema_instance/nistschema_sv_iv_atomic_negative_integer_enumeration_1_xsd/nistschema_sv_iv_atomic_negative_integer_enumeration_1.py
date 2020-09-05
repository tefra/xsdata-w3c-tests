from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-1-NS"


class NistschemaSvIvAtomicNegativeIntegerEnumeration1Type(Enum):
    """
    :cvar VALUE_MINUS_799584049274:
    :cvar VALUE_MINUS_43086541125:
    :cvar VALUE_MINUS_437:
    :cvar VALUE_MINUS_141901608775:
    :cvar VALUE_MINUS_4108769:
    :cvar VALUE_MINUS_965719538530:
    :cvar VALUE_MINUS_9896:
    :cvar VALUE_MINUS_12671901386817929:
    """
    VALUE_MINUS_799584049274 = -799584049274
    VALUE_MINUS_43086541125 = -43086541125
    VALUE_MINUS_437 = -437
    VALUE_MINUS_141901608775 = -141901608775
    VALUE_MINUS_4108769 = -4108769
    VALUE_MINUS_965719538530 = -965719538530
    VALUE_MINUS_9896 = -9896
    VALUE_MINUS_12671901386817929 = -12671901386817929


@dataclass
class NistschemaSvIvAtomicNegativeIntegerEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNegativeIntegerEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
