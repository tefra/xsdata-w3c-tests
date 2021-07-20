from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-decimal-enumeration-4-NS"


class NistschemaSvIvListDecimalEnumeration4Type(Enum):
    VALUE_0_274020448228_9_74_9_6_1751550782945_7321_0_6951282236080014_35699988_0_50015916 = (
            Decimal("0.274020448228"),
            Decimal("-9.74"),
            Decimal("-9.6"),
            Decimal("1751550782945.7321"),
            Decimal("-0.6951282236080014"),
            Decimal("35699988"),
            Decimal("0.50015916"),
        )
    VALUE_3_8_875475206_869_0_45556_1_9962504013_683230844_813 = (
            Decimal("3.8"),
            Decimal("875475206.869"),
            Decimal("0.45556"),
            Decimal("1.9962504013"),
            Decimal("-683230844.813"),
        )
    VALUE_506_1902_2_1_7027728_3_670916_28960686_629_622_7997_019_40951400292_688 = (
            Decimal("-506.1902"),
            Decimal("2.1"),
            Decimal("7027728.3"),
            Decimal("-670916.28960686"),
            Decimal("-629.622"),
            Decimal("-7997.019"),
            Decimal("40951400292.688"),
        )
    VALUE_31874_66228_5_8_7685005_31937997055_4_7_2206_59_9_7880954600_10_2_27 = (
            Decimal("31874.66228"),
            Decimal("5.8"),
            Decimal("7685005.31937997055"),
            Decimal("4.7"),
            Decimal("2206"),
            Decimal("-59.9"),
            Decimal("-7880954600.10"),
            Decimal("-2.27"),
        )
    VALUE_959_0569657154712_7097611965_4_137760903224251_16_7949_40273_805_8_853_5190310586_101813_560_30066433520 = (
            Decimal("-959.0569657154712"),
            Decimal("-7097611965.4"),
            Decimal("137760903224251.16"),
            Decimal("-7949.40273"),
            Decimal("-805"),
            Decimal("8.853"),
            Decimal("5190310586.101813"),
            Decimal("560.30066433520"),
        )
    VALUE_379560127126_91_1656393628_27572_384696_71397_7482_175_57_782725_0_38_9_1 = (
            Decimal("379560127126.91"),
            Decimal("1656393628.27572"),
            Decimal("384696.71397"),
            Decimal("-7482.175"),
            Decimal("-57.782725"),
            Decimal("0.38"),
            Decimal("9.1"),
        )
    VALUE_811_34077506_9380317_5_0_5206959546_5906251232123_430_90_587_15465962359_194097_432_0_436 = (
            Decimal("-811.34077506"),
            Decimal("9380317.5"),
            Decimal("0.5206959546"),
            Decimal("-5906251232123.430"),
            Decimal("-90"),
            Decimal("587.15465962359"),
            Decimal("-194097.432"),
            Decimal("-0.436"),
        )
    VALUE_2314_3_0_812_535_15_5307_854374820_9260615_865672_586_64841190_5762962413414323_1_2312_27676_550_81243_8136_19495400726 = (
            Decimal("-2314.3"),
            Decimal("0.812"),
            Decimal("535.15"),
            Decimal("5307.854374820"),
            Decimal("9260615.865672"),
            Decimal("586.64841190"),
            Decimal("5762962413414323.1"),
            Decimal("-2312.27676"),
            Decimal("550.81243"),
            Decimal("8136.19495400726"),
        )
    VALUE_19591_833610970_6335308382614_5861_573838_5209853_515_4287_34_7104_556433298_26888_296055_25814360122_5_565662083_3098_0 = (
            Decimal("-19591.833610970"),
            Decimal("6335308382614.5861"),
            Decimal("573838.5209853"),
            Decimal("515"),
            Decimal("-4287.34"),
            Decimal("7104.556433298"),
            Decimal("-26888"),
            Decimal("-296055.25814360122"),
            Decimal("-5.565662083"),
            Decimal("-3098.0"),
        )


@dataclass
class NistschemaSvIvListDecimalEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-decimal-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-decimal-enumeration-4-NS"

    value: Optional[NistschemaSvIvListDecimalEnumeration4Type] = field(
        default=None
    )
