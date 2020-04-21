from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "importNS"


@dataclass
class R:
    """
    :ivar content:
    :ivar val:
    """
    class Meta:
        name = "r"
        namespace = "importNS"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
