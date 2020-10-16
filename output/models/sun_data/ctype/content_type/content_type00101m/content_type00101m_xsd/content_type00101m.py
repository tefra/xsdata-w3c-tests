from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A1:
    """
    :ivar attr1:
    """
    class Meta:
        name = "A"

    attr1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
