from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar y:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )