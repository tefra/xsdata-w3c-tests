from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    """
    :ivar ele:
    """
    ele: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
