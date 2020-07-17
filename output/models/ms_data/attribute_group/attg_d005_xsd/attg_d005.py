from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar att1:
    :ivar foo:
    :ivar att2:
    :ivar bar:
    :ivar att3:
    """
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    foo: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    bar: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            max_exclusive=100.0
        )
    )
    att3: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
