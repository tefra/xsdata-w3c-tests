from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-2-NS"


class NistschemaSvIvListNonPositiveIntegerEnumeration2Type(Enum):
    VALUE_787712621_4_822955050976095_666_1163536251774_89998589564980_508246411_2554095_841315300 = (
            -787712621,
            -4,
            -822955050976095,
            -666,
            -1163536251774,
            -89998589564980,
            -508246411,
            -2554095,
            -841315300,
        )
    VALUE_700406708171874_39298_112713199_92596807991668_64994_312012966908252975 = (
            -700406708171874,
            -39298,
            -112713199,
            -92596807991668,
            -64994,
            -312012966908252975,
        )
    VALUE_57185920250813515_1904611123176_620560846373_24_16075684897994_7554_7163149634271 = (
            -57185920250813515,
            -1904611123176,
            -620560846373,
            -24,
            -16075684897994,
            -7554,
            -7163149634271,
        )
    VALUE_9239_815_21888354477232918_4504938332463781_71_859152874 = (
            -9239,
            -815,
            -21888354477232918,
            -4504938332463781,
            -71,
            -859152874,
        )
    VALUE_829370_2978657076025_50181259605290007_829728_1117522_36_516 = (
            -829370,
            -2978657076025,
            -50181259605290007,
            -829728,
            -1117522,
            -36,
            -516,
        )


@dataclass
class NistschemaSvIvListNonPositiveIntegerEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-nonPositiveInteger-enumeration-2-NS"

    value: Optional[NistschemaSvIvListNonPositiveIntegerEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
