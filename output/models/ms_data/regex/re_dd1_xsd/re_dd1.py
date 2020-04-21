from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Regex:
    """
    :ivar att:
    """
    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"P\p{Nd}{4}Y\p{Nd}{2}M"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: List[Regex] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
