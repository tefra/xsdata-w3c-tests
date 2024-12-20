from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-enumeration-1-NS"


class NistschemaSvIvListIntEnumeration1Type(Enum):
    VALUE_89920_270_654_8059163_5902_9583334 = (
        89920,
        -270,
        -654,
        8059163,
        5902,
        -9583334,
    )
    VALUE_14874707_4781_8716603_7782_8189_23191_8611110_98_8967801 = (
        14874707,
        4781,
        8716603,
        7782,
        8189,
        -23191,
        -8611110,
        -98,
        8967801,
    )
    VALUE_7482_903433_328395_965698_52_4_86 = (
        7482,
        -903433,
        328395,
        -965698,
        -52,
        -4,
        -86,
    )
    VALUE_97_83231_2451_12_670313_74235_275_960 = (
        97,
        83231,
        -2451,
        12,
        -670313,
        -74235,
        -275,
        -960,
    )
    VALUE_78262_77262644_524610911_840393_58_30_86197727 = (
        -78262,
        77262644,
        -524610911,
        840393,
        58,
        30,
        86197727,
    )
    VALUE_905267_764266_29391_35795_28_559 = (
        -905267,
        -764266,
        -29391,
        35795,
        28,
        559,
    )
    VALUE_40634337_33389_4712_8370_5448132_2844582_3335_754313570_8363613_539 = (
        -40634337,
        33389,
        -4712,
        -8370,
        -5448132,
        2844582,
        3335,
        754313570,
        -8363613,
        -539,
    )
    VALUE_928863_9724_916_2147483648_18032_58482838 = (
        928863,
        -9724,
        916,
        -2147483648,
        -18032,
        58482838,
    )
    VALUE_95_56_2158094_45_886060_85760821_44951970 = (
        95,
        -56,
        -2158094,
        -45,
        -886060,
        85760821,
        -44951970,
    )


@dataclass
class NistschemaSvIvListIntEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-int-enumeration-1-NS"

    value: Optional[NistschemaSvIvListIntEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
