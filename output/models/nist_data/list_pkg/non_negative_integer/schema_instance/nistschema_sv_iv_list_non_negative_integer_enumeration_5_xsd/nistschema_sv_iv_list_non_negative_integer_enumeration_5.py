from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-enumeration-5-NS"


class NistschemaSvIvListNonNegativeIntegerEnumeration5Type(Enum):
    VALUE_18573_9992315_526_6007323361359310_774685903454_90520629321230705 = (
        18573,
        9992315,
        526,
        6007323361359310,
        774685903454,
        90520629321230705,
    )
    VALUE_57678762_22130213556815_198_975099027_4428248949 = (
        57678762,
        22130213556815,
        198,
        975099027,
        4428248949,
    )
    VALUE_35140_6781079863_2798357647200_576060_4427984 = (
        35140,
        6781079863,
        2798357647200,
        576060,
        4427984,
    )
    VALUE_305_5206086908888591_7538948699436_2925620477493_880888727734_93459427 = (
        305,
        5206086908888591,
        7538948699436,
        2925620477493,
        880888727734,
        93459427,
    )
    VALUE_65622266297730_61598190898446_48_326_6263929283_10_832127328659_52 = (
        65622266297730,
        61598190898446,
        48,
        326,
        6263929283,
        10,
        832127328659,
        52,
    )
    VALUE_9145399451347302_455466479_576092987499099_6682475231744_255501259736_437_72416022400468_10091_1735673046913 = (
        9145399451347302,
        455466479,
        576092987499099,
        6682475231744,
        255501259736,
        437,
        72416022400468,
        10091,
        1735673046913,
    )


@dataclass(kw_only=True)
class NistschemaSvIvListNonNegativeIntegerEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-enumeration-5-NS"

    value: NistschemaSvIvListNonNegativeIntegerEnumeration5Type = field()
