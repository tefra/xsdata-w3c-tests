from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "importNS"


@dataclass
class Iid:
    """
    :ivar value:
    :ivar val:
    """
    class Meta:
        name = "iid"
        namespace = "importNS"

    value: Optional[str] = field(
        default=None,
    )
    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="importNS"
        )
    )