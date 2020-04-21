from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_final"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_final"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"1"
        )
    )
