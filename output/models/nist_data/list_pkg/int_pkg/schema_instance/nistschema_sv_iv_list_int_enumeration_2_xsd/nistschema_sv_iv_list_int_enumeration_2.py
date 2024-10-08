from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-enumeration-2-NS"


class NistschemaSvIvListIntEnumeration2Type(Enum):
    VALUE_75348_588606350_79999482_6093_49647_61283_635507079_55013215_946033653 = (
        75348,
        -588606350,
        -79999482,
        6093,
        49647,
        -61283,
        635507079,
        55013215,
        946033653,
    )
    VALUE_48780_63265451_19231_742_46_8697 = (
        -48780,
        -63265451,
        -19231,
        742,
        46,
        8697,
    )
    VALUE_59_2583845_233715779_493_4801_89609733_590_240940_2147483648_26718 = (
        59,
        2583845,
        233715779,
        493,
        4801,
        89609733,
        -590,
        240940,
        -2147483648,
        -26718,
    )
    VALUE_324287644_711_1541_523_779_1833261376_2241_49556848_23247 = (
        -324287644,
        -711,
        1541,
        -523,
        -779,
        1833261376,
        2241,
        -49556848,
        -23247,
    )
    VALUE_4446_721871790_52_2147483647_109429 = (
        -4446,
        -721871790,
        -52,
        2147483647,
        -109429,
    )
    VALUE_4186_300_3274_8627789_7232438_67136_9121_12 = (
        -4186,
        -300,
        3274,
        -8627789,
        -7232438,
        67136,
        -9121,
        -12,
    )
    VALUE_69469459_2147483647_4846086_497_10_3249 = (
        69469459,
        2147483647,
        4846086,
        497,
        10,
        3249,
    )


@dataclass
class NistschemaSvIvListIntEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-int-enumeration-2-NS"

    value: Optional[NistschemaSvIvListIntEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
