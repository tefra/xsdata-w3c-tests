from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v05"


@dataclass
class Root:
    """
    :ivar el_max_exclusive_min_inclusive:
    :ivar el_max_exclusive_min_exclusive:
    :ivar el_max_exclusive_max_inclusive:
    :ivar el_max_exclusive_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v05"

    el_max_exclusive_min_inclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elMaxExclusive_MinInclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_inclusive="-P39DT3M",
            max_exclusive="P28D"
        )
    )
    el_max_exclusive_min_exclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elMaxExclusive_MinExclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_exclusive="-P39DT2M",
            max_exclusive="P28D"
        )
    )
    el_max_exclusive_max_inclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elMaxExclusive_MaxInclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            max_exclusive="P28D",
            max_inclusive="P27DT3M"
        )
    )
    el_max_exclusive_max_exclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elMaxExclusive_MaxExclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            max_exclusive="P27D"
        )
    )
