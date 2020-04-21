from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E1:
    """
    :ivar e3:
    :ivar e4:
    :ivar e5:
    """
    class Meta:
        name = "e1"
        nillable = True

    e3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    e4: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    e5: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Root:
    """
    :ivar e1:
    """
    class Meta:
        name = "root"

    e1: Optional[E1] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
