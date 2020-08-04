from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Bad:
    """
    :ivar value:
    """
    class Meta:
        name = "bad"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            tokens=True
        )
    )


@dataclass
class Good:
    """
    :ivar value:
    """
    class Meta:
        name = "good"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
