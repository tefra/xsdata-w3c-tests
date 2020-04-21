from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar foo:
    :ivar sg:
    """
    class Meta:
        name = "root"

    foo: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sg: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
