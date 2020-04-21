from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v01"


class YMdenumeration(Enum):
    """
    :cvar VALUE_P5_DT3_S:
    :cvar VALUE_PT43_M4_2_S:
    :cvar P2_D:
    :cvar PT54_H3_M2_3_S:
    """
    VALUE_P5_DT3_S = "-P5DT3S"
    VALUE_PT43_M4_2_S = "-PT43M4.2S"
    P2_D = "P2D"
    PT54_H3_M2_3_S = "PT54H3M2.3S"


@dataclass
class Root:
    """
    :ivar ely_mdtype:
    :ivar ely_mdenumeration:
    :ivar ely_mdmin_max_inclusive:
    :ivar ely_mdmin_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v01"

    ely_mdtype: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDType",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    ely_mdenumeration: List[YMdenumeration] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDEnumeration",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    ely_mdmin_max_inclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDMinMaxInclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_inclusive="-P2D",
            max_inclusive="P2D"
        )
    )
    ely_mdmin_max_exclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDMinMaxExclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_exclusive="-P2D",
            max_exclusive="P2D"
        )
    )
