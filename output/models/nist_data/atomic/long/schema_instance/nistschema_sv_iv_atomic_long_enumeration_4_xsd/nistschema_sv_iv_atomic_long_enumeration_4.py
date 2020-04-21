from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-4-NS"


class NistschemaSvIvAtomicLongEnumeration4Type(Enum):
    """
    :cvar VALUE_MINUS_19024765988335756:
    :cvar VALUE_MINUS_2295090265679:
    :cvar VALUE_MINUS_245446:
    :cvar VALUE_MINUS_52501609699:
    :cvar VALUE_MINUS_902030968896:
    :cvar VALUE_MINUS_97146741275:
    :cvar VALUE_62317068276:
    :cvar VALUE_698832321694:
    :cvar VALUE_9289163707500556:
    :cvar VALUE_947653025590775:
    """
    VALUE_MINUS_19024765988335756 = -19024765988335756
    VALUE_MINUS_2295090265679 = -2295090265679
    VALUE_MINUS_245446 = -245446
    VALUE_MINUS_52501609699 = -52501609699
    VALUE_MINUS_902030968896 = -902030968896
    VALUE_MINUS_97146741275 = -97146741275
    VALUE_62317068276 = 62317068276
    VALUE_698832321694 = 698832321694
    VALUE_9289163707500556 = 9289163707500556
    VALUE_947653025590775 = 947653025590775


@dataclass
class NistschemaSvIvAtomicLongEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicLongEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
