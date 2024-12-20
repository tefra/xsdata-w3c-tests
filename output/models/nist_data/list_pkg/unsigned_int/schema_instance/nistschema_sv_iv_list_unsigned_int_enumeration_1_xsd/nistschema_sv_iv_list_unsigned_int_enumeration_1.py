from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-enumeration-1-NS"


class NistschemaSvIvListUnsignedIntEnumeration1Type(Enum):
    VALUE_4868_1_6932_134_22820202_4294967295_2028084_551545731 = (
        4868,
        1,
        6932,
        134,
        22820202,
        4294967295,
        2028084,
        551545731,
    )
    VALUE_712_87610_217_220985_80_17413527_7892606_8500608_3425030 = (
        712,
        87610,
        217,
        220985,
        80,
        17413527,
        7892606,
        8500608,
        3425030,
    )
    VALUE_6_73106868_74019_735_41438_36_52_87003028_50 = (
        6,
        73106868,
        74019,
        735,
        41438,
        36,
        52,
        87003028,
        50,
    )
    VALUE_5_557_265202817_88588_919_124_18304833_33960725_143_128 = (
        5,
        557,
        265202817,
        88588,
        919,
        124,
        18304833,
        33960725,
        143,
        128,
    )
    VALUE_90099_3376636_3805538_478357794_33563300_67_26_569_8608 = (
        90099,
        3376636,
        3805538,
        478357794,
        33563300,
        67,
        26,
        569,
        8608,
    )
    VALUE_42_49_855434752_2841_4294967295_7144053_610423_89027659_37748_4278608 = (
        42,
        49,
        855434752,
        2841,
        4294967295,
        7144053,
        610423,
        89027659,
        37748,
        4278608,
    )
    VALUE_123_72091_18679_9588_55205584 = (
        123,
        72091,
        18679,
        9588,
        55205584,
    )
    VALUE_7963011_396579936_4294967295_2317919_9609_636853069_44268631_36044_948330576 = (
        7963011,
        396579936,
        4294967295,
        2317919,
        9609,
        636853069,
        44268631,
        36044,
        948330576,
    )
    VALUE_4597162_65562535_5577_60118_64001597_9065_13421 = (
        4597162,
        65562535,
        5577,
        60118,
        64001597,
        9065,
        13421,
    )


@dataclass
class NistschemaSvIvListUnsignedIntEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-enumeration-1-NS"

    value: Optional[NistschemaSvIvListUnsignedIntEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
