from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v04"


@dataclass
class Root:
    """
    :ivar eld_time_stamp_union_a:
    :ivar eld_time_stamp_union_b:
    :ivar eld_time_stamp_union_c:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v04"

    eld_time_stamp_union_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampUnionA",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    eld_time_stamp_union_b: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampUnionB",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    eld_time_stamp_union_c: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampUnionC",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*"
        )
    )
