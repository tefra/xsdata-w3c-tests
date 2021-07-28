from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class B:
    class Meta:
        name = "b"
        nillable = True
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class T:
    class Meta:
        name = "t"

    b: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
            "nillable": True,
        }
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
