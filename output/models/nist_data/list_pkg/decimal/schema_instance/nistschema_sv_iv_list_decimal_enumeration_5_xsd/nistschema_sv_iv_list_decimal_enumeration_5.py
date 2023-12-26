from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-enumeration-5-NS"


class NistschemaSvIvListDecimalEnumeration5Type(Enum):
    VALUE_69_3817003_806533146393_14244_7_692_24_9875727835_21_0_272460498067008671_789_1_580436548_481858549_88_5294419203 = (
        Decimal("-69.3817003"),
        Decimal("-806533146393.14244"),
        Decimal("-7.692"),
        Decimal("24.9875727835"),
        Decimal("-21"),
        Decimal("-0.272460498067008671"),
        Decimal("789.1"),
        Decimal("580436548.481858549"),
        Decimal("-88.5294419203"),
    )
    VALUE_185053587719_80_794_5_43507402_5874_3675248638_27067_480489_97043436573497932_0 = (
        Decimal("-185053587719.80"),
        Decimal("-794"),
        Decimal("-5.43507402"),
        Decimal("-5874.3675248638"),
        Decimal("-27067.480489"),
        Decimal("97043436573497932.0"),
    )
    VALUE_42_12164620414052_54707_925170_674092163_2667417_7840_18_112787_7433_33_9_5_1662400_522081_438918_1_1 = (
        Decimal("42.12164620414052"),
        Decimal("54707.925170"),
        Decimal("-674092163.2667417"),
        Decimal("7840.18"),
        Decimal("-112787.7433"),
        Decimal("-33.9"),
        Decimal("5.1662400"),
        Decimal("522081.438918"),
        Decimal("-1.1"),
    )
    VALUE_0_9679_11_93_55376_858_67_49397_5889105522594_120_17635_60_74_3256_344002_1962231 = (
        Decimal("-0.9679"),
        Decimal("-11.93"),
        Decimal("55376.858"),
        Decimal("67.49397"),
        Decimal("5889105522594.120"),
        Decimal("-17635.60"),
        Decimal("74.3256"),
        Decimal("-344002.1962231"),
    )
    VALUE_980968517543_7_1_66_0_9_36_60485_855511097386_6 = (
        Decimal("-980968517543.7"),
        Decimal("-1.66"),
        Decimal("0.9"),
        Decimal("-36.60485"),
        Decimal("-855511097386.6"),
    )
    VALUE_677_8137_953196_72765_500799323_66_3301179007_728_471755663018_9327833_3550357_8298052_89_320163069_05121_41035356_53_0_944465388 = (
        Decimal("677.8137"),
        Decimal("953196.72765"),
        Decimal("-500799323"),
        Decimal("66.3301179007"),
        Decimal("-728.471755663018"),
        Decimal("9327833.3550357"),
        Decimal("8298052.89"),
        Decimal("320163069.05121"),
        Decimal("41035356.53"),
        Decimal("0.944465388"),
    )
    VALUE_37_74_9412497_567185408_32_2_89122_6_0_5_140_36420183149 = (
        Decimal("37.74"),
        Decimal("9412497.567185408"),
        Decimal("-32.2"),
        Decimal("-89122.6"),
        Decimal("-0.5"),
        Decimal("140.36420183149"),
    )


@dataclass
class NistschemaSvIvListDecimalEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-decimal-enumeration-5-NS"

    value: Optional[NistschemaSvIvListDecimalEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
