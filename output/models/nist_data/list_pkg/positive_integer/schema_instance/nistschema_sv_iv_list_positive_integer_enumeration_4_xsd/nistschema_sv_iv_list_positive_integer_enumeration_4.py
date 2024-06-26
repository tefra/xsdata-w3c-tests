from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-enumeration-4-NS"


class NistschemaSvIvListPositiveIntegerEnumeration4Type(Enum):
    VALUE_1260843646755_66538312_552054554_44295580377693799_8469012_6169553815191437_45589233396360151_677735 = (
        1260843646755,
        66538312,
        552054554,
        44295580377693799,
        8469012,
        6169553815191437,
        45589233396360151,
        677735,
    )
    VALUE_811220561388005_796541_8953815245343_908988246_242165_80882499028_3532798597_4573927792589_81622650964136 = (
        811220561388005,
        796541,
        8953815245343,
        908988246,
        242165,
        80882499028,
        3532798597,
        4573927792589,
        81622650964136,
    )
    VALUE_15519_1479511015721408_65963958302564_858885377537_2098600_90510114918804329 = (
        15519,
        1479511015721408,
        65963958302564,
        858885377537,
        2098600,
        90510114918804329,
    )
    VALUE_276920496949_78_65181553_56526726446357_3002807196_590203444158840_94090_116915776266770632 = (
        276920496949,
        78,
        65181553,
        56526726446357,
        3002807196,
        590203444158840,
        94090,
        116915776266770632,
    )
    VALUE_76701_107081562_395653_308457773500_2107564_535537_3119995803 = (
        76701,
        107081562,
        395653,
        308457773500,
        2107564,
        535537,
        3119995803,
    )
    VALUE_3315_214227539944891_4894191880925_2476_88904_79_43584343_9288603084373_21706573558 = (
        3315,
        214227539944891,
        4894191880925,
        2476,
        88904,
        79,
        43584343,
        9288603084373,
        21706573558,
    )


@dataclass
class NistschemaSvIvListPositiveIntegerEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-enumeration-4-NS"

    value: Optional[NistschemaSvIvListPositiveIntegerEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
