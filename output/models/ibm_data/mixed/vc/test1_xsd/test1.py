from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"

    value: Optional[int] = field(
        default=None,
    )
