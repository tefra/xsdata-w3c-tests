from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )