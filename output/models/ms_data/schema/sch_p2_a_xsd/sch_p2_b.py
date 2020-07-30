from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BE1:
    """
    :ivar value:
    """
    class Meta:
        name = "b-e1"
        namespace = "ns-a"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=4
        )
    )
