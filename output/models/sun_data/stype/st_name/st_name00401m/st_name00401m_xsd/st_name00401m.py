from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_name"


@dataclass
class Test:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            pattern=r"1|2|3"
        )
    )
