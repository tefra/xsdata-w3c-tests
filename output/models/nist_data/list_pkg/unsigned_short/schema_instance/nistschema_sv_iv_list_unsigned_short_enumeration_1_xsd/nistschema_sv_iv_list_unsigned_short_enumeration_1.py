from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-enumeration-1-NS"


class NistschemaSvIvListUnsignedShortEnumeration1Type(Enum):
    """
    :cvar VALUE_3137_19_2_9139_129_15:
    :cvar VALUE_42_33691_48979_99_406_3072_9318_428_22:
    :cvar VALUE_52_92_464_45351_276_731:
    :cvar VALUE_57_65535_7460_419_83:
    :cvar VALUE_6131_43_926_88_49_727_71_4072_1805_18291:
    :cvar VALUE_65535_626_1696_8_76_3716_88_921:
    :cvar VALUE_6_425_3292_540_23_58748_1053:
    """
    VALUE_3137_19_2_9139_129_15 = "3137 19 2 9139 129 15"
    VALUE_42_33691_48979_99_406_3072_9318_428_22 = "42 33691 48979 99 406 3072 9318 428 22"
    VALUE_52_92_464_45351_276_731 = "52 92 464 45351 276 731"
    VALUE_57_65535_7460_419_83 = "57 65535 7460 419 83"
    VALUE_6131_43_926_88_49_727_71_4072_1805_18291 = "6131 43 926 88 49 727 71 4072 1805 18291"
    VALUE_65535_626_1696_8_76_3716_88_921 = "65535 626 1696 8 76 3716 88 921"
    VALUE_6_425_3292_540_23_58748_1053 = "6 425 3292 540 23 58748 1053"


@dataclass
class NistschemaSvIvListUnsignedShortEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-enumeration-1-NS"

    value: Optional[NistschemaSvIvListUnsignedShortEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
