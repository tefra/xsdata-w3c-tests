from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )