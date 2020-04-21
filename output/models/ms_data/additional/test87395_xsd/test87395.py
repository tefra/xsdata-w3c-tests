from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


class St(Enum):
    """
    :cvar A:
    """
    A = "a"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "foo"

    value: Optional[St] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar a:
    """
    class Meta:
        name = "doc"
        namespace = "foo"

    a: Optional[A] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
