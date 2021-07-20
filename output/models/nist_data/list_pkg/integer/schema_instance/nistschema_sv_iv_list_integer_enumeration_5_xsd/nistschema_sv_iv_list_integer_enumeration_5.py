from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-enumeration-5-NS"


class NistschemaSvIvListIntegerEnumeration5Type(Enum):
    VALUE_50837143516081_847710276125945_65_9903941903200123_4320_6922 = (
            50837143516081,
            847710276125945,
            65,
            9903941903200123,
            -4320,
            -6922,
        )
    VALUE_3066310768_38_27_67562577016_97528798718514808_59378588 = (
            3066310768,
            -38,
            -27,
            -67562577016,
            97528798718514808,
            -59378588,
        )
    VALUE_9203_51230954488_1351589649533_39177887523096_4954055065_991883_265849053855 = (
            9203,
            51230954488,
            1351589649533,
            -39177887523096,
            4954055065,
            -991883,
            265849053855,
        )
    VALUE_871676_1157639603593011_23_332395177_12767_298482467175 = (
            871676,
            1157639603593011,
            23,
            -332395177,
            12767,
            298482467175,
        )
    VALUE_409022897_1588_415967941582_825_70049416_103584_778005173165675_76 = (
            -409022897,
            1588,
            -415967941582,
            825,
            70049416,
            -103584,
            -778005173165675,
            -76,
        )
    VALUE_5144664_8695843825483700_750_995111_748016961_25533_9107965793684688 = (
            5144664,
            -8695843825483700,
            750,
            -995111,
            748016961,
            -25533,
            -9107965793684688,
        )


@dataclass
class NistschemaSvIvListIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-integer-enumeration-5-NS"

    value: Optional[NistschemaSvIvListIntegerEnumeration5Type] = field(
        default=None
    )
