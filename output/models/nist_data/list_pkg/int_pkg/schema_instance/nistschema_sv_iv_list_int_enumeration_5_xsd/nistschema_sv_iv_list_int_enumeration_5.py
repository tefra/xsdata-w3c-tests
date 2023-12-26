from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-enumeration-5-NS"


class NistschemaSvIvListIntEnumeration5Type(Enum):
    VALUE_6474139_375_3373754_74_85259_6079_47300 = (
        6474139,
        375,
        3373754,
        -74,
        85259,
        -6079,
        -47300,
    )
    VALUE_288418594_358_461507010_21102289_554446_950_1418908_3313619_2147483647_1608 = (
        -288418594,
        358,
        461507010,
        -21102289,
        554446,
        950,
        -1418908,
        -3313619,
        2147483647,
        -1608,
    )
    VALUE_4240109_7851790_28268_649069_4171111_242_8722_1633 = (
        4240109,
        7851790,
        -28268,
        -649069,
        4171111,
        242,
        -8722,
        1633,
    )
    VALUE_91237550_2147483647_87853_48814_29179_74 = (
        -91237550,
        2147483647,
        -87853,
        48814,
        29179,
        -74,
    )
    VALUE_71440047_6547482_15_8416105_89809817 = (
        71440047,
        -6547482,
        -15,
        8416105,
        89809817,
    )
    VALUE_60_2147483647_4800260_875988_31776479_569419_8076_91838_351082551_950747868 = (
        60,
        2147483647,
        4800260,
        -875988,
        31776479,
        569419,
        8076,
        91838,
        -351082551,
        950747868,
    )
    VALUE_5200583_7760_2147483648_1034_67856533 = (
        -5200583,
        7760,
        -2147483648,
        -1034,
        -67856533,
    )
    VALUE_1260_25547308_57_142998_17843594_1428_2656_2147483647_599986389_8857201 = (
        -1260,
        -25547308,
        57,
        -142998,
        -17843594,
        1428,
        -2656,
        2147483647,
        -599986389,
        -8857201,
    )


@dataclass
class NistschemaSvIvListIntEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-int-enumeration-5-NS"

    value: Optional[NistschemaSvIvListIntEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
