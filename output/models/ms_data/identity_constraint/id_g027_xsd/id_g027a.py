from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "importNS"


@dataclass
class R:
    """
    :ivar content:
    :ivar val2:
    """
    class Meta:
        name = "r"
        namespace = "importNS"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    val2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="importNS"
        )
    )
