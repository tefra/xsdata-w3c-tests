from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
    class Meta:
        name = "doc"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    c: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    d: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )