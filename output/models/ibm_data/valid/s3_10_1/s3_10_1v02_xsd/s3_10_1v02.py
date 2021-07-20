from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class D:
    class Meta:
        name = "d"
        namespace = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class T:
    class Meta:
        name = "t"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 1,
        }
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
