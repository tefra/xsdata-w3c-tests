from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar total1:
    :ivar total2:
    """
    total1: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Total1",
            type="Element",
            namespace="",
            required=True,
            total_digits=3
        )
    )
    total2: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Total2",
            type="Element",
            namespace="",
            required=True,
            min_exclusive=100.0,
            total_digits=3
        )
    )