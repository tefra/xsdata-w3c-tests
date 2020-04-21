from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v04"


@dataclass
class Root:
    """
    :ivar eld_time_union_a:
    :ivar eld_time_union_b:
    :ivar eld_time_union_c:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v04"

    eld_time_union_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeUnionA",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            explicit_timezone="required"
        )
    )
    eld_time_union_b: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeUnionB",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            explicit_timezone="prohibited"
        )
    )
    eld_time_union_c: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeUnionC",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            explicit_timezone="optional"
        )
    )
