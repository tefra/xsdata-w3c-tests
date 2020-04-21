from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "importNS"


@dataclass
class R:
    """
    :ivar value:
    """
    class Meta:
        name = "r"
        namespace = "importNS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
