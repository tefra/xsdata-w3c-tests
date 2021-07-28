from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-enumeration-3-NS"


class NistschemaSvIvListUnsignedLongEnumeration3Type(Enum):
    VALUE_8_80892725_34966687977403_5171729959_2074699017206486_6965585773_5679075_2376188661537 = (
            8,
            80892725,
            34966687977403,
            5171729959,
            2074699017206486,
            6965585773,
            5679075,
            2376188661537,
        )
    VALUE_60_8826867_71_45_975554996_9544996351_4463_37554800356737927 = (
            60,
            8826867,
            71,
            45,
            975554996,
            9544996351,
            4463,
            37554800356737927,
        )
    VALUE_967528050895_875671210_1153563521_658291575881240_7602404492496775_357984609940_63206867507 = (
            967528050895,
            875671210,
            1153563521,
            658291575881240,
            7602404492496775,
            357984609940,
            63206867507,
        )
    VALUE_898716798402622_6033902128052_417857_450294120242153_18_10632036 = (
            898716798402622,
            6033902128052,
            417857,
            450294120242153,
            18,
            10632036,
        )
    VALUE_7091_5132422121_7319_4245_7581218140_49561029506_813092025_908229221590680_480655051621710405 = (
            7091,
            5132422121,
            7319,
            4245,
            7581218140,
            49561029506,
            813092025,
            908229221590680,
            480655051621710405,
        )
    VALUE_4142055732534304_7635_717_9178828842837_8899688890_569009129956880_22827234790_3325899 = (
            4142055732534304,
            7635,
            717,
            9178828842837,
            8899688890,
            569009129956880,
            22827234790,
            3325899,
        )


@dataclass
class NistschemaSvIvListUnsignedLongEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-enumeration-3-NS"

    value: Optional[NistschemaSvIvListUnsignedLongEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
