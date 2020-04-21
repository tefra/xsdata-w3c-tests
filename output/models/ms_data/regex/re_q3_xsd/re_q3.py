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
            pattern=r"\i"
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
