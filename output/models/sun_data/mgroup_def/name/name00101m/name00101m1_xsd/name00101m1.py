from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "name"


@dataclass
class A1:
    """
    :ivar c:
    """
    class Meta:
        name = "A"

    c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "name"
