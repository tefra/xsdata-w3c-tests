from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "compositor"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "compositor"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "compositor"
