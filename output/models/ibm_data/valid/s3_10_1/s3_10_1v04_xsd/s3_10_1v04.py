from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class T:
    class Meta:
        name = "t"

    z: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Z:
    class Meta:
        name = "z"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
