from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar start:
    :ivar end:
    :ivar attr:
    """
    class Meta:
        name = "root"

    start: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    end: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
