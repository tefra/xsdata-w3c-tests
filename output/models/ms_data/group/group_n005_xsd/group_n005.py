from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elem:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "elem"

    a1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    a2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
