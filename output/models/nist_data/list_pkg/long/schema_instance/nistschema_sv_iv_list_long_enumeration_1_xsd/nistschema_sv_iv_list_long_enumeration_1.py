from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-enumeration-1-NS"


class NistschemaSvIvListLongEnumeration1Type(Enum):
    """
    :cvar VALUE_271843373332464666_2233621498154969_913206_6213154277963098_3018729042566_31952446170020_65_33_395_7554348360:
    :cvar VALUE_331301399645876237_6768774690357174_22392_641769916857_9873626081_429364613406553_15198431658_7291133504_3956376:
    :cvar VALUE_356219_83244855376041315_32844_2722422603087550_97330623332_90460_284216443:
    :cvar VALUE_556_68987259131_444610540925_181727_138018422_584026870213947_763378913909_10_3302208_5375:
    :cvar VALUE_6476499953006163_302_9008_35073697_7_13_72214481:
    :cvar VALUE_96682429568362_87250076110547_695_245206134_12941351_897300496024_4421404032568:
    :cvar VALUE_357_68651875120_469893354707_79078874815317_9772809142048_21046004043341:
    :cvar VALUE_97643129479577_51390416_74571993607874_8593658_334716807952_6940143575216557_976181206907_74410094:
    """
    VALUE_271843373332464666_2233621498154969_913206_6213154277963098_3018729042566_31952446170020_65_33_395_7554348360 = "-271843373332464666 -2233621498154969 -913206 -6213154277963098 3018729042566 -31952446170020 65 -33 -395 7554348360"
    VALUE_331301399645876237_6768774690357174_22392_641769916857_9873626081_429364613406553_15198431658_7291133504_3956376 = "-331301399645876237 -6768774690357174 22392 -641769916857 -9873626081 -429364613406553 -15198431658 7291133504 3956376"
    VALUE_356219_83244855376041315_32844_2722422603087550_97330623332_90460_284216443 = "-356219 -83244855376041315 32844 -2722422603087550 97330623332 90460 284216443"
    VALUE_556_68987259131_444610540925_181727_138018422_584026870213947_763378913909_10_3302208_5375 = "-556 -68987259131 444610540925 181727 -138018422 -584026870213947 763378913909 -10 3302208 5375"
    VALUE_6476499953006163_302_9008_35073697_7_13_72214481 = "-6476499953006163 -302 -9008 -35073697 -7 13 72214481"
    VALUE_96682429568362_87250076110547_695_245206134_12941351_897300496024_4421404032568 = "-96682429568362 87250076110547 695 245206134 12941351 897300496024 4421404032568"
    VALUE_357_68651875120_469893354707_79078874815317_9772809142048_21046004043341 = "357 -68651875120 -469893354707 79078874815317 9772809142048 -21046004043341"
    VALUE_97643129479577_51390416_74571993607874_8593658_334716807952_6940143575216557_976181206907_74410094 = "97643129479577 51390416 74571993607874 8593658 334716807952 6940143575216557 -976181206907 74410094"


@dataclass
class NistschemaSvIvListLongEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-long-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-long-enumeration-1-NS"

    value: Optional[NistschemaSvIvListLongEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )