from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Zing:
    """
    :ivar e:
    :ivar f:
    :ivar local_element:
    """
    class Meta:
        name = "zing"

    e: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    f: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local",
            required=True
        )
    )


@dataclass
class Doc(Zing):
    class Meta:
        name = "doc"
