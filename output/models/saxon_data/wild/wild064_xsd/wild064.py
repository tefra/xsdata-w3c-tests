from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class G:
    """
    :ivar value:
    """
    class Meta:
        name = "g"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Zing:
    """
    :ivar g:
    :ivar e:
    :ivar f:
    :ivar local_element:
    """
    class Meta:
        name = "zing"

    g: Optional[G] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    e: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    f: Optional[int] = field(
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