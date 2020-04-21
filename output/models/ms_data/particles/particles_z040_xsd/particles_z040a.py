from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class A1:
    """
    :ivar value:
    """
    class Meta:
        name = "a1"
        namespace = "a"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class A2:
    """
    :ivar value:
    """
    class Meta:
        name = "a2"
        namespace = "a"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
