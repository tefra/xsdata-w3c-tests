from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-3-NS"


class NistschemaSvIvAtomicNegativeIntegerEnumeration3Type(Enum):
    """
    :cvar VALUE_MINUS_13149:
    :cvar VALUE_MINUS_29566:
    :cvar VALUE_MINUS_51381660407640261:
    :cvar VALUE_MINUS_627946996321885664:
    :cvar VALUE_MINUS_6839697930198:
    :cvar VALUE_MINUS_74:
    :cvar VALUE_MINUS_78815123:
    :cvar VALUE_MINUS_923074469:
    :cvar VALUE_MINUS_99:
    """
    VALUE_MINUS_13149 = -13149
    VALUE_MINUS_29566 = -29566
    VALUE_MINUS_51381660407640261 = -51381660407640261
    VALUE_MINUS_627946996321885664 = -627946996321885664
    VALUE_MINUS_6839697930198 = -6839697930198
    VALUE_MINUS_74 = -74
    VALUE_MINUS_78815123 = -78815123
    VALUE_MINUS_923074469 = -923074469
    VALUE_MINUS_99 = -99


@dataclass
class NistschemaSvIvAtomicNegativeIntegerEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicNegativeIntegerEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )