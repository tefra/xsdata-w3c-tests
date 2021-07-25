from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    class Meta:
        name = "t"

    a_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "a",
        }
    )


@dataclass
class X:
    class Meta:
        name = "x"
        namespace = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
