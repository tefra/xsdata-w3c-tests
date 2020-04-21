from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar a_ns_element:
    :ivar b_ns_element:
    """
    class Meta:
        name = "doc"
        nillable = True

    a_ns_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://a.ns/",
            min_occurs=2,
            max_occurs=5
        )
    )
    b_ns_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="http://b.ns/",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
