from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar base:
    """
    class Meta:
        name = "root"

    base: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace",
            required=True
        )
    )
