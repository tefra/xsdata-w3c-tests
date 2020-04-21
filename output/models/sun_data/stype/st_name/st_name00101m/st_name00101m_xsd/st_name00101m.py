from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_name"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"1|2|3"
        )
    )
