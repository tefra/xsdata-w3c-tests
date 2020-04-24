from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Date:
    """
    :ivar value:
    """
    class Meta:
        name = "date"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Outer:
    """
    :ivar date:
    """
    class Meta:
        name = "outer"

    date: List[Date] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
