from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-enumeration-2-NS"


class NistschemaSvIvAtomicLongEnumeration2Type(Enum):
    """
    :cvar VALUE_MINUS_36983185:
    :cvar VALUE_MINUS_4958442914:
    :cvar VALUE_MINUS_530271545:
    :cvar VALUE_MINUS_53330603926218023:
    :cvar VALUE_MINUS_60196439767:
    :cvar VALUE_29044724:
    :cvar VALUE_528615:
    :cvar VALUE_649699813723:
    """
    VALUE_MINUS_36983185 = -36983185
    VALUE_MINUS_4958442914 = -4958442914
    VALUE_MINUS_530271545 = -530271545
    VALUE_MINUS_53330603926218023 = -53330603926218023
    VALUE_MINUS_60196439767 = -60196439767
    VALUE_29044724 = 29044724
    VALUE_528615 = 528615
    VALUE_649699813723 = 649699813723


@dataclass
class NistschemaSvIvAtomicLongEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-long-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicLongEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )