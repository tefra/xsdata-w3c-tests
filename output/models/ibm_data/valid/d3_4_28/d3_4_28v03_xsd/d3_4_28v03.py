from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v03"


@dataclass
class EldTimeStampListC:
    """
    :ivar value: Tests the simpleType dateTimeStamp used in a lists
    """
    class Meta:
        name = "eldTimeStampListC"
        namespace = "http://xstest-tns/schema11_D3_4_28_v03"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*"
        )
    )


@dataclass
class DTimeStampRoot:
    """
    :ivar eld_time_stamp_pattern:
    :ivar eld_time_stamp_list_a:
    :ivar eld_time_stamp_list_b:
    :ivar eld_time_stamp_list_c:
    """
    class Meta:
        name = "dTimeStampRoot"

    eld_time_stamp_pattern: Optional[str] = field(
        default=None,
        metadata=dict(
            name="eldTimeStampPattern",
            type="Element",
            namespace="",
            required=True,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*"
        )
    )
    eld_time_stamp_list_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampListA",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    eld_time_stamp_list_b: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampListB",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    eld_time_stamp_list_c: Optional[EldTimeStampListC] = field(
        default=None,
        metadata=dict(
            name="eldTimeStampListC",
            type="Element",
            namespace="http://xstest-tns/schema11_D3_4_28_v03",
            required=True
        )
    )


@dataclass
class Root(DTimeStampRoot):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v03"
