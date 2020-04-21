from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "systemId"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "systemId"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
