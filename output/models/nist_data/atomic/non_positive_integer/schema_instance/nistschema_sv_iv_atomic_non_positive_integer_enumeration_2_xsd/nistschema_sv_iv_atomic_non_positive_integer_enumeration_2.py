from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-2-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration2Type(Enum):
    """
    :cvar VALUE_MINUS_559044:
    :cvar VALUE_MINUS_69:
    :cvar VALUE_MINUS_40316819:
    :cvar VALUE_MINUS_351:
    :cvar VALUE_MINUS_712506:
    :cvar VALUE_MINUS_118:
    :cvar VALUE_MINUS_748:
    :cvar VALUE_MINUS_23407037:
    :cvar VALUE_MINUS_19:
    :cvar VALUE_MINUS_677813318583757:
    """
    VALUE_MINUS_559044 = -559044
    VALUE_MINUS_69 = -69
    VALUE_MINUS_40316819 = -40316819
    VALUE_MINUS_351 = -351
    VALUE_MINUS_712506 = -712506
    VALUE_MINUS_118 = -118
    VALUE_MINUS_748 = -748
    VALUE_MINUS_23407037 = -23407037
    VALUE_MINUS_19 = -19
    VALUE_MINUS_677813318583757 = -677813318583757


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNonPositiveIntegerEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
