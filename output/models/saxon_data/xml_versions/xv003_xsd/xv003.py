from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    """
    :ivar content:
    :ivar att:
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
    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
