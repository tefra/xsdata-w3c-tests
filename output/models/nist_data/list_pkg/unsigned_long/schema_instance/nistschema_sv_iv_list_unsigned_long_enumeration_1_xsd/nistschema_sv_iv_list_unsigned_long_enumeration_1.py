from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-enumeration-1-NS"


class NistschemaSvIvListUnsignedLongEnumeration1Type(Enum):
    VALUE_221071704_740303242307_3355389142255_912904847828_8639692_52529073_46343_25810 = (
        221071704,
        740303242307,
        3355389142255,
        912904847828,
        8639692,
        52529073,
        46343,
        25810,
    )
    VALUE_954504251103496_6436438080417239_917_609554_9846 = (
        954504251103496,
        6436438080417239,
        917,
        609554,
        9846,
    )
    VALUE_2628606301_95575969407277_83095_1745662_6723369_21588352481_971645879987178_5940035208_501902 = (
        2628606301,
        95575969407277,
        83095,
        1745662,
        6723369,
        21588352481,
        971645879987178,
        5940035208,
        501902,
    )
    VALUE_35155970552_51182735_4070957407306294_364816_96493876244_855778493581_319102_95887 = (
        35155970552,
        51182735,
        4070957407306294,
        364816,
        96493876244,
        855778493581,
        319102,
        95887,
    )
    VALUE_60_1108831861712_55171926518900771_794183_94905 = (
        60,
        1108831861712,
        55171926518900771,
        794183,
        94905,
    )


@dataclass
class NistschemaSvIvListUnsignedLongEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-enumeration-1-NS"

    value: Optional[NistschemaSvIvListUnsignedLongEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
