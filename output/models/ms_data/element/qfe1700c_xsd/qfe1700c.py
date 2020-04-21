from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E2:
    """
    :ivar content:
    :ivar e3:
    """
    class Meta:
        name = "e2"
        nillable = True

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    e3: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar e1:
    :ivar any_element:
    :ivar e2:
    """
    class Meta:
        name = "root"

    e1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    e2: Optional[E2] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
