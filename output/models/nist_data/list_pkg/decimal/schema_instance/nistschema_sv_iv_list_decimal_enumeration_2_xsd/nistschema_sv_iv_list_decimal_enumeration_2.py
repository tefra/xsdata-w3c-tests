from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-enumeration-2-NS"


class NistschemaSvIvListDecimalEnumeration2Type(Enum):
    VALUE_19_022665803_39366424076_7_6_10155_603261_15_35246638200058_0_868374425939_76144 = (
        Decimal("19.022665803"),
        Decimal("39366424076.7"),
        Decimal("6.10155"),
        Decimal("-603261.15"),
        Decimal("-35246638200058.0"),
        Decimal("868374425939.76144"),
    )
    VALUE_54_83021630_15_0_0_4_12677012_307369_5_1_352_37733_508711986951_572775519_7755_2889389618998_039 = (
        Decimal("-54.83021630"),
        Decimal("-15.0"),
        Decimal("-0.4"),
        Decimal("-12677012.307369"),
        Decimal("5.1"),
        Decimal("-352"),
        Decimal("-37733.508711986951"),
        Decimal("572775519.7755"),
        Decimal("2889389618998.039"),
    )
    VALUE_1_88_8_1_4373_05898_65197_5_5_1_38588405711_59_9588103_7 = (
        Decimal("-1.88"),
        Decimal("-8.1"),
        Decimal("4373.05898"),
        Decimal("-65197.5"),
        Decimal("5.1"),
        Decimal("-38588405711.59"),
        Decimal("-9588103.7"),
    )
    VALUE_6_37741_3_26172_8442649493_7_14484019_103408_6482101_272_7617992_77173_55_036_75551579319923_86_4 = (
        Decimal("6.37741"),
        Decimal("-3.26172"),
        Decimal("-8442649493.7"),
        Decimal("-14484019.103408"),
        Decimal("-6482101.272"),
        Decimal("7617992.77173"),
        Decimal("55.036"),
        Decimal("-75551579319923"),
        Decimal("-86.4"),
    )
    VALUE_12_62875524_68871_029178497_10_7_1_0659_10246907606_46_14_3749789 = (
        Decimal("-12.62875524"),
        Decimal("-68871.029178497"),
        Decimal("-10.7"),
        Decimal("1.0659"),
        Decimal("-10246907606.46"),
        Decimal("-14.3749789"),
    )
    VALUE_459_33869440_1243910124960_6987_5447176501_84_4506438757795_7_72_016564461583_210_41033_0_3_8_9743338807462_80113843546788665_5_9443298_950048 = (
        Decimal("-459.33869440"),
        Decimal("-1243910124960.6987"),
        Decimal("5447176501.84"),
        Decimal("-4506438757795.7"),
        Decimal("-72.016564461583"),
        Decimal("-210.41033"),
        Decimal("-0.3"),
        Decimal("-8.9743338807462"),
        Decimal("80113843546788665.5"),
        Decimal("-9443298.950048"),
    )
    VALUE_8_8_43939607_37914_19153865475_5839_1_1_5_162_35_4_2_360_65_412474_539322473_1 = (
        Decimal("8"),
        Decimal("-8.43939607"),
        Decimal("37914.19153865475"),
        Decimal("5839.1"),
        Decimal("-1.5"),
        Decimal("-162.35"),
        Decimal("-4"),
        Decimal("-2.360"),
        Decimal("65.412474"),
        Decimal("-539322473.1"),
    )
    VALUE_382_2_8384_56_7304025153_946616_719_2_1558_272232170_8305_163_584 = (
        Decimal("-382.2"),
        Decimal("-8384.56"),
        Decimal("-7304025153.946616"),
        Decimal("-719.2"),
        Decimal("1558.272232170"),
        Decimal("8305.163"),
        Decimal("-584"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListDecimalEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-decimal-enumeration-2-NS"

    value: NistschemaSvIvListDecimalEnumeration2Type = field()
