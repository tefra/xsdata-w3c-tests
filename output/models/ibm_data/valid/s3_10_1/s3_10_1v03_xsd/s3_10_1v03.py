from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    """
    :ivar q_element:
    """
    class Meta:
        name = "t"

    q_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "q",
            "required": True,
        }
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
