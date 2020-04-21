from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    """
    :ivar e:
    """
    e: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Abc(B):
    """
    :ivar att:
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "abc"

    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc(Abc):
    class Meta:
        name = "doc"
