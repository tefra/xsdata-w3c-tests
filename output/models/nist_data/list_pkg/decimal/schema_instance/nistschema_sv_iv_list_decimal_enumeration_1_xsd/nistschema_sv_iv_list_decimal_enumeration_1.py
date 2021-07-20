from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-enumeration-1-NS"


class NistschemaSvIvListDecimalEnumeration1Type(Enum):
    VALUE_8_0660962264022095_0_56_504_50017438537553_41162572200_6_918_7_7_2 = (
            Decimal("8.0660962264022095"),
            Decimal("0.56"),
            Decimal("-504.50017438537553"),
            Decimal("41162572200.6"),
            Decimal("918.7"),
            Decimal("-7.2"),
        )
    VALUE_4845_79257872999_8_993_219753_09629_7432_5473_3_3436417_6_80210_39 = (
            Decimal("-4845.79257872999"),
            Decimal("-8.993"),
            Decimal("-219753.09629"),
            Decimal("-7432.5473"),
            Decimal("-3.3436417"),
            Decimal("-6"),
            Decimal("80210.39"),
        )
    VALUE_0_65_49_911645736975396_9_23939_64_1523_257209965_89463 = (
            Decimal("-0.65"),
            Decimal("-49.911645736975396"),
            Decimal("-9.23939"),
            Decimal("64.1523"),
            Decimal("-257209965.89463"),
        )
    VALUE_99978_341_0_4_672_13674_764191985_992_115_1_523411606084_958475378_2982_87607_2024 = (
            Decimal("99978.341"),
            Decimal("0.4"),
            Decimal("-672.13674"),
            Decimal("764191985.992"),
            Decimal("115"),
            Decimal("1.523411606084"),
            Decimal("-958475378.2982"),
            Decimal("87607.2024"),
        )
    VALUE_8_7_40827333981_15834_85328_0078_224147698_039_84349014_8934_0_898 = (
            Decimal("8.7"),
            Decimal("-40827333981.15834"),
            Decimal("85328.0078"),
            Decimal("-224147698.039"),
            Decimal("84349014.8934"),
            Decimal("0.898"),
        )
    VALUE_43_068990388774430_15385_04_68458_4313356029_120_9_1093_84288648700652_1800_64_46026 = (
            Decimal("43.068990388774430"),
            Decimal("15385.04"),
            Decimal("68458.4313356029"),
            Decimal("120"),
            Decimal("9.1093"),
            Decimal("84288648700652.1800"),
            Decimal("64.46026"),
        )
    VALUE_4250288_104_272_327746_8234_72_73376513_0_18040677_9_3 = (
            Decimal("4250288.104"),
            Decimal("272"),
            Decimal("327746.8234"),
            Decimal("-72.73376513"),
            Decimal("0.18040677"),
            Decimal("9.3"),
        )


@dataclass
class NistschemaSvIvListDecimalEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-decimal-enumeration-1-NS"

    value: Optional[NistschemaSvIvListDecimalEnumeration1Type] = field(
        default=None
    )
