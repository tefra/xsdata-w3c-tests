from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-enumeration-3-NS"


class NistschemaSvIvListIntEnumeration3Type(Enum):
    VALUE_935_4735_36891_40998_592625956 = (
        935,
        4735,
        -36891,
        40998,
        592625956,
    )
    VALUE_25_82965170_3654965_1620383_2952092_75113_674 = (
        -25,
        -82965170,
        3654965,
        -1620383,
        -2952092,
        75113,
        -674,
    )
    VALUE_9536118_16855921_3648952_503_2147483648_3538013_5431840 = (
        9536118,
        -16855921,
        3648952,
        503,
        -2147483648,
        3538013,
        -5431840,
    )
    VALUE_8_5_458_480_8805_2147483648_2633 = (
        -8,
        5,
        -458,
        -480,
        -8805,
        -2147483648,
        2633,
    )
    VALUE_1014054369_9112_3638834_214039_7908524_243298 = (
        1014054369,
        9112,
        3638834,
        214039,
        -7908524,
        243298,
    )
    VALUE_2147483647_89308_4_914147703_26_2312_244 = (
        2147483647,
        -89308,
        -4,
        -914147703,
        26,
        2312,
        244,
    )
    VALUE_7983103_97645_6193_589_65968 = (
        7983103,
        97645,
        -6193,
        -589,
        65968,
    )
    VALUE_6259_37_32249_813635813_69_933 = (
        -6259,
        -37,
        -32249,
        813635813,
        -69,
        933,
    )


@dataclass
class NistschemaSvIvListIntEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-int-enumeration-3-NS"

    value: Optional[NistschemaSvIvListIntEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
