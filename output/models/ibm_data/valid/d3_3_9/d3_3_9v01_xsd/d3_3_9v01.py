from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_9_v01"


@dataclass
class Root:
    """
    :ivar el_time1:
    :ivar el_time2:
    :ivar el_time3:
    :ivar el_time4:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_9_v01"

    el_time1: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elTime1",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive="08:00:00+10:00"
        )
    )
    el_time2: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elTime2",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive="00:00:00+01:00"
        )
    )
    el_time3: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elTime3",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive="10:00:00+13:00"
        )
    )
    el_time4: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elTime4",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_inclusive="03:00:00+04:00"
        )
    )
