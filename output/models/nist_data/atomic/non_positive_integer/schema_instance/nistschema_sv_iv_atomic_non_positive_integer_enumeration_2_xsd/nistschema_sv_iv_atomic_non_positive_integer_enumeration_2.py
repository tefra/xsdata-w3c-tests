from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-2-NS"


class NistschemaSvIvAtomicNonPositiveIntegerEnumeration2Type(Enum):
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
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicNonPositiveIntegerEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
