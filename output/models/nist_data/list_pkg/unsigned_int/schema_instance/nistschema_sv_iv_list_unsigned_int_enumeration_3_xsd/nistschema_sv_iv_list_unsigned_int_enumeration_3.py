from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-enumeration-3-NS"


class NistschemaSvIvListUnsignedIntEnumeration3Type(Enum):
    VALUE_147421_266_720769_15238931_172933_689921_168178_114955 = "147421 266 720769 15238931 172933 689921 168178 114955"
    VALUE_253_1813_352989250_33635_72237_75297797_95161_601646_4294967295 = "253 1813 352989250 33635 72237 75297797 95161 601646 4294967295"
    VALUE_39246234_62307075_5021498_68771_644811_556630_87482065_65580182_23013 = "39246234 62307075 5021498 68771 644811 556630 87482065 65580182 23013"
    VALUE_64_91_8002815_478279250_788100 = "64 91 8002815 478279250 788100"
    VALUE_6577598_65939516_67021555_917_85_417_25830279_3464 = "6577598 65939516 67021555 917 85 417 25830279 3464"


@dataclass
class NistschemaSvIvListUnsignedIntEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-enumeration-3-NS"

    value: Optional[NistschemaSvIvListUnsignedIntEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
