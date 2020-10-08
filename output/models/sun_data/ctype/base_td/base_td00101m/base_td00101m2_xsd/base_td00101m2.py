from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "baseTD"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "baseTD"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
