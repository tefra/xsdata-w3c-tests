from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_baseTD"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_baseTD"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=3,
            pattern=r"b+"
        )
    )
