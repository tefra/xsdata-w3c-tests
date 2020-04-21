from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar att:
    """
    class Meta:
        name = "doc"

    foo: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    att: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
