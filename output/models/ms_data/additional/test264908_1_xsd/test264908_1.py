from dataclasses import dataclass, field
from typing import Optional


@dataclass
class T:
    """
    :ivar blah:
    """
    class Meta:
        name = "t"

    blah: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )