from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    """
    :ivar x:
    """
    x: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Elem(B):
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "elem"

    a1: Optional[object] = field(
        default=None,
        metadata=dict(
            name="A1",
            type="Element",
            namespace=""
        )
    )
    a2: Optional[object] = field(
        default=None,
        metadata=dict(
            name="A2",
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
