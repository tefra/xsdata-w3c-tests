from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Outer:
    """
    :ivar value:
    """
    class Meta:
        name = "outer"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Value:
    """
    :ivar value:
    """
    class Meta:
        name = "value"

    value: Optional[str] = field(
        default=None,
    )
