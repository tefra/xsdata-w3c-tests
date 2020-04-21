from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    """
    :ivar att1:
    :ivar att2:
    :ivar bar:
    """
    class Meta:
        name = "attRef"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    bar: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    :ivar x1:
    :ivar x2:
    :ivar foo:
    """
    class Meta:
        name = "doc"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    x1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    x2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    foo: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
