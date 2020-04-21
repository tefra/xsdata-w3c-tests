from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar e:
    :ivar f:
    """
    class Meta:
        name = "root"
        nillable = True

    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    f: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
