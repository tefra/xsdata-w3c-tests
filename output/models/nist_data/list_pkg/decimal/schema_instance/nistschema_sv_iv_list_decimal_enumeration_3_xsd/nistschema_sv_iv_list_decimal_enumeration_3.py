from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-enumeration-3-NS"


class NistschemaSvIvListDecimalEnumeration3Type(Enum):
    VALUE_88318_75274_79489370_40_370133690139_74095692869_3913496_82181079315_992178_41451465_53349939_633_8_89588_062664 = (
        Decimal("-88318.75274"),
        Decimal("-79489370"),
        Decimal("40.370133690139"),
        Decimal("74095692869.3913496"),
        Decimal("-82181079315.992178"),
        Decimal("-41451465.53349939"),
        Decimal("-633.8"),
        Decimal("89588.062664"),
    )
    VALUE_7_0_71268_6361_1_20229_87_5779346983_0_1920_64013397402_0_231661588810895_116_86 = (
        Decimal("7"),
        Decimal("-0.71268"),
        Decimal("-6361.1"),
        Decimal("20229.87"),
        Decimal("-5779346983.0"),
        Decimal("1920.64013397402"),
        Decimal("-0.231661588810895"),
        Decimal("-116.86"),
    )
    VALUE_0_9_471_64354_38_0_379_9245465891_2926579_353695_749542226_14_621597110_9_3795_580_44055841979 = (
        Decimal("0.9"),
        Decimal("-471.64354"),
        Decimal("-38.0"),
        Decimal("-379"),
        Decimal("-9245465891.2926579"),
        Decimal("-353695.749542226"),
        Decimal("14.621597110"),
        Decimal("-9.3795"),
        Decimal("580.44055841979"),
    )
    VALUE_6_2_19597104460610_503_9659_245559_5_705226077419_54734728157608_4809_2_841 = (
        Decimal("-6.2"),
        Decimal("-19597104460610.503"),
        Decimal("9659.245559"),
        Decimal("-5.705226077419"),
        Decimal("54734728157608.4809"),
        Decimal("2.841"),
    )
    VALUE_908593695648_51455_4_11233_53052_61_3193_392887_44824_443 = (
        Decimal("908593695648.51455"),
        Decimal("4.11233"),
        Decimal("53052.61"),
        Decimal("-3193.392887"),
        Decimal("44824.443"),
    )
    VALUE_79717_8430313_85445384_33429_160257990_9537_5827586952_8_9_873375466979_24_77_35471654965_75_5_48_825_72644_5_6613 = (
        Decimal("79717.8430313"),
        Decimal("-85445384.33429"),
        Decimal("160257990.9537"),
        Decimal("5827586952.8"),
        Decimal("9.873375466979"),
        Decimal("24.77"),
        Decimal("-35471654965.75"),
        Decimal("-5.48"),
        Decimal("825.72644"),
        Decimal("-5.6613"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-decimal-enumeration-3-NS"

    value: NistschemaSvIvListDecimalEnumeration3Type = field(
        metadata={
            "required": True,
        }
    )
