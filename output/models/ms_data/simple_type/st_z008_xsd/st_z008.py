from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class T2:
    """
    :ivar value:
    :ivar att:
    """
    class Meta:
        name = "t2"

    value: Optional[object] = field(
        default=None,
    )
    att: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "root"

    e1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10
        )
    )
    e2: List[T2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10
        )
    )
