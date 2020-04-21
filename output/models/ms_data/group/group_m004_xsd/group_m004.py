from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elem:
    """
    :ivar a1:
    """
    class Meta:
        name = "elem"

    a1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
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
