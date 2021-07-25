from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    class Meta:
        name = "t"

    q_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "q",
        }
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
