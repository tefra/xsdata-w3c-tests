from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar foo:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )