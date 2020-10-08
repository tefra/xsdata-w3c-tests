from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
        nillable = True
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class T:
    """
    :ivar b:
    """
    class Meta:
        name = "t"

    b: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True,
            nillable=True
        )
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
