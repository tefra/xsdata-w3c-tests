from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_targetNS"


@dataclass
class Test:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"1|2",
        }
    )
