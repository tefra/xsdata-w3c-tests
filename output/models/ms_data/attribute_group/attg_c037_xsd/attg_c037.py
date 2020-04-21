from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar foo1:
    :ivar foo2:
    """
    class Meta:
        name = "test"

    foo1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    foo2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc(Test):
    class Meta:
        name = "doc"
