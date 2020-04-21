from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "bar"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "bar"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
        namespace = "bar"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class C:
    """
    :ivar value:
    """
    class Meta:
        name = "c"
        namespace = "bar"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
