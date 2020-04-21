from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ct:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "ct"

    e1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_exclusive=2.0,
            min_inclusive=2.0
        )
    )
    e2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            min_exclusive=2.0,
            min_inclusive=3.0
        )
    )


@dataclass
class Root(Ct):
    pass
